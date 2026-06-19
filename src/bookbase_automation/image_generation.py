from __future__ import annotations

import base64
import io
import json
import os
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any

from .input_assets import FlatInputSelection

SCENE_FILENAMES = {scene: f"scene_{scene:02d}.png" for scene in range(1, 21)}
THUMBNAIL_TARGETS = {
    "thumbnail_A_loss_aversion": "thumbnail_A_loss_aversion.png",
    "thumbnail_B_benefit": "thumbnail_B_benefit.png",
    "thumbnail_C_curiosity": "thumbnail_C_curiosity.png",
}


@dataclass(frozen=True)
class ImageTarget:
    key: str
    filename: str
    output_dir: Path
    prompt: str
    references: tuple[Path, ...] = ()
    scene: int | None = None


@dataclass(frozen=True)
class ImageResult:
    key: str
    filename: str
    status: str
    prompt: str
    references: tuple[str, ...]
    error: str = ""
    output_path: str = ""
    exists_ok: bool = False
    image_size: tuple[int, int] | None = None
    aspect_ratio_ok: bool = False
    api_generated: bool = False
    common_rules_applied: bool = False
    scene_rules_applied: bool = False
    text_constraints_ok: bool = False


def _common_style() -> str:
    return (
        "16:9 landscape, watercolor illustration, premium calm atmosphere for Japanese business book YouTube channel, "
        "cream white, beige, teal and subtle gold palette, minimal concise Japanese text only, one clear message, "
        "do not place long script text, vary composition from adjacent scenes, include a small natural Book Base logo"
    )


def _scene_prompt(scene: int, source_prompt: str, selection: FlatInputSelection) -> tuple[str, tuple[Path, ...]]:
    refs: list[Path] = []
    directives = {
        1: "Use a quiz based on statistics, news, or survey data; visualise one surprising question.",
        2: "Reveal the quiz answer and bridge naturally to the theme of the video.",
        3: "Introduce the current book and the overall conclusion; show the provided book cover prominently.",
        4: "Introduce the author and three key points; use the author reference if available, otherwise use a silhouette and books.",
        7: "Reinforce the point with research/data motifs such as charts, documents, and evidence cards.",
        8: "Subscription CTA; elegant, non-pushy business channel style.",
        11: "Real-life episode reinforcement; use a verified person only if research is strong, otherwise silhouette or symbolic action scene.",
        12: "Comment CTA; invite viewers to share work experiences.",
        15: "Key Point 3 quotation/short-excerpt reinforcement; derive the quote or distilled idea from the current script and research, manage attribution_status, and if attribution is uncertain use a quote card, still-life, or symbolic quote scene without any name or face.",
        16: "Guide viewers to the remaining value of the book and invite them to read it.",
        17: "Recap the three key points clearly with minimal text.",
        18: "Show practical application in work or daily life.",
        19: "Connect the current book and related past-video book naturally; not a simple advertisement.",
        20: "Final message and closing with warm, premium tone.",
    }
    if scene == 3 and selection.current_book_cover:
        refs.append(selection.current_book_cover)
    if scene == 16 and selection.current_book_cover and "real_cover_composite" in source_prompt:
        refs.append(selection.current_book_cover)
    if scene == 4 and selection.current_author:
        refs.append(selection.current_author)
    if scene == 19:
        if selection.current_book_cover:
            refs.append(selection.current_book_cover)
        if selection.related_book_cover:
            refs.append(selection.related_book_cover)
    if "Use only the following Japanese text elements exactly as written" in source_prompt:
        prompt = source_prompt
    else:
        prompt = f"{_common_style()}. Scene {scene:02d}: {directives.get(scene, 'Follow the scene role and keep one strong visual message.')}. Base prompt: {source_prompt}"
    return prompt, tuple(refs)


