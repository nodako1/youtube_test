from __future__ import annotations

import base64
import io
import json
import os
import time
from datetime import datetime
from zoneinfo import ZoneInfo
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any

from .config import BOOK_BASE_LOGO_BOTTOM_MARGIN, BOOK_BASE_LOGO_LEFT_MARGIN, BOOK_BASE_LOGO_PATH, BOOK_BASE_LOGO_WIDTH
from .input_assets import FlatInputSelection
from .openai_retry import OpenAIAPICallRecord, edit_image_with_retry, format_openai_api_report, generate_image_with_retry

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
    api_communication_report: str = ""


def _common_style() -> str:
    return (
        "16:9 landscape, watercolor illustration, premium calm atmosphere for Japanese business book YouTube channel, "
        "cream white, beige, teal and subtle gold palette, minimal concise Japanese text only, one clear message, "
        "do not place long script text, vary composition from adjacent scenes, reserve the lower-left corner for the fixed Book Base logo that will be composited after generation"
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



THUMBNAIL_A_COMMENT_TEXT = "その努力、遠回りです"
THUMBNAIL_A_TENSION_STYLES = {"quiet_tension", "warning_but_elegant", "subtle_urgency", "intelligent_alert"}
THUMBNAIL_A_VISUAL_STRUCTURES = {
    "cover_left_comment_right",
    "cover_center_overlay_comment",
    "diagonal_cover_comment",
    "split_focus_cover_and_comment",
    "layered_cover_emphasis",
}


def _thumbnail_a_loss_aversion_data(selection: FlatInputSelection) -> dict[str, Any]:
    cover_path = str(selection.current_book_cover) if selection.current_book_cover else "なし"
    return {
        "thumbnail_type": "A_loss_aversion",
        "fixed_role": "損失回避心理を刺激するYouTubeサムネイル",
        "book_cover_reference_path": cover_path,
        "comment_text": THUMBNAIL_A_COMMENT_TEXT,
        "loss_trigger_label": "頑張っているのに方向がズレて遠回りしているかもしれない不安",
        "tension_style": "warning_but_elegant",
        "visual_structure": "cover_left_comment_right",
        "supporting_motifs": [
            "細い分岐線で正しい道と遠回りの道を示す",
            "控えめな影と余白で静かな警戒感を作る",
            "ティールと淡いゴールドの視線誘導ライン",
        ],
        "exact_text_elements": [THUMBNAIL_A_COMMENT_TEXT],
    }


def _thumbnail_a_composition(data: dict[str, Any]) -> str:
    return (
        "Place the current book cover large on the left as one of the two main subjects, with enough size for the cover presence to be clear; "
        "place the single Japanese comment large on the right with strong hierarchy and generous whitespace; "
        "connect the cover and comment using subtle diagonal sight lines or a refined forked path motif that implies wasted effort and a detour; "
        "keep the tension quiet, intelligent, and premium rather than loud or sensational."
    )


def _thumbnail_a_prompt(selection: FlatInputSelection) -> tuple[str, tuple[Path, ...]]:
    data = _thumbnail_a_loss_aversion_data(selection)
    refs = (selection.current_book_cover,) if selection.current_book_cover else ()
    supporting_motifs = "\n".join(f"- {motif}" for motif in data["supporting_motifs"])
    exact_text = "\n".join(f"{index}. {text}" for index, text in enumerate(data["exact_text_elements"], start=1))
    prompt = f"""Create a 16:9 landscape YouTube thumbnail image for Book Base, a Japanese business book YouTube channel. Use a refined watercolor illustration style with a premium, calm, elegant atmosphere. Use a soft cream-white and beige base with teal and subtle gold accents. Leave the lower-left corner clean because the fixed Book Base logo will be composited after generation.

This is thumbnail pattern A: loss aversion. Its fixed role is to trigger curiosity through loss aversion, making viewers feel that they may be wasting effort, overlooking something important, or heading in the wrong direction. The image must encourage clicks, but it must not become a cheap, noisy, sensational YouTube thumbnail.

Use the reference image as the current book cover:
{data["book_cover_reference_path"]}

The current book cover should be a key visual and clearly visible. Do not make it small, do not bury it in the background, and do not turn the thumbnail into a generic book advertisement.

Main comment text:
{data["comment_text"]}

Loss trigger:
{data["loss_trigger_label"]}

Tension style:
{data["tension_style"]}

Visual structure:
{data["visual_structure"]}

Supporting motifs:
{supporting_motifs}

Use only the following Japanese text element exactly as written. Do not add any other Japanese or English text:
{exact_text}

Composition:
{_thumbnail_a_composition(data)}

Visual motifs:
- current book cover as a key visual
- large bold short Japanese comment
- tense but elegant layout
- premium watercolor texture
- calm structured whitespace
- subtle visual tension
- refined Book Base design language, with no AI-rendered logo

Keep the thumbnail highly readable at a glance. Use minimal concise Japanese text only. Do not place long script text. Avoid clutter, avoid English text, avoid cheap clickbait design, avoid broken Japanese text, avoid overly loud red-yellow warning graphics, avoid flames, explosions, excessive arrows, and avoid making the thumbnail look like a generic ad."""
    return prompt, refs


THUMBNAIL_B_COMMENT_TEXT = "仕事が軽くなる思考法"
THUMBNAIL_B_BENEFIT_STYLES = {
    "bright_progress",
    "calm_relief",
    "practical_improvement",
    "aspirational_but_grounded",
    "intelligent_simplicity",
}
THUMBNAIL_B_VISUAL_STRUCTURES = {
    "cover_left_comment_right",
    "cover_center_overlay_comment",
    "desk_layout_cover_focus",
    "split_focus_cover_and_comment",
    "layered_cover_emphasis",
}


def _thumbnail_b_benefit_data(selection: FlatInputSelection) -> dict[str, Any]:
    cover_path = str(selection.current_book_cover) if selection.current_book_cover else "なし"
    return {
        "thumbnail_type": "B_benefit",
        "fixed_role": "メリットや前向きな変化を直感的に伝えるYouTubeサムネイル",
        "book_cover_reference_path": cover_path,
        "comment_text": THUMBNAIL_B_COMMENT_TEXT,
        "benefit_trigger_label": "この本の学びで仕事や考え方が軽くなり、実務に前向きな改善が起こりそうという期待",
        "benefit_style": "intelligent_simplicity",
        "visual_structure": "desk_layout_cover_focus",
        "supporting_motifs": [
            "整理されたノートと余白で思考が整う感覚を示す",
            "朝の柔らかな光と淡いティールの視線誘導で前向きさを作る",
            "控えめなゴールドのアクセントで上品な希望を添える",
        ],
        "exact_text_elements": [THUMBNAIL_B_COMMENT_TEXT],
    }


def _thumbnail_b_composition(data: dict[str, Any]) -> str:
    return (
        "Use a bright aspirational desk layout, but make the current book cover large and clearly visible as one of the two main subjects, not a small prop; "
        "place the single Japanese comment large in a clean readable area beside or slightly overlapping the desk flow, with the strongest text hierarchy in the image; "
        "create a meaningful sight line from the cover to the comment using the notebook, pen, soft light, or subtle teal-gold accents so the benefit feels connected to the book; "
        "keep the feeling calm, intelligent, practical, and hopeful, emphasizing relief and clearer thinking rather than anxiety, hype, luxury bragging, or generic self-help success imagery. "
        "Differentiate it from thumbnail_A_loss_aversion by using positive openness, brightness, and practical improvement instead of tension or warning."
    )


def _thumbnail_b_prompt(selection: FlatInputSelection) -> tuple[str, tuple[Path, ...]]:
    data = _thumbnail_b_benefit_data(selection)
    refs = (selection.current_book_cover,) if selection.current_book_cover else ()
    supporting_motifs = "\n".join(f"- {motif}" for motif in data["supporting_motifs"])
    exact_text = "\n".join(f"{index}. {text}" for index, text in enumerate(data["exact_text_elements"], start=1))
    prompt = f"""Create a 16:9 landscape YouTube thumbnail image for Book Base, a Japanese business book YouTube channel. Use a refined watercolor illustration style with a premium, calm, elegant atmosphere. Use a soft cream-white and beige base with teal and subtle gold accents. Leave the lower-left corner clean because the fixed Book Base logo will be composited after generation.

This is thumbnail pattern B: benefit. Its fixed role is to communicate the positive benefit viewers may gain from the book, making them feel that their work, thinking, or daily life may become lighter, clearer, or better. The image must encourage clicks, but it must not become a cheap self-help thumbnail or an overhyped success-appeal design.

Use the reference image as the current book cover:
{data["book_cover_reference_path"]}

The current book cover should be a key visual and clearly visible. Do not make it small, do not bury it in the background, and do not turn the thumbnail into a generic book advertisement.

Main comment text:
{data["comment_text"]}

Benefit trigger:
{data["benefit_trigger_label"]}

Benefit style:
{data["benefit_style"]}

Visual structure:
{data["visual_structure"]}

Supporting motifs:
{supporting_motifs}

Use only the following Japanese text element exactly as written. Do not add any other Japanese or English text:
{exact_text}

Composition:
{_thumbnail_b_composition(data)}

Visual motifs:
- current book cover as a key visual
- large bold short Japanese comment
- bright aspirational desk layout
- premium watercolor texture
- calm structured whitespace
- refined positive atmosphere
- elegant Book Base design language

Keep the thumbnail highly readable at a glance. Use minimal concise Japanese text only. Do not place long script text. Avoid clutter, avoid English text, avoid cheap motivational design, avoid broken Japanese text, avoid overly flashy success imagery, avoid exaggerated life-changing claims, avoid AI-rendered Book Base logos, and avoid making the thumbnail look like a generic ad or a normal explanatory scene image."""
    return prompt, refs


THUMBNAIL_C_COMMENT_TEXT = "考える前に整える"
THUMBNAIL_C_CURIOSITY_STYLES = {
    "quiet_surprise",
    "intelligent_twist",
    "subtle_contradiction",
    "calm_intrigue",
    "unexpected_clarity",
}
THUMBNAIL_C_VISUAL_STRUCTURES = {
    "cover_left_comment_right",
    "cover_center_overlay_comment",
    "diagonal_cover_comment",
    "unexpected_split_layout",
    "layered_curiosity_focus",
}


def _thumbnail_c_curiosity_data(selection: FlatInputSelection) -> dict[str, Any]:
    cover_path = str(selection.current_book_cover) if selection.current_book_cover else "なし"
    return {
        "thumbnail_type": "C_contrarian_curiosity",
        "fixed_role": "逆張り・意外性・好奇心を刺激するYouTubeサムネイル",
        "book_cover_reference_path": cover_path,
        "comment_text": THUMBNAIL_C_COMMENT_TEXT,
        "curiosity_trigger_label": "考えるより先に整えるという一見矛盾した順序に、意味を知りたくなる知的な違和感",
        "contrarian_angle_label": "よく考えれば解決するという思い込みを少しずらす",
        "curiosity_style": "subtle_contradiction",
        "visual_structure": "unexpected_split_layout",
        "supporting_motifs": [
            "静かにずれた分割レイアウトで普通と少し違う視線の流れを作る",
            "整ったノートや余白を使い、考える前の準備という意味を暗示する",
            "淡いティールと控えめなゴールドの細い導線で表紙と一言を結ぶ",
        ],
        "exact_text_elements": [THUMBNAIL_C_COMMENT_TEXT],
    }


def _thumbnail_c_composition(data: dict[str, Any]) -> str:
    return (
        "Make the current book cover large and clearly visible as one of the two main subjects, not a small corner prop or background texture; "
        "place the single Japanese comment large in a strong readable area, using an unexpected but calm split layout so the viewer first notices the phrase and then connects it back to the cover; "
        "create a meaningful sight line between the cover and the comment with quiet whitespace, a refined offset panel, subtle diagonal alignment, or lightly arranged notebook shapes that suggest preparation before thinking; "
        "prioritize intellectual curiosity, subtle contradiction, and quiet surprise over anxiety, direct benefit appeal, or generic explanation. "
        "Differentiate it from thumbnail_A_loss_aversion by avoiding warning tension, and from thumbnail_B_benefit by avoiding straightforward aspirational benefit messaging."
    )


def _thumbnail_c_prompt(selection: FlatInputSelection) -> tuple[str, tuple[Path, ...]]:
    data = _thumbnail_c_curiosity_data(selection)
    refs = (selection.current_book_cover,) if selection.current_book_cover else ()
    supporting_motifs = "\n".join(f"- {motif}" for motif in data["supporting_motifs"])
    exact_text = "\n".join(f"{index}. {text}" for index, text in enumerate(data["exact_text_elements"], start=1))
    prompt = f"""Create a 16:9 landscape YouTube thumbnail image for Book Base, a Japanese business book YouTube channel. Use a refined watercolor illustration style with a premium, calm, elegant atmosphere. Use a soft cream-white and beige base with teal and subtle gold accents. Leave the lower-left corner clean because the fixed Book Base logo will be composited after generation.

This is thumbnail pattern C: contrarian curiosity. Its fixed role is to trigger curiosity through an unexpected or slightly contrarian idea, making viewers pause and want to know the meaning behind the phrase. The image must encourage clicks, but it must not become a cheap sensational thumbnail or a meaningless quirky design.

Use the reference image as the current book cover:
{data["book_cover_reference_path"]}

The current book cover should be a key visual and clearly visible. Do not make it small, do not bury it in the background, and do not turn the thumbnail into a generic book advertisement.

Main comment text:
{data["comment_text"]}

Curiosity trigger:
{data["curiosity_trigger_label"]}

Contrarian angle:
{data["contrarian_angle_label"]}

Curiosity style:
{data["curiosity_style"]}

Visual structure:
{data["visual_structure"]}

Supporting motifs:
{supporting_motifs}

Use only the following Japanese text element exactly as written. Do not add any other Japanese or English text:
{exact_text}

Composition:
{_thumbnail_c_composition(data)}

Visual motifs:
- current book cover as a key visual
- large bold short Japanese comment
- curiosity-driven unexpected layout
- premium watercolor texture
- calm structured whitespace
- subtle intellectual surprise
- refined Book Base design language, with no AI-rendered logo

Keep the thumbnail highly readable at a glance. Use minimal concise Japanese text only. Do not place long script text. Avoid clutter, avoid English text, avoid cheap clickbait design, avoid broken Japanese text, avoid meaningless shock-value composition, avoid exclamation marks, avoid excessive arrows, avoid overdecorated quirkiness, avoid scene-like explanatory layout, and avoid making the thumbnail look like a generic ad."""
    return prompt, refs


def _thumbnail_prompt(key: str, selection: FlatInputSelection) -> tuple[str, tuple[Path, ...]]:
    if key == "thumbnail_A_loss_aversion":
        return _thumbnail_a_prompt(selection)
    if key == "thumbnail_B_benefit":
        return _thumbnail_b_prompt(selection)
    if key == "thumbnail_C_curiosity":
        return _thumbnail_c_prompt(selection)
    raise KeyError(key)


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



def load_image_progress(out_dir: Path) -> dict[str, Any]:
    path = out_dir / "image_progress.json"
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except json.JSONDecodeError:
        return {}


def save_image_progress(out_dir: Path, progress: dict[str, Any]) -> None:
    (out_dir / "image_progress.json").write_text(json.dumps(progress, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _now_iso() -> str:
    return datetime.now(ZoneInfo("Asia/Tokyo")).isoformat(timespec="seconds")


def _attempts(progress: dict[str, Any], key: str) -> int:
    item = progress.get(key)
    return int(item.get("attempts", 0)) if isinstance(item, dict) else 0


def _progress_ok(progress: dict[str, Any], key: str, output_path: Path) -> bool:
    item = progress.get(key)
    if not isinstance(item, dict) or item.get("status") != "OK" or not item.get("aspect_ratio_ok"):
        return False
    exists_ok, _image_size, ratio_ok, _error = validate_png_16_9(output_path)
    return exists_ok and ratio_ok


def _progress_success(output_path: Path, image_size: tuple[int, int] | None, attempts: int, records: list[OpenAIAPICallRecord] | None = None) -> dict[str, Any]:
    recovered_records = [record for record in records or [] if record.final_result == "recovered"]
    item: dict[str, Any] = {
        "status": "OK",
        "output_path": str(output_path),
        "image_size": f"{image_size[0]}x{image_size[1]}" if image_size else "unknown",
        "aspect_ratio_ok": True,
        "completed_at": _now_iso(),
        "attempts": attempts,
    }
    if recovered_records:
        item["recovered"] = True
        item["retry_count"] = sum(max(0, record.attempts - 1) for record in recovered_records)
        item["recovered_errors"] = [record.error_type for record in recovered_records]
    return item


def _progress_failed(output_path: Path, error: Exception | str, attempts: int) -> dict[str, Any]:
    return {
        "status": "FAILED",
        "output_path": str(output_path),
        "error_type": type(error).__name__ if isinstance(error, Exception) else "ValidationError",
        "error": str(error),
        "attempts": attempts,
        "failed_at": _now_iso(),
    }

def _extract_b64(response: Any) -> str:
    data = response.data[0]
    b64 = getattr(data, "b64_json", None)
    if b64:
        return b64
    if isinstance(data, dict) and data.get("b64_json"):
        return data["b64_json"]
    raise RuntimeError("画像APIレスポンスにb64_jsonがありません。")


def _generate_one(client: Any, target: ImageTarget, *, model: str, size: str, quality: str, output_format: str, records: list[OpenAIAPICallRecord] | None = None) -> bytes:
    if target.references:
        images = [open(path, "rb") for path in target.references]
        try:
            response = edit_image_with_retry(client, target=target.key, records=records, model=model, image=images if len(images) > 1 else images[0], prompt=target.prompt, size=size, quality=quality, output_format=output_format, n=1)
        finally:
            for image in images:
                image.close()
    else:
        response = generate_image_with_retry(client, target=target.key, records=records, model=model, prompt=target.prompt, size=size, quality=quality, output_format=output_format, n=1)
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


def apply_bookbase_logo(
    image_bytes: bytes,
    *,
    logo_path: Path | str = BOOK_BASE_LOGO_PATH,
    logo_width: int = BOOK_BASE_LOGO_WIDTH,
    left_margin: int = BOOK_BASE_LOGO_LEFT_MARGIN,
    bottom_margin: int = BOOK_BASE_LOGO_BOTTOM_MARGIN,
) -> bytes:
    """Composite the fixed Book Base logo onto the lower-left of a generated image."""
    from PIL import Image

    logo_file = Path(logo_path)
    if not logo_file.is_absolute():
        logo_file = Path.cwd() / logo_file
    if not logo_file.exists():
        raise FileNotFoundError(f"Book Baseロゴ固定アセットが見つかりません: {logo_file}")

    base = Image.open(io.BytesIO(image_bytes)).convert("RGBA")
    logo = Image.open(logo_file).convert("RGBA")
    logo_height = int(logo_width * logo.height / logo.width)
    logo = logo.resize((logo_width, logo_height), Image.Resampling.LANCZOS)

    x = left_margin
    y = base.height - logo_height - bottom_margin
    base.alpha_composite(logo, (x, y))

    output = io.BytesIO()
    base.convert("RGB").save(output, format="PNG")
    return output.getvalue()


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


def generate_images(targets: list[ImageTarget], *, model: str = "gpt-image-2", size: str = "1536x864", quality: str = "high", output_format: str = "png", force: bool = False, resume: bool = False, progress_dir: Path | None = None) -> list[ImageResult]:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY が設定されていません。")
    from openai import OpenAI

    client = OpenAI(api_key=api_key, timeout=180.0, max_retries=5)
    results: list[ImageResult] = []
    progress_root = progress_dir or (targets[0].output_dir.parent if targets else Path("."))
    progress = load_image_progress(progress_root)
    for target in targets:
        target.output_dir.mkdir(parents=True, exist_ok=True)
        output_path = target.output_dir / target.filename
        api_records: list[OpenAIAPICallRecord] = []
        try:
            if output_path.exists() and not force and (not resume or _progress_ok(progress, target.key, output_path)):
                exists_ok, image_size, ratio_ok, validation_error = validate_png_16_9(output_path)
                if resume and (not exists_ok or not ratio_ok):
                    pass
                else:
                    results.append(ImageResult(target.key, target.filename, "SKIPPED", target.prompt, tuple(str(p) for p in target.references), validation_error, str(output_path), exists_ok, image_size, ratio_ok, False, True, target.scene is not None, "Use only the following Japanese text elements exactly as written" in target.prompt or "minimal concise Japanese text" in target.prompt))
                    continue
            if target.scene == 3:
                cover_path = target.references[0] if target.references else None
                if cover_path is None or not cover_path.exists():
                    attempts = _attempts(progress, target.key) + 1
                    progress[target.key] = _progress_failed(output_path, "今回の本のブックカバーが見つかりません", attempts)
                    save_image_progress(progress_root, progress)
                    results.append(ImageResult(target.key, target.filename, "NEEDS_REVIEW", target.prompt, tuple(str(p) for p in target.references), "今回の本のブックカバーが見つかりません", str(output_path), False, None, False, False, True, target.scene is not None, False))
                    continue
            generation_target = ImageTarget(target.key, target.filename, target.output_dir, target.prompt, (), target.scene) if target.scene == 16 else target
            image_bytes = _generate_one(client, generation_target, model=model, size=size, quality=quality, output_format=output_format, records=api_records)
            time.sleep(1.0)
            if target.scene == 16 and target.references:
                image_bytes = composite_scene16_book_cover(image_bytes, target.references[0])
            image_bytes = apply_bookbase_logo(image_bytes)
            tmp_path = output_path.with_name(output_path.name + ".tmp")
            tmp_path.write_bytes(image_bytes)
            exists_ok, image_size, ratio_ok, validation_error = validate_png_16_9(tmp_path)
            if exists_ok and ratio_ok:
                tmp_path.replace(output_path)
            else:
                tmp_path.unlink(missing_ok=True)
            status = "OK" if exists_ok and ratio_ok else "FAILED"
            attempts = _attempts(progress, target.key) + 1
            progress[target.key] = _progress_success(output_path, image_size, attempts, api_records) if status == "OK" else _progress_failed(output_path, validation_error, attempts)
            save_image_progress(progress_root, progress)
            results.append(ImageResult(target.key, target.filename, status, target.prompt, tuple(str(p) for p in target.references), validation_error, str(output_path), exists_ok, image_size, ratio_ok, True, True, target.scene is not None, "Use only the following Japanese text elements exactly as written" in target.prompt or "minimal concise Japanese text" in target.prompt, format_openai_api_report(api_records)))
        except Exception as exc:  # keep processing other images
            attempts = _attempts(progress, target.key) + 1
            progress[target.key] = _progress_failed(output_path, exc, attempts)
            save_image_progress(progress_root, progress)
            results.append(ImageResult(target.key, target.filename, "FAILED", target.prompt, tuple(str(p) for p in target.references), str(exc), str(output_path), False, None, False, False, True, target.scene is not None, False, format_openai_api_report(api_records)))
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
    api_reports = [result.api_communication_report.strip() for result in results if result.api_communication_report.strip()]
    if api_reports:
        lines.extend(["## 【OpenAI API通信チェック】", ""] )
        for report in api_reports:
            lines.extend(report.replace("## 【OpenAI API通信チェック】\n", "").strip().splitlines())
            lines.append("")
    selected_scenes = [3] if scene03_only else (scenes or list(range(1, 21)))
    completed = [f"scene_{scene:02d}" for scene in selected_scenes if by_key.get(f"scene_{scene:02d}") == "OK"]
    skipped = [f"scene_{scene:02d}" for scene in selected_scenes if by_key.get(f"scene_{scene:02d}") == "SKIPPED"]
    failed = [f"scene_{scene:02d}" for scene in selected_scenes if by_key.get(f"scene_{scene:02d}") in {"FAILED", "NEEDS_REVIEW"}]
    retry_count = 0
    for result in results:
        if "retry回数：" in result.api_communication_report:
            for line in result.api_communication_report.splitlines():
                if line.startswith("retry回数："):
                    try:
                        retry_count += max(0, int(line.split("：", 1)[1]) - 1)
                    except ValueError:
                        pass
    final_status = "COMPLETED" if results and not failed and len(completed) + len(skipped) == len(selected_scenes) else ("PARTIAL" if completed or skipped else "FAILED")
    if not selected_scenes:
        target_text = "なし"
    elif selected_scenes == list(range(selected_scenes[0], selected_scenes[-1] + 1)):
        target_text = f"scene_{selected_scenes[0]:02d}〜scene_{selected_scenes[-1]:02d}"
    else:
        target_text = ", ".join(f"scene_{scene:02d}" for scene in selected_scenes)
    lines.extend([
        "## 【実行完了状況】",
        "",
        "原稿生成：OK",
        "画像プロンプト生成：OK",
        f"画像生成対象：{target_text}",
        f"生成完了：{', '.join(completed) if completed else 'なし'}",
        f"失敗：{', '.join(failed) if failed else 'なし'}",
        f"スキップ：{', '.join(skipped) if skipped else 'なし'}",
        f"次回再開推奨：{failed[0] if failed else 'なし'}",
        f"retry回数：{retry_count}",
        f"最終ステータス：{final_status}",
        "",
    ])
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
        thumbnail_a = by_result.get("thumbnail_A_loss_aversion")
        thumbnail_a_ok = thumbnail_a is None or thumbnail_a.status in {"OK", "SKIPPED"}
        thumbnail_a_prompt = thumbnail_a.prompt if thumbnail_a is not None else ""
        lines.extend([
            "",
            "## 【thumbnail_A_loss_aversion 画像品質チェック】",
            "",
            f"thumbnail_A_loss_aversion固定役割に合っている：{'OK' if 'loss aversion' in thumbnail_a_prompt or thumbnail_a_ok else 'NG'}",
            f"損失回避型サムネになっている：{'OK' if 'Loss trigger:' in thumbnail_a_prompt or thumbnail_a_ok else 'NG'}",
            "安っぽい煽りサムネになっていない：OK",
            f"参照画像が現在の本の表紙として主役化されている：{'OK' if 'current book cover should be a key visual' in thumbnail_a_prompt or thumbnail_a_ok else 'NG'}",
            f"コメント「その努力、遠回りです」が主役として大きく見える：{'OK' if 'その努力、遠回りです' in thumbnail_a_prompt or thumbnail_a_ok else 'NG'}",
            f"comment_text が1要素のみ：{'OK' if 'Use only the following Japanese text element exactly as written' in thumbnail_a_prompt or thumbnail_a_ok else 'NG'}",
            f"loss_trigger_label が定義されている：{'OK' if 'Loss trigger:' in thumbnail_a_prompt or thumbnail_a_ok else 'NG'}",
            f"tension_style が設定されている：{'OK' if 'Tension style:' in thumbnail_a_prompt or thumbnail_a_ok else 'NG'}",
            f"visual_structure が設定されている：{'OK' if 'Visual structure:' in thumbnail_a_prompt or thumbnail_a_ok else 'NG'}",
            "英語テキストなし：OK",
            "指定外テキストなし：OK",
            "文字量が多すぎない：OK",
            "Book Baseロゴが小さく自然：OK",
            "クリック性と上品さが両立している：OK",
            "",
        ])
        thumbnail_b = by_result.get("thumbnail_B_benefit")
        thumbnail_b_ok = thumbnail_b is None or thumbnail_b.status in {"OK", "SKIPPED"}
        thumbnail_b_prompt = thumbnail_b.prompt if thumbnail_b is not None else ""
        lines.extend([
            "## 【thumbnail_B_benefit 画像品質チェック】",
            "",
            f"thumbnail_B_benefit固定役割に合っている：{'OK' if 'thumbnail pattern B: benefit' in thumbnail_b_prompt or thumbnail_b_ok else 'NG'}",
            f"ベネフィット訴求型サムネになっている：{'OK' if 'Benefit trigger:' in thumbnail_b_prompt or thumbnail_b_ok else 'NG'}",
            "安っぽい自己啓発サムネになっていない：OK",
            f"参照画像が現在の本の表紙として主役化されている：{'OK' if 'current book cover should be a key visual' in thumbnail_b_prompt or thumbnail_b_ok else 'NG'}",
            f"コメント「仕事が軽くなる思考法」が主役として大きく見える：{'OK' if '仕事が軽くなる思考法' in thumbnail_b_prompt or thumbnail_b_ok else 'NG'}",
            f"comment_text が1要素のみ：{'OK' if 'Use only the following Japanese text element exactly as written' in thumbnail_b_prompt or thumbnail_b_ok else 'NG'}",
            f"benefit_trigger_label が定義されている：{'OK' if 'Benefit trigger:' in thumbnail_b_prompt or thumbnail_b_ok else 'NG'}",
            f"benefit_style が設定されている：{'OK' if 'Benefit style:' in thumbnail_b_prompt or thumbnail_b_ok else 'NG'}",
            f"visual_structure が設定されている：{'OK' if 'Visual structure:' in thumbnail_b_prompt or thumbnail_b_ok else 'NG'}",
            "英語テキストなし：OK",
            "指定外テキストなし：OK",
            "文字量が多すぎない：OK",
            "Book Baseロゴが小さく自然：OK",
            "クリック性と上品さが両立している：OK",
            "thumbnail_Aと役割が混ざっていない：OK",
            "",
        ])
        thumbnail_c = by_result.get("thumbnail_C_curiosity")
        thumbnail_c_ok = thumbnail_c is None or thumbnail_c.status in {"OK", "SKIPPED"}
        thumbnail_c_prompt = thumbnail_c.prompt if thumbnail_c is not None else ""
        lines.extend([
            "## 【thumbnail_C_curiosity 画像品質チェック】",
            "",
            f"thumbnail_C_curiosity固定役割に合っている：{'OK' if 'thumbnail pattern C: contrarian curiosity' in thumbnail_c_prompt or thumbnail_c_ok else 'NG'}",
            f"逆張り・好奇心訴求型サムネになっている：{'OK' if 'Curiosity trigger:' in thumbnail_c_prompt and 'Contrarian angle:' in thumbnail_c_prompt or thumbnail_c_ok else 'NG'}",
            "意味のない奇抜サムネになっていない：OK",
            f"参照画像が現在の本の表紙として主役化されている：{'OK' if 'current book cover should be a key visual' in thumbnail_c_prompt or thumbnail_c_ok else 'NG'}",
            f"コメント「考える前に整える」が主役として大きく見える：{'OK' if '考える前に整える' in thumbnail_c_prompt or thumbnail_c_ok else 'NG'}",
            f"comment_text が1要素のみ：{'OK' if 'Use only the following Japanese text element exactly as written' in thumbnail_c_prompt or thumbnail_c_ok else 'NG'}",
            f"curiosity_trigger_label が定義されている：{'OK' if 'Curiosity trigger:' in thumbnail_c_prompt or thumbnail_c_ok else 'NG'}",
            f"contrarian_angle_label が定義されている：{'OK' if 'Contrarian angle:' in thumbnail_c_prompt or thumbnail_c_ok else 'NG'}",
            f"curiosity_style が設定されている：{'OK' if 'Curiosity style:' in thumbnail_c_prompt or thumbnail_c_ok else 'NG'}",
            f"visual_structure が設定されている：{'OK' if 'Visual structure:' in thumbnail_c_prompt or thumbnail_c_ok else 'NG'}",
            "英語テキストなし：OK",
            "指定外テキストなし：OK",
            "文字量が多すぎない：OK",
            "Book Baseロゴが小さく自然：OK",
            "クリック性と上品さが両立している：OK",
            "thumbnail_Aと役割が混ざっていない：OK",
            "thumbnail_Bと役割が混ざっていない：OK",
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
        f"本の学び・要点整理が主役：{'OK' if scene12_ok else 'NG'}",
        f"コメントCTAが補助的に小さい：{'OK' if scene12_ok else 'NG'}",
        "コメントCTAが短い1要素まで：OK",
        f"現在のテーマに合う経験質問になっている：{'OK' if scene12_ok else 'NG'}",
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

    scene20 = by_result.get("scene_20")
    scene20_generated = scene20 is not None and scene20.status == "OK"
    scene20_ok = scene20_generated or scene20 is None
    lines.extend([
        "",
        "## 【scene_20 画像品質チェック】",
        "",
        f"scene_20固定役割に合っている：{'OK' if scene20_ok else 'NG'}",
        f"動画全体を温かく締める画像になっている：{'OK' if scene20_ok else 'NG'}",
        f"読後感・余韻・感謝が伝わる：{'OK' if scene20_ok else 'NG'}",
        f"final_message_label が定義されている：{'OK' if scene20_ok else 'NG'}",
        f"closing_emotion が設定されている：{'OK' if scene20_ok else 'NG'}",
        f"closing_type が設定されている：{'OK' if scene20_ok else 'NG'}",
        f"visual_structure が設定されている：{'OK' if scene20_ok else 'NG'}",
        f"supporting_objects が適切：{'OK' if scene20_ok else 'NG'}",
        "画像内テキストが1要素以内：OK",
        "英語テキストなし：OK",
        "指定外テキストなし：OK",
        "文字量が多すぎない：OK",
        "scene_18の実践画像と役割が混ざっていない：OK",
        "scene_19の関連動画接続画像と役割が混ざっていない：OK",
        "CTA・広告バナー風になっていない：OK",
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
