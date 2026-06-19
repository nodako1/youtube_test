from __future__ import annotations

import base64
import json
import os
from dataclasses import dataclass
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
        15: "Quotation reinforcement; if attribution is uncertain use a quote card or still-life composition instead of a face.",
        16: "Guide viewers to the remaining value of the book and invite them to read it.",
        17: "Recap the three key points clearly with minimal text.",
        18: "Show practical application in work or daily life.",
        19: "Connect the current book and related past-video book naturally; not a simple advertisement.",
        20: "Final message and closing with warm, premium tone.",
    }
    if scene == 3 and selection.current_book_cover:
        refs.append(selection.current_book_cover)
    if scene == 4 and selection.current_author:
        refs.append(selection.current_author)
    if scene == 19 and selection.related_book_cover:
        refs.append(selection.related_book_cover)
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
            prompt = item.get("最終プロンプト") or item.get("prompt")
            if isinstance(scene, int) and isinstance(prompt, str):
                prompts[scene] = prompt
    return prompts


def build_image_targets(out_dir: Path, image_prompts: str, selection: FlatInputSelection, *, scene03_only: bool = False) -> list[ImageTarget]:
    scene_prompts = parse_scene_prompts(image_prompts)
    targets: list[ImageTarget] = []
    scenes = [3] if scene03_only else list(range(1, 21))
    for scene in scenes:
        prompt, refs = _scene_prompt(scene, scene_prompts.get(scene, "Book Base scene visual"), selection)
        targets.append(ImageTarget(f"scene_{scene:02d}", SCENE_FILENAMES[scene], out_dir / "images", prompt, refs, scene))
    if not scene03_only:
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


def _generate_one(client: Any, target: ImageTarget, *, model: str, size: str) -> bytes:
    if target.references:
        images = [open(path, "rb") for path in target.references]
        try:
            response = client.images.edit(model=model, image=images if len(images) > 1 else images[0], prompt=target.prompt, size=size, n=1)
        finally:
            for image in images:
                image.close()
    else:
        response = client.images.generate(model=model, prompt=target.prompt, size=size, n=1)
    return base64.b64decode(_extract_b64(response))


def generate_images(targets: list[ImageTarget], *, model: str = "gpt-image-1", size: str = "1536x1024") -> list[ImageResult]:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY が設定されていません。")

    from openai import OpenAI

    client = OpenAI(api_key=api_key)
    results: list[ImageResult] = []
    for target in targets:
        target.output_dir.mkdir(parents=True, exist_ok=True)
        try:
            image_bytes = _generate_one(client, target, model=model, size=size)
            (target.output_dir / target.filename).write_bytes(image_bytes)
            results.append(ImageResult(target.key, target.filename, "OK", target.prompt, tuple(str(p) for p in target.references)))
        except Exception as exc:  # keep processing other images
            results.append(ImageResult(target.key, target.filename, "FAILED", target.prompt, tuple(str(p) for p in target.references), str(exc)))
    return results


def render_failed_images(results: list[ImageResult]) -> str:
    failed = [result for result in results if result.status != "OK"]
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


def build_image_quality_report(results: list[ImageResult], *, scene03_only: bool = False) -> str:
    by_key = {result.key: result.status for result in results}
    lines = ["", "## 【画像生成チェック】", ""]
    scenes = [3] if scene03_only else list(range(1, 21))
    for scene in scenes:
        key = f"scene_{scene:02d}"
        lines.append(f"- {key}：{by_key.get(key, 'NEEDS_REVIEW')}")
    if not scene03_only:
        for key in THUMBNAIL_TARGETS:
            lines.append(f"- {key}：{by_key.get(key, 'NEEDS_REVIEW')}")
    return "\n".join(lines) + "\n"