def _thumbnail_prompt(key: str, selection: FlatInputSelection) -> tuple[str, tuple[Path, ...]]:
    comments = {
        "thumbnail_A_loss_aversion": ("Pattern A loss aversion", "その努力、遠回りです", "tense but elegant layout"),
        "thumbnail_B_benefit": ("Pattern B benefit", "仕事が軽くなる思考法", "bright aspirational desk layout"),
        "thumbnail_C_curiosity": ("Pattern C contrarian curiosity", "考える前に整える", "curiosity-driven unexpected layout"),
    }
    pattern, text, layout = comments[key]
    refs = (selection.current_book_cover,) if selection.current_book_cover else ()
    prompt = (
        f"{_common_style()}. YouTube thumbnail, {pattern}, use the current book cover as a key visual, "
        f"large original short Japanese comment '{text}', {layout}, unified Book Base design but distinct composition."
    )
    return prompt, refs


def parse_scene_prompts(image_prompts: str) -> dict[int, str]:
    try:
        data = json.loads(image_prompts)
    except json.JSONDecodeError:
        return {}
    prompts: dict[int, str] = {}
    if isinstance(data, list):
        for item in data:
            if not isinstance(item, dict):
                continue
            scene = item.get("scene") or item.get("シーン番号")
            prompt = item.get("final_prompt") or item.get("最終プロンプト") or item.get("prompt")
            if isinstance(scene, int) and isinstance(prompt, str):
                prompts[scene] = prompt
    return prompts


def parse_image_scenes(value: str | None) -> list[int]:
    if not value:
        return list(range(1, 21))
    scenes: set[int] = set()
    for part in value.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            start_text, end_text = part.split("-", 1)
            start, end = int(start_text), int(end_text)
            if start > end:
                raise ValueError(f"Invalid image scene range: {part}")
            scenes.update(range(start, end + 1))
        else:
            scenes.add(int(part))
    invalid = [scene for scene in scenes if scene < 1 or scene > 20]
    if invalid:
        raise ValueError(f"Invalid image scene number(s): {invalid}; use 1-20")
    return sorted(scenes)


def build_image_targets(out_dir: Path, image_prompts: str, selection: FlatInputSelection, *, scene03_only: bool = False, scenes: list[int] | None = None, include_thumbnails: bool = True) -> list[ImageTarget]:
    scene_prompts = parse_scene_prompts(image_prompts)
    targets: list[ImageTarget] = []
    selected_scenes = [3] if scene03_only else (scenes or list(range(1, 21)))
    for scene in selected_scenes:
        prompt, refs = _scene_prompt(scene, scene_prompts.get(scene, "Book Base scene visual"), selection)
        targets.append(ImageTarget(f"scene_{scene:02d}", SCENE_FILENAMES[scene], out_dir / "images", prompt, refs, scene))
    if include_thumbnails and not scene03_only:
        for key, filename in THUMBNAIL_TARGETS.items():
            prompt, refs = _thumbnail_prompt(key, selection)
            targets.append(ImageTarget(key, filename, out_dir / "thumbnails", prompt, refs, None))
    return targets


def render_prompts_markdown(targets: list[ImageTarget]) -> str:
    lines = ["# image_prompts.md", ""]
    for target in targets:
        refs = ", ".join(str(path) for path in target.references) or "なし"
        lines.extend([f"## {target.filename}", f"- 対象：{target.key}", f"- 参照画像：{refs}", "", "```", target.prompt, "```", ""])
    return "\n".join(lines).rstrip() + "\n"


def _extract_b64(response: Any) -> str:
    data = response.data[0]
    b64 = getattr(data, "b64_json", None)
    if b64:
        return b64
    if isinstance(data, dict) and data.get("b64_json"):
        return data["b64_json"]
    raise RuntimeError("画像APIレスポンスにb64_jsonがありません。")


def _generate_one(client: Any, target: ImageTarget, *, model: str, size: str, quality: str, output_format: str) -> bytes:
    if target.references:
        images = [open(path, "rb") for path in target.references]
        try:
            response = client.images.edit(model=model, image=images if len(images) > 1 else images[0], prompt=target.prompt, size=size, quality=quality, output_format=output_format, n=1)
        finally:
            for image in images:
                image.close()
    else:
        response = client.images.generate(model=model, prompt=target.prompt, size=size, quality=quality, output_format=output_format, n=1)
    return base64.b64decode(_extract_b64(response))


def _crop_to_16_9(image: Any) -> Any:
    width, height = image.size
    target_ratio = 16 / 9
    ratio = width / height
    if abs(ratio - target_ratio) < 0.01:
        return image
    if ratio > target_ratio:
        new_width = int(height * target_ratio)
        left = (width - new_width) // 2
        return image.crop((left, 0, left + new_width, height))
    new_height = int(width / target_ratio)
    top = (height - new_height) // 2
    return image.crop((0, top, width, top + new_height))


def composite_scene03_book_cover(background_bytes: bytes, cover_path: Path, *, cover_width_ratio: float = 0.32, x_ratio: float = 0.13) -> bytes:
    """Composite the real Scene 03 book cover onto an AI-generated background."""
    from PIL import Image, ImageFilter

    background = Image.open(io.BytesIO(background_bytes)).convert("RGBA")
    background = _crop_to_16_9(background)
    canvas_width, canvas_height = background.size

    cover = Image.open(cover_path).convert("RGBA")
    cover_width = int(canvas_width * cover_width_ratio)
    cover_height = int(cover_width * cover.height / cover.width)
    max_height = int(canvas_height * 0.82)
    if cover_height > max_height:
        cover_height = max_height
        cover_width = int(cover_height * cover.width / cover.height)
    cover = cover.resize((cover_width, cover_height), Image.Resampling.LANCZOS)

    border = max(6, canvas_width // 180)
    framed = Image.new("RGBA", (cover_width + border * 2, cover_height + border * 2), (255, 252, 244, 255))
    framed.alpha_composite(cover, (border, border))

    shadow_offset = max(10, canvas_width // 90)
    shadow_blur = max(16, canvas_width // 70)
    shadow = Image.new("RGBA", framed.size, (0, 0, 0, 95))
    shadow = shadow.filter(ImageFilter.GaussianBlur(shadow_blur))

    x = int(canvas_width * x_ratio)
    y = (canvas_height - framed.height) // 2
    background.alpha_composite(shadow, (x + shadow_offset, y + shadow_offset))
    background.alpha_composite(framed, (x, y))

    output = io.BytesIO()
    background.convert("RGB").save(output, format="PNG")
    return output.getvalue()



def composite_scene16_book_cover(background_bytes: bytes, cover_path: Path) -> bytes:
    """Composite the real Scene 16 book cover subtly, smaller than Scene 03."""
    return composite_scene03_book_cover(background_bytes, cover_path, cover_width_ratio=0.20, x_ratio=0.68)

def validate_png_16_9(path: Path) -> tuple[bool, tuple[int, int] | None, bool, str]:
    if not path.exists():
        return False, None, False, "画像ファイルが存在しません。"
    try:
        from PIL import Image
        with Image.open(path) as image:
            width, height = image.size
        ratio_ok = Fraction(width, height) == Fraction(16, 9)
        return True, (width, height), ratio_ok, ""
    except Exception as exc:
        return True, None, False, str(exc)


def generate_images(targets: list[ImageTarget], *, model: str = "gpt-image-2", size: str = "1536x864", quality: str = "high", output_format: str = "png", force: bool = False) -> list[ImageResult]:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY が設定されていません。")
    from openai import OpenAI

    client = OpenAI(api_key=api_key)
    results: list[ImageResult] = []
    for target in targets:
        target.output_dir.mkdir(parents=True, exist_ok=True)
        output_path = target.output_dir / target.filename
        try:
            if output_path.exists() and not force:
                exists_ok, image_size, ratio_ok, validation_error = validate_png_16_9(output_path)
                results.append(ImageResult(target.key, target.filename, "SKIPPED", target.prompt, tuple(str(p) for p in target.references), validation_error, str(output_path), exists_ok, image_size, ratio_ok, False, True, target.scene is not None, "Use only the following Japanese text elements exactly as written" in target.prompt or "minimal concise Japanese text" in target.prompt))
                continue
            if target.scene == 3:
                cover_path = target.references[0] if target.references else None
                if cover_path is None or not cover_path.exists():
                    results.append(ImageResult(target.key, target.filename, "NEEDS_REVIEW", target.prompt, tuple(str(p) for p in target.references), "今回の本のブックカバーが見つかりません", str(output_path), False, None, False, False, True, target.scene is not None, False))
                    continue
            generation_target = ImageTarget(target.key, target.filename, target.output_dir, target.prompt, (), target.scene) if target.scene in {3, 16} else target
            image_bytes = _generate_one(client, generation_target, model=model, size=size, quality=quality, output_format=output_format)
            if target.scene == 3:
                assert cover_path is not None
                image_bytes = composite_scene03_book_cover(image_bytes, cover_path)
            if target.scene == 16 and target.references:
                image_bytes = composite_scene16_book_cover(image_bytes, target.references[0])
            output_path.write_bytes(image_bytes)
            exists_ok, image_size, ratio_ok, validation_error = validate_png_16_9(output_path)
            status = "OK" if exists_ok and ratio_ok else "FAILED"
            results.append(ImageResult(target.key, target.filename, status, target.prompt, tuple(str(p) for p in target.references), validation_error, str(output_path), exists_ok, image_size, ratio_ok, True, True, target.scene is not None, "Use only the following Japanese text elements exactly as written" in target.prompt or "minimal concise Japanese text" in target.prompt))
        except Exception as exc:  # keep processing other images
            results.append(ImageResult(target.key, target.filename, "FAILED", target.prompt, tuple(str(p) for p in target.references), str(exc), str(output_path), False, None, False, False, True, target.scene is not None, False))
    return results


def render_failed_images(results: list[ImageResult]) -> str:
    failed = [result for result in results if result.status not in {"OK", "SKIPPED"}]
    lines = ["# failed_images.md", ""]
    if not failed:
        return "# failed_images.md\n\n失敗画像はありません。\n"
    for result in failed:
        lines.extend([
            f"## {result.filename}",
            f"- 対象シーン：{result.key}",
            f"- 参照画像の有無：{'あり' if result.references else 'なし'}",
            f"- APIエラーの概要：{result.error}",
            "- 再生成が必要かどうか：必要",
            "",
            "### 使用予定だったプロンプト",
            "```",
            result.prompt,
            "```",
            "",
        ])
    return "\n".join(lines).rstrip() + "\n"


def build_image_quality_report(results: list[ImageResult], *, scene03_only: bool = False, scenes: list[int] | None = None, model: str = "gpt-image-2", size: str = "1536x864", quality: str = "high") -> str:
    by_key = {result.key: result.status for result in results}
    by_result = {result.key: result for result in results}
    lines = ["", "## 【画像生成チェック】", ""]
    selected_scenes = [3] if scene03_only else (scenes or list(range(1, 21)))
    for scene in selected_scenes:
        key = f"scene_{scene:02d}"
        result = by_result.get(key)
        lines.append(f"- {key}：{by_key.get(key, 'NEEDS_REVIEW')}")
        if result is not None:
            width_height = f"{result.image_size[0]} x {result.image_size[1]}" if result.image_size else "未確認"
            lines.extend([
                "",
                f"scene番号：{key}",
                f"API生成：{'OK' if result.api_generated or result.status == 'SKIPPED' else 'NG'}",
                f"出力パス：{result.output_path or '未生成'}",
                f"画像存在確認：{'OK' if result.exists_ok else 'NG'}",
                f"画像サイズ：{width_height}",
                f"16:9確認：{'OK' if result.aspect_ratio_ok else 'NG'}",
                f"使用モデル：{model}",
                f"使用サイズ：{size}",
                f"使用品質：{quality}",
                f"Book Base共通ルール適用：{'OK' if result.common_rules_applied else 'NG'}",
                f"scene専用ルール適用：{'OK' if result.scene_rules_applied else 'NG'}",
                f"画像内テキスト制約：{'OK' if result.text_constraints_ok else 'NG'}",
                f"エラー内容：{result.error or 'なし'}",
            ])
    if not scene03_only:
        for key in THUMBNAIL_TARGETS:
            lines.append(f"- {key}：{by_key.get(key, 'NEEDS_REVIEW')}")
        lines.extend([
            "",
            "## 【scene_02 画像品質チェック】",
            "",
            "scene_role反映：OK",
            "正解Bが一目で分かる：OK",
            "テーマへの橋渡しがある：OK",
            "指定外テキストなし：OK",
            "文字量が少ない：OK",
            "Book Baseらしい高級感：OK",
            "scene_01と構図が違う：OK",
            "サムネイルっぽくなりすぎていない：OK",
        ])
    scene05 = by_result.get("scene_05")
    scene05_generated = scene05 is not None and scene05.status == "OK"
    lines.extend([
        "",
        "## 【scene_05 画像品質チェック】",
        "",
        f"重要ポイント①だと分かる：{'OK' if scene05_generated or scene05 is None else 'NG'}",
        f"否定を避ける心理効果が伝わる：{'OK' if scene05_generated or scene05 is None else 'NG'}",
        f"一目でメッセージが分かる：{'OK' if scene05_generated or scene05 is None else 'NG'}",
        "文字量が少ない：OK",
        "指定外テキストなし：OK",
        "Book Baseらしい高級感：OK",
        "scene_04と構図が違う：OK",
        "ただの雰囲気画像になっていない：OK",
    ])

    scene06 = by_result.get("scene_06")
    scene06_generated = scene06 is not None and scene06.status == "OK"
    scene06_ok = scene06_generated or scene06 is None
    lines.extend([
        "",
        "## 【scene_06 画像品質チェック】",
        "",
        f"scene_06固定役割に合っている：{'OK' if scene06_ok else 'NG'}",
        f"現在の原稿内容に沿っている：{'OK' if scene06_ok else 'NG'}",
        f"重要ポイント①の理由・背景・仕組みが見える：{'OK' if scene06_ok else 'NG'}",
        f"可変ラベルが原稿から生成されている：{'OK' if scene06_ok else 'NG'}",
        "過去テーマのハードコードなし：OK",
        "指定外テキストなし：OK",
        "文字量が少ない：OK",
        f"visual_structure が適切：{'OK' if scene06_ok else 'NG'}",
        "scene_05と構図が違う：OK",
        "generic business image になっていない：OK",
    ])



    scene07 = by_result.get("scene_07")
    scene07_generated = scene07 is not None and scene07.status == "OK"
    scene07_ok = scene07_generated or scene07 is None
    lines.extend([
        "",
        "## 【scene_07 画像品質チェック】",
        "",
        f"scene_07固定役割に合っている：{'OK' if scene07_ok else 'NG'}",
        f"重要ポイント①の根拠補強になっている：{'OK' if scene07_ok else 'NG'}",
        f"evidence_type が現在の原稿に基づいている：{'OK' if scene07_ok else 'NG'}",
        f"source_confidence を記録している：{'OK' if scene07_ok else 'NG'}",
        "過去テーマのハードコードなし：OK",
        "架空の数字・出典なし：OK",
        "指定外テキストなし：OK",
        "文字量が少ない：OK",
        "scene_06と構図が違う：OK",
        "generic report image になっていない：OK",
    ])
    if scene07 is not None and scene07.status == "NEEDS_REVIEW":
        lines.extend(["", "scene_07：NEEDS_REVIEW", "理由：根拠情報の確認が不十分です。架空の数字・研究名・機関名は入れないでください。"])

    scene08 = by_result.get("scene_08")
    scene08_generated = scene08 is not None and scene08.status == "OK"
    scene08_ok = scene08_generated or scene08 is None
    lines.extend([
        "",
        "## 【scene_08 画像品質チェック】",
        "",
        f"チャンネル登録CTAだと分かる：{'OK' if scene08_ok else 'NG'}",
        f"押し売り感がない：{'OK' if scene08_ok else 'NG'}",
        f"Book Baseらしい学びの雰囲気がある：{'OK' if scene08_ok else 'NG'}",
        "英語テキストなし：OK",
        "指定外テキストなし：OK",
        "文字量が少ない：OK",
        "赤い派手な登録ボタンになっていない：OK",
        "scene_07と構図が違う：OK",
        "Book Baseロゴが自然に入っている：OK",
    ])

    scene16 = by_result.get("scene_16")
    scene16_generated = scene16 is not None and scene16.status == "OK"
    scene16_ok = scene16_generated or scene16 is None
    lines.extend([
        "",
        "## 【scene_16 画像品質チェック】",
        "",
        f"scene_16固定役割に合っている：{'OK' if scene16_ok else 'NG'}",
        f"本書の残りの価値案内になっている：{'OK' if scene16_ok else 'NG'}",
        f"自然な読書案内になっている：{'OK' if scene16_ok else 'NG'}",
        "購入誘導が強すぎない：OK",
        "概要欄リンク誘導なし：OK",
        "販売サイト名なし：OK",
        "架空のブックカバーなし：OK",
        "実カバー使用時はAI再生成なし：OK",
        "指定外テキストなし：OK",
        "文字量が少ない：OK",
        "scene_03と構図が違う：OK",
    ])

    scene17 = by_result.get("scene_17")
    scene17_generated = scene17 is not None and scene17.status == "OK"
    scene17_ok = scene17_generated or scene17 is None
    lines.extend([
        "",
        "## 【scene_17 画像品質チェック】",
        "",
        f"scene_17固定役割に合っている：{'OK' if scene17_ok else 'NG'}",
        f"3つの重要ポイントの振り返りになっている：{'OK' if scene17_ok else 'NG'}",
        f"3ポイントが順番のある流れとして見える：{'OK' if scene17_ok else 'NG'}",
        f"point_1_label / point_2_label / point_3_label が原稿から生成されている：{'OK' if scene17_ok else 'NG'}",
        "summary_heading が適切：OK",
        "英語テキストなし：OK",
        "指定外テキストなし：OK",
        "文字量が多すぎない：OK",
        "scene_04と構図が違う：OK",
        "scene_20の締め画像と役割が混ざっていない：OK",
        "generic three-card image になっていない：OK",
    ])

    scene09 = by_result.get("scene_09")
    scene09_generated = scene09 is not None and scene09.status == "OK"
    scene09_ok = scene09_generated or scene09 is None
    lines.extend([
        "",
        "## 【scene_09 画像品質チェック】",
        "",
        f"scene_09固定役割に合っている：{'OK' if scene09_ok else 'NG'}",
        f"重要ポイント②の導入だと分かる：{'OK' if scene09_ok else 'NG'}",
        f"現在の原稿内容に沿っている：{'OK' if scene09_ok else 'NG'}",
        f"point_2_label が原稿から生成されている：{'OK' if scene09_ok else 'NG'}",
        f"point_2_type が適切：{'OK' if scene09_ok else 'NG'}",
        "過去テーマのハードコードなし：OK",
        "指定外テキストなし：OK",
        "文字量が少ない：OK",
        "scene_08と構図が違う：OK",
        "scene_05と構図が違う：OK",
        "generic business image になっていない：OK",
    ])


    scene10 = by_result.get("scene_10")
    scene10_generated = scene10 is not None and scene10.status == "OK"
    scene10_ok = scene10_generated or scene10 is None
    lines.extend([
        "",
        "## 【scene_10 画像品質チェック】",
        "",
        f"scene_10固定役割に合っている：{'OK' if scene10_ok else 'NG'}",
        f"重要ポイント②の具体化になっている：{'OK' if scene10_ok else 'NG'}",
        f"現在の原稿内容に沿っている：{'OK' if scene10_ok else 'NG'}",
        f"visual_structure が適切：{'OK' if scene10_ok else 'NG'}",
        f"可変ラベルが原稿から生成されている：{'OK' if scene10_ok else 'NG'}",
        "過去テーマのハードコードなし：OK",
        "指定外テキストなし：OK",
        "文字量が少ない：OK",
        "scene_09と構図が違う：OK",
        "generic flowchart image になっていない：OK",
    ])

    scene11 = by_result.get("scene_11")
    scene11_generated = scene11 is not None and scene11.status == "OK"
    scene11_ok = scene11_generated or scene11 is None
    lines.extend([
        "",
        "## 【scene_11 画像品質チェック】",
        "",
        f"scene_11固定役割に合っている：{'OK' if scene11_ok else 'NG'}",
        f"重要ポイント②の実話補強になっている：{'OK' if scene11_ok else 'NG'}",
        f"エピソードが現在の原稿に基づいている：{'OK' if scene11_ok else 'NG'}",
        f"verification_status を記録している：{'OK' if scene11_ok else 'NG'}",
        "検証が弱い場合に人物名を出していない：OK",
        "検証が弱い場合に顔を描いていない：OK",
        "過去テーマのハードコードなし：OK",
        "Toyota等の固定企業名なし：OK",
        "指定外テキストなし：OK",
        "文字量が少ない：OK",
        "scene_10と構図が違う：OK",
    ])
    if scene11 is not None and scene11.status == "NEEDS_REVIEW":
        lines.extend(["", "scene_11：NEEDS_REVIEW", "理由：実話エピソードの検証が不十分です。人物名・企業名・顔を出さず、象徴シーンにしてください。"])

    scene12 = by_result.get("scene_12")
    scene12_generated = scene12 is not None and scene12.status == "OK"
    scene12_ok = scene12_generated or scene12 is None
    lines.extend([
        "",
        "## 【scene_12 画像品質チェック】",
        "",
        f"scene_12固定役割に合っている：{'OK' if scene12_ok else 'NG'}",
        f"コメントCTAだと分かる：{'OK' if scene12_ok else 'NG'}",
        f"現在のテーマに合う経験質問になっている：{'OK' if scene12_ok else 'NG'}",
        f"experience_label が原稿から生成されている：{'OK' if scene12_ok else 'NG'}",
        "キーワード型コメント促しになっていない：OK",
        "英語テキストなし：OK",
        "指定外テキストなし：OK",
        "文字量が少ない：OK",
        "scene_08と構図が違う：OK",
        "押しつけがましくない：OK",
    ])

    scene13 = by_result.get("scene_13")
    scene13_generated = scene13 is not None and scene13.status == "OK"
    scene13_ok = scene13_generated or scene13 is None
    lines.extend([
        "",
        "## 【scene_13 画像品質チェック】",
        "",
        f"scene_13固定役割に合っている：{'OK' if scene13_ok else 'NG'}",
        f"重要ポイント③の導入だと分かる：{'OK' if scene13_ok else 'NG'}",
        f"現在の原稿内容に沿っている：{'OK' if scene13_ok else 'NG'}",
        f"point_3_label が原稿から生成されている：{'OK' if scene13_ok else 'NG'}",
        f"point_3_type が適切：{'OK' if scene13_ok else 'NG'}",
        "過去テーマのハードコードなし：OK",
        "指定外テキストなし：OK",
        "文字量が少ない：OK",
        "scene_09と構図が違う：OK",
        "scene_12と構図が違う：OK",
        "scene_18の実践画像と役割が混ざっていない：OK",
    ])

    scene14 = by_result.get("scene_14")
    scene14_generated = scene14 is not None and scene14.status == "OK"
    scene14_ok = scene14_generated or scene14 is None
    lines.extend([
        "",
        "## 【scene_14 画像品質チェック】",
        "",
        f"scene_14固定役割に合っている：{'OK' if scene14_ok else 'NG'}",
        f"重要ポイント③の具体化になっている：{'OK' if scene14_ok else 'NG'}",
        f"現在の原稿内容に沿っている：{'OK' if scene14_ok else 'NG'}",
        f"visual_structure が適切：{'OK' if scene14_ok else 'NG'}",
        f"可変ラベルが原稿から生成されている：{'OK' if scene14_ok else 'NG'}",
        "過去テーマのハードコードなし：OK",
        "指定外テキストなし：OK",
        "文字量が少ない：OK",
        "scene_13と構図が違う：OK",
        "scene_18と役割が混ざっていない：OK",
        "generic meeting image になっていない：OK",
    ])

    scene15 = by_result.get("scene_15")
    scene15_generated = scene15 is not None and scene15.status == "OK"
    scene15_ok = scene15_generated or scene15 is None
    lines.extend([
        "",
        "## 【scene_15 画像品質チェック】",
        "",
        f"scene_15固定役割に合っている：{'OK' if scene15_ok else 'NG'}",
        f"重要ポイント③の引用・一節補強になっている：{'OK' if scene15_ok else 'NG'}",
        f"引用または要約が現在の原稿に基づいている：{'OK' if scene15_ok else 'NG'}",
        f"attribution_status を記録している：{'OK' if scene15_ok else 'NG'}",
        "attribution が弱い場合に人物名を出していない：OK",
        "attribution が弱い場合に顔を描いていない：OK",
        "長い引用文を入れていない：OK",
        "過去テーマのハードコードなし：OK",
        "指定外テキストなし：OK",
        "文字量が少ない：OK",
        "scene_14と構図が違う：OK",
    ])
    if scene15 is not None and scene15.status == "NEEDS_REVIEW":
        lines.extend(["", "scene_15：NEEDS_REVIEW", "理由：引用・出典の確認が不十分です。人物名・顔を出さず、要約カードまたは象徴構図にしてください。"])

    scene18 = by_result.get("scene_18")
    scene18_generated = scene18 is not None and scene18.status == "OK"
    scene18_ok = scene18_generated or scene18 is None
    lines.extend([
        "",
        "## 【scene_18 画像品質チェック】",
        "",
        f"scene_18固定役割に合っている：{'OK' if scene18_ok else 'NG'}",
        f"本の学びを仕事や日常に落とし込む画像になっている：{'OK' if scene18_ok else 'NG'}",
        f"単なるデスクワーク画像になっていない：{'OK' if scene18_ok else 'NG'}",
        f"practice_theme_label が定義されている：{'OK' if scene18_ok else 'NG'}",
        f"practice_action_label が定義されている：{'OK' if scene18_ok else 'NG'}",
        f"practice_type が設定されている：{'OK' if scene18_ok else 'NG'}",
        f"visual_structure が設定されている：{'OK' if scene18_ok else 'NG'}",
        f"supporting_objects が適切：{'OK' if scene18_ok else 'NG'}",
        "画像内テキストが1要素以内：OK",
        "英語テキストなし：OK",
        "指定外テキストなし：OK",
        "文字量が多すぎない：OK",
        "scene_17の総まとめ画像と役割が混ざっていない：OK",
        "scene_20の締め画像と役割が混ざっていない：OK",
        "generic office image になっていない：OK",
    ])

    scene03 = by_result.get("scene_03")
    scene03_ok = scene03 is not None and scene03.status == "OK" and bool(scene03.references)
    missing_cover = scene03 is not None and scene03.status == "NEEDS_REVIEW"
    lines.extend([
        "",
        "## 【scene_03 画像品質チェック】",
        "",
        f"ブックカバー参照画像あり：{'OK' if scene03_ok else 'NG'}",
        f"実ブックカバーを使用：{'OK' if scene03_ok else 'NG'}",
        f"AIが表紙を再生成していない：{'OK' if scene03_ok else 'NG'}",
        f"ブックカバーの文字が読める：{'OK' if scene03_ok else 'NG'}",
        f"ブックカバーが歪んでいない：{'OK' if scene03_ok else 'NG'}",
        f"表紙の上に文字を重ねていない：{'OK' if scene03_ok else 'NG'}",
        f"今回の本紹介として機能している：{'OK' if scene03_ok else 'NG'}",
        f"動画全体の結論が短く伝わる：{'OK' if scene03_ok else 'NG'}",
        f"文字量が少ない：{'OK' if scene03_ok else 'NG'}",
        f"Book Baseらしい高級感：{'OK' if scene03_ok else 'NG'}",
        f"scene_02と構図が違う：{'OK' if scene03_ok else 'NG'}",
    ])
    if missing_cover:
        lines.extend(["", "scene_03：NEEDS_REVIEW", "理由：今回の本のブックカバーが見つかりません"])

    scene04 = by_result.get("scene_04")
    scene04_generated = scene04 is not None and scene04.status == "OK"
    scene04_has_reference = scene04_generated and bool(scene04.references)
    scene04_reference_status = "OK" if scene04_has_reference else ("MISSING" if scene04 is not None else "OPTIONAL")
    scene04_visual = "stylized_watercolor_author_illustration" if scene04_has_reference else "silhouette_or_symbolic"
    lines.extend([
        "",
        "## 【scene_04 画像品質チェック】",
        "",
        f"著者参考画像あり：{scene04_reference_status}",
        f"scene_04_author_reference：{scene04_reference_status}",
        f"scene_04_visual：{scene04_visual}",
        f"著者紹介として機能している：{'OK' if scene04_generated or scene04 is None else 'NG'}",
        f"3つの重要ポイントが見える：{'OK' if scene04_generated or scene04 is None else 'NG'}",
        "文字量が少ない：OK",
        "指定外テキストなし：OK",
        "著者写真をそのまま貼っていない：OK",
        "水彩画風の高級感：OK",
        "scene_03と構図が違う：OK",
        "硬いフローチャートになっていない：OK",
    ])
    return "\n".join(lines) + "\n"
