from __future__ import annotations

import json
import os
import re
from pathlib import Path
from dataclasses import dataclass
from typing import Any

from .assets import AssetCheck, asset_checks_by_scene
from .quality import SCENE_MAX_CHARS, SCENE_MIN_CHARS, TOTAL_MAX_CHARS, TOTAL_MIN_CHARS, count_scene_body_chars


class AIResponseJSONParseError(ValueError):
    """Raised when the OpenAI response cannot be parsed as one JSON object."""


class AIResponseValidationError(ValueError):
    """Raised when the OpenAI response JSON has an unexpected shape."""


_COMMON_STYLE_FOR_SCHEMA = "16:9 landscape, watercolor illustration, premium calm atmosphere, Japanese business book YouTube channel, cream white, beige, teal, subtle gold palette, clean composition, enough whitespace, small natural Book Base logo, minimal concise Japanese text only, one clear message, do not place long script text, vary composition from adjacent scenes"

TEXT_LOCK_INSTRUCTION = "Use only the following Japanese text elements exactly as written. Do not add any other Japanese or English text."

SCENE_04_COMPOSITION = "左側に著者参考画像があれば上品な水彩イラスト、なければシルエットや本の象徴モチーフを置き、右側に3つの小さなポイントカードを縦に並べる。カード同士は細いゴールドの線でゆるくつなぎ、scene_03の本中心構図とは変える。"


def _asset_path(asset_checks: list[AssetCheck] | None, key: str) -> str | None:
    for check in asset_checks or []:
        if check.key == key and check.path:
            return check.path
    return None


def _scene_body(script: str, scene: int) -> str:
    match = re.search(rf"【シーン{scene}】\n(?P<body>.*?)(?=\n\n【シーン\d+】\n|\Z)", script, flags=re.S)
    return " ".join(match.group("body").split()) if match else ""


def _short_label(text: str, fallback: str, limit: int = 14) -> str:
    clean = re.sub(r"[『』「」\s]", "", text).strip("。,.、")
    if not clean:
        return fallback
    return clean[:limit]


def build_image_context(script: str, book_title: str, asset_checks: list[AssetCheck] | None = None) -> dict[str, object]:
    scene1 = _scene_body(script, 1)
    scene2 = _scene_body(script, 2)
    scene3 = _scene_body(script, 3)
    scene4 = _scene_body(script, 4)
    scene5 = _scene_body(script, 5)
    scene6 = _scene_body(script, 6)
    scene7 = _scene_body(script, 7)
    options = {letter: _short_label(value, f"選択肢{letter}", 18) for letter, value in re.findall(r"([ABC])\.\s*([^ABC。]+)", scene1)}
    correct = (re.search(r"正解は\s*([ABC])", scene2) or re.search(r"正解は([ABC])", scene2))
    point_matches = re.findall(r"[①②③](.*?)(?:、|。|です|$)", scene4)
    labels = [_short_label(m, f"ポイント{i}", 12) for i, m in enumerate(point_matches[:3], 1)]
    while len(labels) < 3:
        defaults = ["問題を見える化", "背景を捉える", "小さく実践"]
        labels.append(defaults[len(labels)])
    p1 = _short_label(re.sub(r"^重要ポイントの1つ目は", "", scene5), labels[0], 16)
    author_match = re.search(r"今回紹介するのは、(.+?)さんの『", scene3) or re.search(r"著者の(.+?)さん", scene4)
    author = author_match.group(1) if author_match else "著者"
    theme = _short_label(scene2 or scene3, "現在の動画テーマ", 18)
    context = {
        "book_title": book_title,
        "author_name": author,
        "current_theme": theme,
        "quiz": {
            "question": _short_label(scene1.split("A.")[0], "現在の本に合わせた短い問い", 36),
            "correct_answer": correct.group(1) if correct else "B",
            "answer_label": _short_label(scene2, "正解の短い説明", 18),
            "option_a": options.get("A", "選択肢A"),
            "option_b": options.get("B", "選択肢B"),
            "option_c": options.get("C", "選択肢C"),
        },
        "three_key_points": [
            {"index": 1, "label": labels[0], "core_message": _short_label(scene5, labels[0], 30)},
            {"index": 2, "label": labels[1], "core_message": labels[1]},
            {"index": 3, "label": labels[2], "core_message": labels[2]},
        ],
        "scene_bodies": {"scene_05": scene5, "scene_06": scene6, "scene_07": scene7},
        "assets": {
            "book_cover": _asset_path(asset_checks, "scene_03_current_book_cover"),
            "author_reference": _asset_path(asset_checks, "scene_04_author_reference"),
        },
    }
    return context


def _text_block(elements: list[str]) -> str:
    return "\n".join(f"{i}. {element}" for i, element in enumerate(elements, 1))


def _scene_01_structured_prompt(context: dict[str, object]) -> dict[str, object]:
    quiz = context["quiz"]
    elements = [str(quiz["question"]), f"A. {quiz['option_a']}", f"B. {quiz['option_b']}", f"C. {quiz['option_c']}"]
    final_prompt = f"Create a video-insert image. Style: {_COMMON_STYLE_FOR_SCHEMA}. This is Scene 01: opening question. Its fixed role is to present a quiz based on statistics, news, survey data, or research-like framing and make viewers think. Do not reveal the answer. Use A/B/C options. {TEXT_LOCK_INSTRUCTION}:\n{_text_block(elements)}\nComposition: office worker thinking, simple chart or survey sheet, clean quiz card, enough whitespace. Avoid showing a correct answer or theme-specific fixed wording."
    return {"scene": 1, "scene_role": "オープニングの統計・ニュース・調査データ風クイズ", "core_message": str(quiz["question"]), "exact_text_elements": elements, "composition": "考える会社員＋調査風クイズカード", "visual_motifs": ["会社員", "クイズカード", "簡易グラフ", "調査用紙"], "style": _COMMON_STYLE_FOR_SCHEMA, "negative_rules": ["答えを出さない", "長文を入れない", "今回テーマ固有語句を固定しない"], "variation_key": "opening-statistics-quiz", "final_prompt": final_prompt}


def _scene_02_structured_prompt(context: dict[str, object]) -> dict[str, object]:
    quiz = context["quiz"]
    elements = [f"正解は{quiz['correct_answer']}", str(quiz["answer_label"]), str(context["current_theme"])]
    final_prompt = f"Create a video-insert image. Style: {_COMMON_STYLE_FOR_SCHEMA}. This is Scene 02: reveal the answer to Scene 01 and bridge naturally into the video theme. Keep it calm, not a flashy quiz show. {TEXT_LOCK_INSTRUCTION}:\n{_text_block(elements)}\nComposition: answer card separated from a small theme-bridge card, calm office worker, subtle light. Avoid repeating Scene 01 composition."
    return {"scene": 2, "scene_role": "クイズ正解発表とテーマへの橋渡し", "core_message": str(quiz["answer_label"]), "exact_text_elements": elements, "composition": "答えカード＋テーマ接続カード", "visual_motifs": ["答えカード", "会社員", "テーマカード", "淡い光"], "style": _COMMON_STYLE_FOR_SCHEMA, "negative_rules": ["派手なクイズ番組風にしない", "長文を入れない", "今回テーマ固有語句を固定しない"], "variation_key": "calm-answer-theme-bridge", "final_prompt": final_prompt}


def _scene_03_structured_prompt(context: dict[str, object]) -> dict[str, object]:
    cover = context["assets"]["book_cover"]
    elements = ["今回の一冊", str(context["three_key_points"][0]["core_message"])]
    final_prompt = f"Create a video-insert background image. Style: {_COMMON_STYLE_FOR_SCHEMA}. This is Scene 03: introduce the current book and briefly show the video's value. The actual book cover will be composited later from the provided reference image. Use the real current book cover path during compositing: {cover or 'none'}. Do not draw or recreate the book cover. Leave prominent clean space for the real cover. {TEXT_LOCK_INSTRUCTION}:\n{_text_block(elements)}\nComposition: premium desk, cover placeholder, short value message, notebook and pen."
    return {"scene": 3, "scene_role": "今回の本紹介と動画全体の結論提示", "reference_image_required": True, "reference_image_path": cover, "core_message": elements[1], "exact_text_elements": elements, "composition": "実ブックカバー用余白＋短い価値メッセージ", "visual_motifs": ["実ブックカバー", "デスク", "ノート", "ペン"], "style": _COMMON_STYLE_FOR_SCHEMA, "negative_rules": ["ブックカバーをAIに再生成させない", "固定パスを使わない", "長文を入れない"], "post_process": {"composite_real_book_cover": True, "preserve_aspect_ratio": True, "cover_width_ratio": "0.25-0.38", "add_shadow": True, "add_light_border": True}, "variation_key": "real-cover-book-introduction", "final_prompt": final_prompt}


def _scene_04_structured_prompt(context: dict[str, object]) -> dict[str, object]:
    author_ref = context["assets"]["author_reference"]
    points = context["three_key_points"]
    elements = ["著者紹介", "3つの重要ポイント", f"①{points[0]['label']}", f"②{points[1]['label']}", f"③{points[2]['label']}"]
    ref = "Use the author reference only to make a refined watercolor illustration; do not paste the photo." if author_ref else "No author reference is available; do not imagine a face. Use a silhouette or book motif."
    final_prompt = f"Create a video-insert image. Style: {_COMMON_STYLE_FOR_SCHEMA}. This is Scene 04: introduce the author and show a roadmap of three key points. {ref} {TEXT_LOCK_INSTRUCTION}:\n{_text_block(elements)}\nComposition: {SCENE_04_COMPOSITION}"
    return {"scene": 4, "scene_role": "著者紹介と3つの重要ポイント提示", "reference_image_required": False, "reference_image_path": author_ref, "reference_image_usage": "著者参考画像がある場合のみ水彩画風イラスト生成に使う。なければ顔を想像しない。", "core_message": "3つの重要ポイント", "exact_text_elements": elements, "composition": SCENE_04_COMPOSITION, "visual_motifs": ["著者イラストまたはシルエット", "3つのポイントカード", "本", "細い接続線"], "style": _COMMON_STYLE_FOR_SCHEMA, "negative_rules": ["著者写真をそのまま貼らない", "固定ポイント語句を使わない", "固定パスを使わない", "長文を入れない"], "variation_key": "author-and-three-point-roadmap", "final_prompt": final_prompt}


def _scene_05_structured_prompt(context: dict[str, object]) -> dict[str, object]:
    point = context["three_key_points"][0]
    elements = ["重要ポイント①", str(point["label"]), _short_label(str(point["core_message"]), str(point["label"]), 14)]
    metaphor = "a visual metaphor derived from Key Point 1, such as a clear first step, spotlight, doorway, map, or focused desk motif"
    final_prompt = f"Create a video-insert image. Style: {_COMMON_STYLE_FOR_SCHEMA}. This is Scene 05: begin Key Point 1 and make the first important message clear at a glance. One image, one message, different composition from Scene 04. Visual metaphor: {metaphor}. {TEXT_LOCK_INSTRUCTION}:\n{_text_block(elements)}\nAvoid fixed wording from any specific book; derive labels from image_context.json."
    return {"scene": 5, "scene_role": "重要ポイント①の導入", "core_message": str(point["core_message"]), "exact_text_elements": elements, "composition": "重要ポイント①にズームインする単一メッセージ構図", "visual_motifs": ["最初の一歩", "スポットライト", "カード", "余白"], "style": _COMMON_STYLE_FOR_SCHEMA, "negative_rules": ["scene_04と同じ構図にしない", "固定テーマ語句を使わない", "長文を入れない"], "variation_key": "key-point-1-introduction", "final_prompt": final_prompt}


def _select_scene_06_visual_structure(scene6_body: str) -> str:
    if re.search(r"前|後|変化|変わ|改善|すると|できると", scene6_body):
        return "before_after"
    if re.search(r"仕組み|構造|内側|心理|感情|判断|習慣|思考|前提", scene6_body):
        return "hidden_mechanism"
    if re.search(r"障壁|詰ま|妨げ|阻害|壁|解決|取り除", scene6_body):
        return "obstacle_and_solution"
    if re.search(r"一方|逆に|対比|違い|ではなく|より", scene6_body):
        return "contrast"
    return "cause_to_effect"


def _scene_06_composition(visual_structure: str) -> str:
    mapping = {
        "cause_to_effect": "左から右へ、理由・仕組み・結果が自然に流れる構図。3つの短いカードを細い線でつなぎ、scene_05の導入カード構図とは違う因果の流れを見せる。",
        "before_after": "左側に変化前、右側に変化後を置き、中央に背景や仕組みを示す小さな橋を配置する。scene_05のズームイン構図を繰り返さない。",
        "hidden_mechanism": "表面上の仕事場面の背後に、内側の仕組みを示す半透明カードや線を配置する。人物だけに頼らず、見えない構造を主役にする。",
        "obstacle_and_solution": "左に詰まりや障害、中央に背景の仕組み、右に開けた結果を置く。机や付箋だけの雰囲気画像にしない。",
        "contrast": "左側に一般的な見方、右側に本書が示す視点を並べる。中央に視点の切り替わりを示す余白を置く。",
    }
    return mapping.get(visual_structure, mapping["cause_to_effect"])


def _scene_06_structured_prompt(context: dict[str, object]) -> dict[str, object]:
    point = context["three_key_points"][0]
    scene_bodies = context.get("scene_bodies", {})
    scene6_body = str(scene_bodies.get("scene_06", "")) if isinstance(scene_bodies, dict) else ""
    point_1_label = str(point["label"])
    core_message = _short_label(scene6_body or str(point["core_message"]), point_1_label, 28)
    reason_label = _short_label(re.split(r"。|、", scene6_body)[0] if scene6_body else core_message, "理由", 12)
    mechanism_source = re.search(r"(仕組み|構造|背景|前提|感情|事実|原因|材料|視点).{0,12}", scene6_body)
    mechanism_label = _short_label(mechanism_source.group(0) if mechanism_source else core_message, "仕組み", 12)
    effect_source = re.search(r"(進め|見え|変わ|減|強ま|選び|続け|つなが).{0,12}", scene6_body)
    effect_label = _short_label(effect_source.group(0) if effect_source else str(point["core_message"]), "影響", 12)
    elements = []
    for label in [reason_label, mechanism_label, effect_label]:
        if label and label not in elements:
            elements.append(label[:15])
    elements = elements[:3]
    while len(elements) < 3:
        fallback = ["理由", "仕組み", "影響"][len(elements)]
        if fallback not in elements:
            elements.append(fallback)
    visual_structure = _select_scene_06_visual_structure(scene6_body)
    visual_metaphor = "current-script-derived mechanism diagram: layered cards, subtle connecting lines, and a visual metaphor matching Key Point 1 without using any previous-book topic words"
    composition = _scene_06_composition(visual_structure)
    motifs = ["理由カード", "仕組みカード", "結果カード", "細い接続線", "半透明レイヤー"]
    final_prompt = f"""Create a 16:9 landscape video-insert image for Book Base, a Japanese business book YouTube channel. Use a refined watercolor illustration style with a premium, calm, elegant atmosphere. Use a soft cream-white and beige background with teal and subtle gold accents. Include a small natural Book Base logo placed unobtrusively.

This is Scene 06. Its fixed role is to explain the reason, background, or mechanism behind Key Point 1. The image should visually clarify why the first key point matters, based on the current script. Do not create a generic business person image. Do not hard-code any topic from a previous book. Build the visual message from the current script only.

Current Key Point 1:
{point_1_label}

Current Scene 06 core message:
{core_message}

{TEXT_LOCK_INSTRUCTION}:
{_text_block(elements)}

Visual structure:
{visual_structure}

Visual metaphor:
{visual_metaphor}

Composition:
{composition}

Visual motifs:
{', '.join(motifs)}

Keep the image clean and easy to understand at a glance. Use minimal text only. Do not place long script text. Avoid clutter, avoid generic emotional icons, avoid a generic desk-only scene, avoid over-explaining, and avoid repeating the Scene 05 composition."""
    return {"scene": 6, "fixed_role": "重要ポイント①の理由・背景・仕組み説明", "scene_role": "重要ポイント①の理由・背景・仕組み説明", "point_1_label": point_1_label, "core_message": core_message, "scene_06_core_message": core_message, "reason_label": elements[0], "mechanism_label": elements[1], "effect_label": elements[2], "visual_metaphor": visual_metaphor, "visual_structure": visual_structure, "exact_text_elements": elements, "composition": composition, "visual_motifs": motifs, "style": _COMMON_STYLE_FOR_SCHEMA, "negative_rules": ["特定の本の語句を固定しない", "過去テーマの語句を使い回さない", "generic emotional iconsを使わない", "ただのビジネス人物イラストにしない", "scene_05と同じ構図にしない", "文字を増やしすぎない"], "variation_key": f"scene-06-{visual_structure}-key-point-1-mechanism", "final_prompt": final_prompt}


def _scene_07_evidence_type(scene7_body: str) -> str:
    if re.search(r"論文|研究|実験|検証", scene7_body):
        return "research"
    if re.search(r"アンケート|調査|利用者|読者", scene7_body):
        return "survey"
    if re.search(r"公的|官公庁|統計|白書|政府|省庁", scene7_body):
        return "public_data"
    if re.search(r"レポート|業界|市場|企業", scene7_body):
        return "report"
    if re.search(r"実例|事例|実績|成果|ケース", scene7_body):
        return "case_data"
    return "book_claim"


def _scene_07_source_confidence(scene7_body: str, evidence_type: str) -> str:
    if not scene7_body.strip():
        return "unavailable"
    if evidence_type == "book_claim":
        return "needs_review"
    if re.search(r"確認|出典|データ|調査|研究|論文|統計|白書|公的|実績|報告", scene7_body):
        return "verified"
    return "needs_review"


def _scene_07_visual_structure(evidence_type: str) -> str:
    mapping = {
        "research": "research_board",
        "survey": "data_report",
        "public_data": "document_review",
        "report": "data_report",
        "experiment": "research_board",
        "case_data": "evidence_card",
        "book_claim": "evidence_card",
    }
    return mapping.get(evidence_type, "evidence_card")


def _scene_07_composition(visual_structure: str) -> str:
    mapping = {
        "evidence_card": "中央に大きなエビデンスカードを置き、周囲に資料・小さな抽象グラフ・付箋を余白多めに配置する。人物は小さくし、scene_06の因果図解と被らせない。",
        "data_report": "左側にレポート資料と抽象化したグラフ、右側に重要ポイント①の短い結論カードを置き、根拠から結論へ視線が流れる構図にする。",
        "research_board": "ホワイトボード風の資料ボードに短い根拠ラベルと簡単な図だけを置き、研究室風に寄せすぎず上品なビジネス資料として見せる。",
        "document_review": "落ち着いた机上で公的資料風のドキュメントカードを確認する構図。数字や機関名は作らず、根拠ラベルだけを強調する。",
        "chart_focus": "中央に抽象化された小さなチャートと根拠カードを重ね、詳細数字ではなく裏付けの存在を示す。scene_06の原因結果線は使わない。",
    }
    return mapping.get(visual_structure, mapping["evidence_card"])


def _scene_07_evidence_label(evidence_type: str, source_confidence: str) -> str:
    if source_confidence != "verified":
        return "参考データ" if source_confidence == "needs_review" else "根拠確認中"
    return {
        "research": "研究データ",
        "survey": "調査結果",
        "public_data": "公的データ",
        "report": "調査レポート",
        "experiment": "実験結果",
        "case_data": "実例データ",
        "book_claim": "本書の視点",
    }.get(evidence_type, "根拠データ")


def _scene_07_structured_prompt(context: dict[str, object]) -> dict[str, object]:
    point = context["three_key_points"][0]
    scene_bodies = context.get("scene_bodies", {})
    scene7_body = str(scene_bodies.get("scene_07", "")) if isinstance(scene_bodies, dict) else ""
    point_1_label = str(point["label"])
    core_message = _short_label(scene7_body or str(point["core_message"]), f"{point_1_label}の根拠", 30)
    evidence_type = _scene_07_evidence_type(scene7_body)
    source_confidence = _scene_07_source_confidence(scene7_body, evidence_type)
    evidence_label = _scene_07_evidence_label(evidence_type, source_confidence)
    conclusion_fallback = "根拠で確認" if source_confidence == "verified" else "データで見る"
    key_finding_label = _short_label(re.split(r"。|、", scene7_body)[-2] if "。" in scene7_body else core_message, conclusion_fallback, 12)
    elements = [evidence_label[:15], point_1_label[:15], key_finding_label[:15]]
    visual_structure = _scene_07_visual_structure(evidence_type)
    composition = _scene_07_composition(visual_structure)
    final_prompt = f"""Create a 16:9 landscape video-insert image for Book Base, a Japanese business book YouTube channel. Use a refined watercolor illustration style with a premium, calm, elegant atmosphere. Use a soft cream-white and beige background with teal and subtle gold accents. Include a small natural Book Base logo placed unobtrusively.

This is Scene 07. Its fixed role is to reinforce Key Point 1 with evidence, such as research, survey results, public data, reports, experiments, or documented examples. The evidence type must be based on the current script and current research data. Do not hard-code psychology research or any topic from a previous book. Do not invent specific numbers, sources, or study names.

Current Key Point 1:
{point_1_label}

Current Scene 07 core message:
{core_message}

Evidence type:
{evidence_type}

Source confidence:
{source_confidence}

{TEXT_LOCK_INSTRUCTION}:
{_text_block(elements)}

Visual structure:
{visual_structure}

Composition:
{composition}

Visual motifs:
elegant evidence card, report documents, simple abstract charts, calm business desk, subtle data icons, enough whitespace, premium watercolor texture

Keep the image clean and easy to understand at a glance. Use minimal text only. Do not place long script text. Avoid clutter, avoid fake detailed charts, avoid invented statistics, avoid hard-coded psychology research, and avoid repeating the Scene 06 composition."""
    return {"scene": 7, "fixed_role": "重要ポイント①の根拠補強", "scene_role": "重要ポイント①の根拠補強", "point_1_label": point_1_label, "core_message": core_message, "scene_07_core_message": core_message, "evidence_type": evidence_type, "evidence_label": elements[0], "key_finding_label": elements[2], "source_confidence": source_confidence, "visual_structure": visual_structure, "exact_text_elements": elements, "composition": composition, "visual_motifs": ["エビデンスカード", "資料", "抽象グラフ", "データアイコン", "余白"], "style": _COMMON_STYLE_FOR_SCHEMA, "negative_rules": ["心理学研究を固定しない", "架空の数字を作らない", "出典不明の研究名を入れない", "証明と断定しない", "scene_06と同じ構図にしない"], "variation_key": f"scene-07-{visual_structure}-{evidence_type}-evidence", "final_prompt": final_prompt}


@dataclass(frozen=True)
class GeneratedAssets:
    script: str
    titles: str
    description: str
    thumbnail_ideas: str
    thumbnail_comments: str
    metadata: str
    image_prompts: str
    image_context: str
    research_scene_11: str
    research_scene_15: str


def render_script_from_scenes(scenes: Any) -> str:
    if not isinstance(scenes, list):
        raise ValueError(f"Unexpected scenes type: {type(scenes).__name__}")
    if len(scenes) != 20:
        raise ValueError(f"scenesは必ず20件です: {len(scenes)}件")
    rendered_parts: list[str] = []
    for expected_number, scene in enumerate(scenes, start=1):
        if not isinstance(scene, dict):
            raise ValueError(f"Unexpected scene item type: {type(scene).__name__}")
        scene_number = scene.get("scene_number") or scene.get("scene") or scene.get("シーン番号")
        body = scene.get("body") or scene.get("text") or scene.get("content")
        if scene_number != expected_number:
            raise ValueError(f"シーン番号が順番通りではありません: expected={expected_number}, actual={scene_number}")
        if not isinstance(body, str) or not body.strip():
            raise ValueError(f"シーン{expected_number}の本文が空です")
        clean_body = " ".join(body.strip().splitlines())
        rendered_parts.append(f"【シーン{scene_number}】\n{clean_body}")
    return "\n\n".join(rendered_parts) + "\n"


def validate_bookbase_script(script: str) -> list[str]:
    matches = list(re.finditer(r"^【シーン(?P<number>\d+)】$", script, flags=re.MULTILINE))
    errors: list[str] = []
    if len(matches) != 20:
        errors.append(f"シーン数：{len(matches)}個。20個ではありません")
    numbers = [int(match.group("number")) for match in matches]
    if numbers != list(range(1, 21)):
        errors.append(f"シーン番号：{numbers}。1〜20の順番ではありません")
    if re.search(r"^【シーン\d+】\S", script, flags=re.MULTILINE):
        errors.append("見出しと本文が同じ行になっています")
    if matches and not all(f"\n\n【シーン{index}】\n" in script for index in range(2, 21)):
        errors.append("シーン間改行なし")
    total = 0
    bullet_pattern = re.compile(r"(^|\n)\s*(?:[-*・]|\d+[.)．、])\s+")
    for index, match in enumerate(matches):
        number = int(match.group("number"))
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(script)
        body = script[start:end].strip()
        if "\n" in body:
            errors.append(f"シーン{number}：本文内に不要な改行があります")
        if bullet_pattern.search(body):
            errors.append(f"シーン{number}：箇条書きがあります")
        count = count_scene_body_chars(body)
        total += count
        if count < SCENE_MIN_CHARS:
            errors.append(f"シーン{number}：{count}字。{SCENE_MIN_CHARS}字未満")
        elif count > SCENE_MAX_CHARS:
            errors.append(f"シーン{number}：{count}字。{SCENE_MAX_CHARS}字超過")
    if total < TOTAL_MIN_CHARS or total > TOTAL_MAX_CHARS:
        errors.append(f"全体文字数：{total}字。{TOTAL_MIN_CHARS}〜{TOTAL_MAX_CHARS}字の範囲外")
    return errors


def _markdown_scalar(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def _markdown_from_value(value: Any, *, heading_level: int = 2) -> str:
    if isinstance(value, str):
        return value.rstrip()
    if isinstance(value, list):
        lines: list[str] = []
        for item in value:
            if isinstance(item, str):
                lines.append(item)
            elif isinstance(item, dict):
                if set(item) <= {"scene", "scene_number", "シーン番号", "text", "body", "content"}:
                    scene = item.get("scene") or item.get("scene_number") or item.get("シーン番号")
                    body = item.get("text") or item.get("body") or item.get("content") or ""
                    prefix = f"【シーン{scene}】\n" if scene else ""
                    lines.append(prefix + _markdown_scalar(body))
                else:
                    lines.extend(f"- {key}: {_markdown_scalar(item[key])}" for key in item)
            else:
                lines.append(_markdown_scalar(item))
        return "\n".join(lines).rstrip()
    if isinstance(value, dict):
        preferred_body_keys = ("markdown", "text", "body", "content", "script")
        if "scenes" in value:
            return render_script_from_scenes(value["scenes"]).rstrip()
        for key in preferred_body_keys:
            body = value.get(key)
            if isinstance(body, str) and body.strip():
                return body.rstrip()
            if isinstance(body, (list, dict)):
                return _markdown_from_value(body, heading_level=heading_level).rstrip()
        lines: list[str] = []
        marker = "#" * heading_level
        for key, item in value.items():
            if isinstance(item, (dict, list)):
                rendered = _markdown_from_value(item, heading_level=heading_level + 1).rstrip()
                lines.extend([f"{marker} {key}", "", rendered, ""])
            else:
                lines.append(f"- {key}: {_markdown_scalar(item)}")
        return "\n".join(lines).rstrip()
    return _markdown_scalar(value).rstrip()


def _ensure_markdown_text(value: Any, field_name: str) -> str:
    if not isinstance(value, (str, dict, list)):
        raise ValueError(f"Unexpected {field_name} type: {type(value).__name__}")
    rendered = _markdown_from_value(value).rstrip()
    if not rendered:
        raise ValueError(f"Unexpected {field_name} value: empty")
    return rendered + "\n"


def render_titles(titles: Any) -> str:
    if isinstance(titles, str):
        return titles.rstrip() + "\n"
    if isinstance(titles, dict):
        pattern_a = titles.get("pattern_a") or titles.get("A") or ""
        pattern_b = titles.get("pattern_b") or titles.get("B") or ""
        pattern_c = titles.get("pattern_c") or titles.get("C") or ""
        return (
            "## タイトル案\n\n"
            "Pattern A：脅し・損失回避型\n"
            f"{pattern_a}\n\n"
            "Pattern B：誘惑・ベネフィット型\n"
            f"{pattern_b}\n\n"
            "Pattern C：逆張り・好奇心型\n"
            f"{pattern_c}\n"
        )
    raise ValueError(f"Unexpected titles type: {type(titles).__name__}")


def render_schedule(schedule: Any) -> str:
    expected_times = ["0:00", "2:00", "4:00", "6:00", "8:00"]
    expected_prefixes = ["本日のテーマ：", "ポイント①：", "ポイント②：", "ポイント③：", "まとめ："]

    if isinstance(schedule, str):
        raw_lines = [line.strip() for line in schedule.splitlines() if line.strip()]
        if len(raw_lines) != 5:
            raise ValueError("タイムスケジュールは必ず5行である必要があります")
        lines = raw_lines
    elif isinstance(schedule, list):
        if len(schedule) != 5:
            raise ValueError("タイムスケジュールは必ず5行である必要があります")
        lines = []
        for index, (expected_time, item) in enumerate(zip(expected_times, schedule)):
            if isinstance(item, str):
                topic = item.strip()
                for candidate_time in expected_times:
                    topic = re.sub(rf"^{re.escape(candidate_time)}\s+", "", topic).strip()
            elif isinstance(item, dict):
                topic = str(
                    item.get("topic")
                    or item.get("title")
                    or item.get("content")
                    or item.get("description")
                    or ""
                ).strip()
            else:
                raise ValueError(f"Unexpected schedule item type: {type(item).__name__}")
            if not topic:
                topic = expected_prefixes[index] + "〇〇〇〇"
            lines.append(f"{expected_time} {topic}")
    elif isinstance(schedule, dict):
        lines = []
        for index, expected_time in enumerate(expected_times):
            value = schedule.get(expected_time) or schedule.get(str(index)) or schedule.get(str(index + 1)) or ""
            topic = str(value).strip() or expected_prefixes[index] + "〇〇〇〇"
            lines.append(f"{expected_time} {topic}")
    else:
        raise ValueError(f"Unexpected schedule type: {type(schedule).__name__}")
    return "## タイムスケジュール\n\n" + "\n".join(lines) + "\n"


def render_description(description: Any) -> str:
    if isinstance(description, str):
        return description.rstrip() + "\n"
    if isinstance(description, dict):
        text = description.get("text") or description.get("description") or description.get("body") or ""
        count = description.get("文字数") or description.get("count") or len(text)
        return f"## 50文字説明\n\n{text}\n文字数：{count}文字\n"
    raise ValueError(f"Unexpected description type: {type(description).__name__}")


def render_comment(comment: Any) -> str:
    if isinstance(comment, str):
        lines = [line.strip() for line in comment.splitlines() if line.strip()]
    elif isinstance(comment, list):
        if not all(isinstance(item, str) for item in comment):
            raise ValueError("Unexpected comment item type: non-string")
        lines = [item.strip() for item in comment if item.strip()]
    elif isinstance(comment, dict):
        lines = [str(value).strip() for value in comment.values() if str(value).strip()]
    else:
        raise ValueError(f"Unexpected comment type: {type(comment).__name__}")
    if len(lines) != 3:
        raise ValueError("コメントは必ず3行である必要があります")
    lines[2] = "もし似たような経験があれば、ぜひコメント欄で教えてください。"
    return "## コメント\n\n" + "\n".join(lines) + "\n"


def render_image_prompts(image_prompts: Any) -> str:
    if isinstance(image_prompts, str):
        return image_prompts.rstrip() + "\n"
    if isinstance(image_prompts, (list, dict)):
        return json.dumps(image_prompts, ensure_ascii=False, indent=2) + "\n"
    raise ValueError(f"Unexpected image_prompts type: {type(image_prompts).__name__}")


def render_metadata(data: dict[str, Any]) -> str:
    metadata = data.get("metadata")
    if isinstance(metadata, str) and metadata.strip():
        return metadata.rstrip() + "\n"
    if metadata is not None and not isinstance(metadata, dict):
        raise ValueError(f"Unexpected metadata type: {type(metadata).__name__}")
    source = {**data, **metadata} if isinstance(metadata, dict) else data
    parts = ["# 投稿補助情報", "", render_titles(source.get("titles", data.get("titles"))).rstrip()]
    if "schedule" in source:
        parts.extend(["", render_schedule(source["schedule"]).rstrip()])
    if "description" in source:
        parts.extend(["", render_description(source["description"]).rstrip()])
    if "comment" in source:
        parts.extend(["", render_comment(source["comment"]).rstrip()])
    return "\n".join(parts).rstrip() + "\n"


def _write_ai_json_validation_error_report(error_dir: Path | None, message: str, data: Any) -> None:
    if error_dir is None:
        return
    error_dir.mkdir(parents=True, exist_ok=True)
    (error_dir / "error_report.md").write_text(
        "\n".join([
            "エラー種別：AI応答JSON型検証失敗",
            f"原因：{message}",
            "発生箇所：generator.py / generate_ai_assets / render_*",
            "対応：AI出力JSON schemaとPython側のMarkdown整形処理の型を確認してください。",
            "",
        ]),
        encoding="utf-8",
    )
    (error_dir / "parsed_ai_response.json").write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def _split_summary(source_text: str, scene_count: int = 20) -> list[str]:
    compact = " ".join(source_text.split())
    if not compact:
        return ["入力本文の要点を追記してください。"] * scene_count
    chunk_size = max(1, len(compact) // scene_count)
    chunks = [compact[i : i + chunk_size] for i in range(0, len(compact), chunk_size)]
    if len(chunks) < scene_count:
        chunks.extend([chunks[-1]] * (scene_count - len(chunks)))
    return chunks[:scene_count]





def _description_50(book_name: str) -> str:
    base = f"{book_name}の要点を仕事の判断に活かし、迷いを減らして明日から行動できる学びを解説します。"
    if len(base) < 50:
        base = f"{book_name}の要点を仕事の判断に活かし、会社員が迷いを減らして明日から行動できる実践的な学びを解説します。"
    while len(base) < 50:
        base += "。"
    return base[:60]


def _build_metadata(book_name: str) -> str:
    description = _description_50(book_name)
    return "\n".join(
        [
            "# 投稿補助情報",
            "",
            "## タイトル案",
            "",
            "Pattern A：脅し・損失回避型",
            f"【角が立つ一言に注意】{book_name}で直すNG表現7選【信頼を削る前に】",
            "",
            "Pattern B：誘惑・ベネフィット型",
            f"【会議の返しがやわらぐ】{book_name}の言い換え10例【評価される伝え方へ】",
            "",
            "Pattern C：逆張り・好奇心型",
            f"【正論ほど嫌われる？】{book_name}が教える否定しない話し方【まず受け止める技術】",
            "",
            "## タイムスケジュール",
            "",
            "0:00 本日のテーマ：仕事の迷いを減らす本の学び",
            "2:00 ポイント①：まず問題を見える化する",
            "4:00 ポイント②：原因と背景を構造で捉える",
            "6:00 ポイント③：小さな行動に落とし込む",
            "8:00 まとめ：学びを明日の仕事へつなげる",
            "",
            "## 50文字説明",
            "",
            description,
            f"文字数：{len(description)}文字",
            "",
            "## コメント",
            "",
            "今回は、仕事の迷いを減らす考え方について紹介しました。",
            "頑張っているのに、なぜか行動が前に進まないと感じた経験はありますか？",
            "もし似たような経験があれば、ぜひコメント欄で教えてください。",
        ]
    ) + "\n"

def _thumbnail_cover_check(asset_checks: list[AssetCheck] | None) -> AssetCheck | None:
    for check in asset_checks or []:
        if check.key == "scene_03_current_book_cover":
            return check
    return None


def _build_thumbnail_comments(book_name: str, cover_check: AssetCheck | None = None) -> str:
    cover_path = cover_check.path if cover_check and cover_check.path else "なし"
    needs_review = bool(cover_check and cover_check.status == "MISSING")
    lines = [
        "# thumbnail_comments.md",
        "",
        "Pattern A：",
        "方向性：脅し・損失回避型",
        "コメント：その努力、遠回りです",
        f"狙い：{book_name}の要点を、会社員が今のやり方を見直したくなる損失回避の切り口に変換する。",
        "出力ファイル名：thumbnail_A_loss_aversion.png",
        f"使用画像：{cover_path}",
        f"needs_review：{needs_review}",
        "",
        "Pattern B：",
        "方向性：誘惑・ベネフィット型",
        "コメント：仕事が軽くなる思考法",
        f"狙い：{book_name}から得られる前向きな変化を、仕事改善のベネフィットとして伝える。",
        "出力ファイル名：thumbnail_B_benefit.png",
        f"使用画像：{cover_path}",
        f"needs_review：{needs_review}",
        "",
        "Pattern C：",
        "方向性：逆張り・好奇心型",
        "コメント：考える前に整える",
        f"狙い：{book_name}の主張を、普通の努力論とは違う意外性のある入口に変換する。",
        "出力ファイル名：thumbnail_C_curiosity.png",
        f"使用画像：{cover_path}",
        f"needs_review：{needs_review}",
    ]
    if needs_review:
        lines.extend([
            "",
            "注意：scene_03_current_book_cover が見つからないため、サムネイル生成はneeds_reviewです。架空のブックカバーは作らないでください。",
        ])
    return "\n".join(lines) + "\n"


def _build_thumbnail_ideas(book_name: str, cover_check: AssetCheck | None = None) -> str:
    cover_path = cover_check.path if cover_check and cover_check.path else "なし"
    needs_review = bool(cover_check and cover_check.status == "MISSING")
    shared = (
        "16:9 watercolor premium Japanese business book YouTube thumbnail, "
        "large short original Japanese comment, visible book cover, small natural Book Base logo, "
        "cream white beige teal gold palette, intellectual calm atmosphere, smartphone-readable text"
    )
    patterns = [
        ("Pattern A", "thumbnail_A_loss_aversion.png", "脅し・損失回避型", "その努力、遠回りです", "left large comment, right visible book cover, tense but elegant office desk background"),
        ("Pattern B", "thumbnail_B_benefit.png", "誘惑・ベネフィット型", "仕事が軽くなる思考法", "center large comment, side book cover, bright morning desk and notebook background"),
        ("Pattern C", "thumbnail_C_curiosity.png", "逆張り・好奇心型", "考える前に整える", "upper large comment, lower corner book cover, curiosity-driven tidy notes and soft contrast"),
    ]
    lines = ["# サムネイル生成プロンプト", "", f"使用ブックカバー：{cover_path}", f"needs_review：{needs_review}", ""]
    for label, filename, direction, comment, layout in patterns:
        lines.extend([
            f"## {label}：{direction}",
            f"出力ファイル名：{filename}",
            f"コメント：{comment}",
            f"使用画像：{cover_path}",
            f"最終プロンプト：{shared}, pattern {label}, direction {direction}, comment text '{comment}', {layout}",
            "",
        ])
    if needs_review:
        lines.append("注意：ブックカバーがないため、架空の表紙や無関係な本画像を作らず、サムネイル生成はneeds_reviewにしてください。")
    return "\n".join(lines).rstrip() + "\n"


def _build_research_scene_11(*, verified: bool = False) -> str:
    status = "OK" if verified else "NEEDS_REVIEW"
    return "\n".join(
        [
            "# scene_11 実話エピソード人物",
            "",
            "人物名：未確定" if not verified else "人物名：AI生成結果を確認してください",
            "人物の概要：重要ポイント②を補強できる実在人物を、原稿生成後に選定します。",
            "使用する実話エピソード：事実確認できる実話のみ使用します。",
            "重要ポイント②とのつながり：原因・背景・構造理解を補強するエピソードに限定します。",
            "確認した出典：未取得。出典確認後にOKへ更新してください。",
            "画像生成時の表現方針：人物画像未取得の場合は、顔を想像で描かず、人物シルエットまたは行動場面で代替します。",
            f"自動取得ステータス：{status}",
        ]
    ) + "\n"


def _build_research_scene_15(*, verified: bool = False) -> str:
    status = "OK" if verified else "NEEDS_REVIEW"
    return "\n".join(
        [
            "# scene_15 名言人物",
            "",
            "名言：未確定" if not verified else "名言：AI生成結果を確認してください",
            "発言者：未確定" if not verified else "発言者：AI生成結果を確認してください",
            "発言者の概要：重要ポイント③の実践・行動化を補強できる人物を、原稿生成後に選定します。",
            "名言の意味：行動へ移しやすい短い言葉として扱います。",
            "重要ポイント③とのつながり：実践・応用・行動化を後押しする名言に限定します。",
            "確認した出典：未取得。誤引用の可能性を確認後にOKへ更新してください。",
            "画像生成時の表現方針：人物画像未取得の場合は、顔を想像で描かず、名言カードまたは静物構図で代替します。",
            f"自動取得ステータス：{status}",
        ]
    ) + "\n"

def _image_block_metadata(scene: int) -> dict[str, str]:
    if 1 <= scene <= 4:
        block = "シーン1〜4：冒頭導入・クイズ・本紹介・重要ポイント提示"
        role_map = {1: "問い・問題提起", 2: "結論・本の紹介", 3: "全体像の提示", 4: "重要ポイントへの橋渡し"}
        return {
            "所属ブロック": block,
            "ブロックの役割": "視聴者に問題意識を持たせ、動画を見る理由と本から学べる価値を示す",
            "重要ポイント番号": "該当なし",
            "ブロック内での役割": role_map[scene],
            "前ブロックからの理解の流れ": "動画冒頭として、悩みから本の価値と全体像へ導く",
        }
    if 5 <= scene <= 8:
        role_map = {5: "重要ポイント1の導入", 6: "重要ポイント1の説明・理由", 7: "重要ポイント1の根拠補強", 8: "重要ポイント1の締め＋登録促し"}
        return {
            "所属ブロック": "シーン5〜8：重要ポイント1",
            "ブロックの役割": "前提・土台・最初の気づきを理解させる",
            "重要ポイント番号": "重要ポイント1",
            "ブロック内での役割": role_map[scene],
            "前ブロックからの理解の流れ": "導入で提示した問題意識を、まず押さえるべき土台の理解へ進める",
        }
    if 9 <= scene <= 12:
        role_map = {9: "重要ポイント2の導入", 10: "重要ポイント2の理由・構造", 11: "重要ポイント2の具体例・比較", 12: "重要ポイント2の締め＋コメント促し"}
        return {
            "所属ブロック": "シーン9〜12：重要ポイント2",
            "ブロックの役割": "重要ポイント1の土台をもとに、理由・構造・比較で理解を深める",
            "重要ポイント番号": "重要ポイント2",
            "ブロック内での役割": role_map[scene],
            "前ブロックからの理解の流れ": "土台理解から一段深く、なぜそうなるのかが見える状態へ進める",
        }
    if 13 <= scene <= 16:
        role_map = {13: "重要ポイント3の導入", 14: "重要ポイント3の実践・応用", 15: "重要ポイント3の整理・行動化", 16: "重要ポイント3の締め"}
        return {
            "所属ブロック": "シーン13〜16：重要ポイント3",
            "ブロックの役割": "重要ポイント1・2を踏まえて、実践・応用・行動化へ落とし込む",
            "重要ポイント番号": "重要ポイント3",
            "ブロック内での役割": role_map[scene],
            "前ブロックからの理解の流れ": "構造理解から、自分の仕事や日常で何をするかへ進める",
        }
    role_map = {17: "動画内容のおさらい", 18: "学びの実践化・余韻", 19: "関連動画接続", 20: "まとめ・着地"}
    return {
        "所属ブロック": "シーン17〜20：おさらい・実践・関連動画接続・締め",
        "ブロックの役割": "おさらい、実践、関連動画接続、最終メッセージで前向きな余韻を残す",
        "重要ポイント番号": "該当なし",
        "ブロック内での役割": role_map[scene],
        "前ブロックからの理解の流れ": "実践への落とし込みを受け、本全体の意味と次の行動へつなげる",
    }


def _build_image_prompt_item(scene: int, context: dict[str, object] | None = None, asset_check: AssetCheck | None = None) -> dict[str, object]:
    if context is None:
        context = build_image_context("", "現在の本", [])
    scene_01_prompt = _scene_01_structured_prompt(context) if scene == 1 else None
    scene_02_prompt = _scene_02_structured_prompt(context) if scene == 2 else None
    scene_03_prompt = _scene_03_structured_prompt(context) if scene == 3 else None
    scene_04_prompt = _scene_04_structured_prompt(context) if scene == 4 else None
    scene_05_prompt = _scene_05_structured_prompt(context) if scene == 5 else None
    scene_06_prompt = _scene_06_structured_prompt(context) if scene == 6 else None
    scene_07_prompt = _scene_07_structured_prompt(context) if scene == 7 else None
    meta = _image_block_metadata(scene)
    composition_by_point = {
        "重要ポイント1": "仕事机、ノート、タスク、時計を使い、土台・入口・最初の気づきが伝わる構図",
        "重要ポイント2": "比較、構造、原因と結果、Before/Afterが見える図解的な構図。ただし文字量は少なくする",
        "重要ポイント3": "整理されたデスク、チェックリスト、予定表、朝の光で実践・応用・行動化を示す構図",
        "該当なし": "ブロックの役割に合わせ、導入または締めとして余白のある落ち着いた構図",
    }
    point = str(meta["重要ポイント番号"])
    purpose = "1画像1メッセージで、シーンの役割を直感的に伝える"
    text = "短いキーワードのみ" if scene not in {1, 20} else "必要なら短い見出し、長文なし"
    differentiation = "前後シーンと人物位置、視点、背景、主モチーフ、文字配置を変える"
    used_image = asset_check.path if asset_check and asset_check.path else "なし"
    asset_note = asset_check.note if asset_check else "このシーンに必須入力画像はありません。"
    if scene == 11 and asset_check is None:
        asset_note = "scene_11の人物は原稿生成後に人物名と実話エピソードを確定し、出典確認できる場合のみ水彩画風イラストに反映します。人物画像未取得の場合は顔を想像で描かず、シルエットまたは行動場面で代替します。"
    elif scene == 15 and asset_check is None:
        asset_note = "scene_15の名言人物は原稿生成後に発言者・原文・文脈を確認し、誤引用リスクが低い場合のみ水彩画風イラストに反映します。人物画像未取得の場合は顔を想像で描かず、名言カードまたは静物構図で代替します。"
    if scene_01_prompt:
        purpose = str(scene_01_prompt["scene_role"])
        text = " / ".join(scene_01_prompt["exact_text_elements"])
        differentiation = str(scene_01_prompt["variation_key"])
        prompt = str(scene_01_prompt["final_prompt"])
        recommended_composition = str(scene_01_prompt["composition"])
    elif scene_02_prompt:
        purpose = str(scene_02_prompt["scene_role"])
        text = " / ".join(scene_02_prompt["exact_text_elements"])
        differentiation = str(scene_02_prompt["variation_key"])
        prompt = str(scene_02_prompt["final_prompt"])
        recommended_composition = str(scene_02_prompt["composition"])
    elif scene_03_prompt:
        purpose = str(scene_03_prompt["scene_role"])
        text = " / ".join(scene_03_prompt["exact_text_elements"])
        differentiation = "scene_02の人物・答えカード中心から、本そのものを主役にした左カバー・右メッセージ型へ変える"
        prompt = str(scene_03_prompt["final_prompt"])
        recommended_composition = str(scene_03_prompt["composition"])
        asset_note = "実ブックカバーを後処理で合成します。AIには背景のみ生成させ、架空の表紙を作らせません。" if used_image != "なし" else "scene_03：NEEDS_REVIEW。理由：今回の本のブックカバーが見つかりません。架空の表紙は作らないでください。"
    elif scene_04_prompt:
        purpose = str(scene_04_prompt["scene_role"])
        text = " / ".join(scene_04_prompt["exact_text_elements"])
        differentiation = "scene_03のブックカバー中心構図から、著者イラスト＋3ポイントカードの見取り図へ変える"
        prompt = str(scene_04_prompt["final_prompt"])
        recommended_composition = str(scene_04_prompt["composition"])
    elif scene_05_prompt:
        purpose = str(scene_05_prompt["scene_role"])
        text = " / ".join(scene_05_prompt["exact_text_elements"])
        differentiation = "scene_04の著者＋3ポイント構図から、重要ポイント①の導入メッセージへズームインする"
        prompt = str(scene_05_prompt["final_prompt"])
        recommended_composition = str(scene_05_prompt["composition"])
    elif scene_06_prompt:
        purpose = str(scene_06_prompt["scene_role"])
        text = " / ".join(scene_06_prompt["exact_text_elements"])
        differentiation = "scene_05の重要ポイント①導入から、理由・背景・仕組みが見える図解構図へ変える"
        prompt = str(scene_06_prompt["final_prompt"])
        recommended_composition = str(scene_06_prompt["composition"])
    elif scene_07_prompt:
        purpose = str(scene_07_prompt["scene_role"])
        text = " / ".join(scene_07_prompt["exact_text_elements"])
        differentiation = "scene_06の理由・仕組み図解から、根拠資料・エビデンスカード中心の裏付け構図へ変える"
        prompt = str(scene_07_prompt["final_prompt"])
        recommended_composition = str(scene_07_prompt["composition"])
    else:
        recommended_composition = composition_by_point[point]
        prompt = (
            "16:9 watercolor illustration for a premium Japanese business book YouTube channel, "
            "soft cream white beige teal and gold palette, small natural Book Base logo in the upper-right or lower-right, "
            f"scene {scene}, {meta['所属ブロック']}, {meta['ブロック内での役割']}, "
            f"{recommended_composition}, no long text, one clear message, avoid repeating adjacent composition"
        )
    return {
        "シーン番号": scene,
        "所属ブロック": meta["所属ブロック"],
        "ブロックの役割": meta["ブロックの役割"],
        "重要ポイント番号": meta["重要ポイント番号"],
        "ブロック内での役割": meta["ブロック内での役割"],
        "前ブロックからの理解の流れ": meta["前ブロックからの理解の流れ"],
        "このシーンで伝える要点": "現在のシーン原稿から最も重要な要点を1つだけ抽出する",
        "画像の目的": purpose,
        "推奨構図": recommended_composition,
        "画面内テキスト": text,
        "前後画像との差別化": differentiation,
        "使用画像": used_image,
        "入力画像チェック": asset_note,
        "needs_review": bool((scene == 3 and used_image == "なし") or (asset_check and asset_check.status == "MISSING" and scene in {19}) or scene in {11, 15}),
        "最終プロンプト": prompt + (f", reference image: {used_image}, asset note: {asset_note}" if scene not in {2, 3, 4, 5, 6, 7} else ""),
        "scene": scene,
        "prompt": prompt,
        "scene_role": (scene_01_prompt or scene_02_prompt or scene_03_prompt or scene_04_prompt or scene_05_prompt or scene_06_prompt or scene_07_prompt)["scene_role"] if (scene_01_prompt or scene_02_prompt or scene_03_prompt or scene_04_prompt or scene_05_prompt or scene_06_prompt or scene_07_prompt) else meta["ブロック内での役割"],
        "core_message": (scene_01_prompt or scene_02_prompt or scene_03_prompt or scene_04_prompt or scene_05_prompt or scene_06_prompt or scene_07_prompt)["core_message"] if (scene_01_prompt or scene_02_prompt or scene_03_prompt or scene_04_prompt or scene_05_prompt or scene_06_prompt or scene_07_prompt) else "現在のシーン原稿から最も重要な要点を1つだけ抽出する",
        "exact_text_elements": (scene_01_prompt or scene_02_prompt or scene_03_prompt or scene_04_prompt or scene_05_prompt or scene_06_prompt or scene_07_prompt)["exact_text_elements"] if (scene_01_prompt or scene_02_prompt or scene_03_prompt or scene_04_prompt or scene_05_prompt or scene_06_prompt or scene_07_prompt) else [text],
        "composition": (scene_01_prompt or scene_02_prompt or scene_03_prompt or scene_04_prompt or scene_05_prompt or scene_06_prompt or scene_07_prompt)["composition"] if (scene_01_prompt or scene_02_prompt or scene_03_prompt or scene_04_prompt or scene_05_prompt or scene_06_prompt or scene_07_prompt) else recommended_composition,
        "visual_motifs": (scene_01_prompt or scene_02_prompt or scene_03_prompt or scene_04_prompt or scene_05_prompt or scene_06_prompt or scene_07_prompt)["visual_motifs"] if (scene_01_prompt or scene_02_prompt or scene_03_prompt or scene_04_prompt or scene_05_prompt or scene_06_prompt or scene_07_prompt) else [recommended_composition],
        "style": (scene_01_prompt or scene_02_prompt or scene_03_prompt or scene_04_prompt or scene_05_prompt or scene_06_prompt or scene_07_prompt)["style"] if (scene_01_prompt or scene_02_prompt or scene_03_prompt or scene_04_prompt or scene_05_prompt or scene_06_prompt or scene_07_prompt) else _COMMON_STYLE_FOR_SCHEMA,
        "negative_rules": (scene_01_prompt or scene_02_prompt or scene_03_prompt or scene_04_prompt or scene_05_prompt or scene_06_prompt or scene_07_prompt)["negative_rules"] if (scene_01_prompt or scene_02_prompt or scene_03_prompt or scene_04_prompt or scene_05_prompt or scene_06_prompt or scene_07_prompt) else ["長文を入れない", "指定外の文字を入れない", "前後シーンと同じ構図にしない"],
        "variation_key": (scene_01_prompt or scene_02_prompt or scene_03_prompt or scene_04_prompt or scene_05_prompt or scene_06_prompt or scene_07_prompt)["variation_key"] if (scene_01_prompt or scene_02_prompt or scene_03_prompt or scene_04_prompt or scene_05_prompt or scene_06_prompt or scene_07_prompt) else differentiation,
        "final_prompt": prompt,
        **({"reference_image_required": scene_03_prompt["reference_image_required"], "reference_image_path": scene_03_prompt["reference_image_path"], "post_process": scene_03_prompt["post_process"]} if scene_03_prompt else {}),
        **({"reference_image_required": scene_04_prompt["reference_image_required"], "reference_image_path": scene_04_prompt["reference_image_path"], "reference_image_usage": scene_04_prompt["reference_image_usage"]} if scene_04_prompt else {}),
        **({"fixed_role": scene_06_prompt["fixed_role"], "point_1_label": scene_06_prompt["point_1_label"], "scene_06_core_message": scene_06_prompt["scene_06_core_message"], "reason_label": scene_06_prompt["reason_label"], "mechanism_label": scene_06_prompt["mechanism_label"], "effect_label": scene_06_prompt["effect_label"], "visual_metaphor": scene_06_prompt["visual_metaphor"], "visual_structure": scene_06_prompt["visual_structure"]} if scene_06_prompt else {}),
        **({"fixed_role": scene_07_prompt["fixed_role"], "point_1_label": scene_07_prompt["point_1_label"], "scene_07_core_message": scene_07_prompt["scene_07_core_message"], "evidence_type": scene_07_prompt["evidence_type"], "evidence_label": scene_07_prompt["evidence_label"], "key_finding_label": scene_07_prompt["key_finding_label"], "source_confidence": scene_07_prompt["source_confidence"], "visual_structure": scene_07_prompt["visual_structure"]} if scene_07_prompt else {}),
    }

def _fit_scene(text: str, *, min_chars: int = 180, max_chars: int = 220) -> str:
    filler = "会社員の現実に置き換えると、評価や納期に追われる場面でも、論点を一つずつ整理して行動へ移す助けになります。"
    while len(text) < min_chars:
        text += filler
    return text[:max_chars]


def generate_fallback_assets(source_text: str, book_name: str, asset_checks: list[AssetCheck] | None = None) -> GeneratedAssets:
    chunks = _split_summary(source_text)
    assets_by_scene = asset_checks_by_scene(asset_checks or [])
    book_title = book_name.replace("_", " ")
    author = "著者"
    scene_leads = {
        1: "人材サービス会社が社会人に行った調査では、仕事の悩みは知識不足より整理不足から生まれることが多いとされています。では、忙しい会社員が最初に見直すべきものは何でしょうか。A.思考の整理 B.根性 C.残業時間。それでは正解を発表します。",
        2: "正解はAの思考の整理です。数字や調査結果を見ると、会社員の悩みは能力そのものより、情報をどう扱うかで大きく変わります。今回のテーマは、本の内容を仕事の判断に変える方法です。",
        3: f"今回紹介するのは、{author}さんの『{book_title}』こちらの本になります。本書の要点は、知識を増やすだけでなく、目の前の課題に使える形へ整えることです。会社員にとっては、迷いを減らし行動を早める武器になります。",
        4: "著者の経歴で注目したいのは、複雑なテーマを実生活に結びつけて語っている点です。今回の重要ポイントは3つあります。問題を見える化すること、背景を捉えること、最後に小さく実践へ移すことです。",
        5: "重要ポイントの1つ目は問題を見える化することです。仕事で迷う時ほど、原因は能力不足ではなく、考える材料が頭の中で混ざっていることにあります。まず何に困っているのかを言葉にすると、次の行動が見えます。",
        6: "問題を見える化すると、上司の評価、納期、会議の発言なども分けて考えられます。本書のメモでは、感情と事実を切り分ける視点が重要です。不安をそのまま抱えるより、事実を書き出す方が前に進めます。",
        7: "本書の説明や関連する調査資料では、悩みを言葉にして整理することで判断材料が見えやすくなるとされています。外部根拠は毎回確認し、確認が弱い場合は参考データとして扱います。",
        8: f"問題を整理できると、毎日の仕事で無駄に消耗しにくくなります。{ 'このチャンネルでは、話題の本を、日々の仕事や年収アップにどう活かせるかという視点でお届けしています。興味のある方は、ぜひチャンネル登録お願いします。' }",
        9: "重要ポイントの2つ目は原因や背景を捉えることです。目の前の失敗だけを見ると落ち込みますが、背景まで見ると対策が変わります。報連相が遅れたなら、性格ではなく仕組みや優先順位の問題かもしれません。",
        10: "背景を捉える人は、同じ失敗を繰り返しにくくなります。本書の内容も、表面の出来事に反応するのではなく、なぜそうなったのかを見に行く姿勢を重視しています。これは管理職にも若手にも役立つ視点です。",
        11: "実話エピソードとして、経営者が失敗の原因を個人の根性ではなく仕組みで見直す話は多く語られます。たとえば改善を続ける企業ほど、失敗を責めるより記録し、次の判断材料に変えます。",
        12: "背景を見直すと、自分を責めすぎず改善点を探せます。みなさんも仕事で、失敗の原因を後から整理して次に活かせた経験はありますか？もし似たような経験があれば、ぜひコメント欄で教えてください。",
        13: "重要ポイントの3つ目は小さく実践へ移すことです。学びは理解しただけでは変化になりません。会議前に論点を一つ書く、退勤前に明日の判断材料を整理するなど、小さな行動へ落とすことで意味が出ます。",
        14: "小さな実践は、忙しい会社員に向いています。大きな改革を狙うと続きませんが、毎日一つだけ判断を楽にする工夫なら続けやすいです。本書の価値は、読後に仕事の見方が少し変わる点にあります。",
        15: "名言として、ピーター・ドラッカーの言葉に、測定できないものは管理できないという考え方があります。行動も同じで、何を変えるかが見えていなければ続きません。本書の学びも、見える化して初めて実践できます。",
        16: "ここで紹介した以外にも、本書には考え方を整えるヒントが残っています。動画では扱いきれない具体例もあるので、自分の仕事に引き寄せて読むほど発見があります。もし気になった方は、ぜひ本書を手に取ってみてください。",
        17: "今回の内容をおさらいすると、まず問題を見える化し、次に原因や背景を捉え、最後に小さく実践する流れが大切でした。知識を増やすだけでなく、仕事の判断に使える形へ整えることが本書の価値です。",
        18: "明日から実践するなら、まず一つの悩みを紙に書き出してみてください。評価、納期、人間関係のどれが問題なのかを分けるだけでも、行動は選びやすくなります。日常の小さな整理が、判断の速さを変えます。",
        19: "この考え方は、過去動画で扱った習慣化や時間管理のテーマともつながります。考えを整理してから行動するほど、毎日の改善は続きやすくなります。気になる方は、ぜひそちらもあわせてご視聴ください。",
        20: "最後に、本は読むだけで終わらせるより、仕事の一場面に使って初めて力になります。今日の内容から一つだけ選び、明日の判断に活かしてみてください。参考になった方は、高評価やハイプで応援していただけると嬉しいです。それでは、また次回の動画でお会いしましょう。最後までご視聴ありがとうございました。",
    }
    scenes = []
    for index in range(1, 21):
        body = scene_leads[index]
        if index not in {1, 2, 3, 4, 8, 12, 16, 17, 19, 20}:
            body += f" 入力メモの要素として「{chunks[index - 1][:30]}」も踏まえます。"
        scenes.append(f"【シーン{index}】\n{_fit_scene(body)}")

    script = "\n\n".join(scenes) + "\n"
    titles = "\n".join(
        [
            f"# タイトル案：{book_name}",
            f"A. 【角が立つ一言に注意】{book_name}で直すNG表現7選【信頼を削る前に】",
            f"B. 【会議の返しがやわらぐ】{book_name}の言い換え10例【評価される伝え方へ】",
            f"C. 【正論ほど嫌われる？】{book_name}が教える否定しない話し方【まず受け止める技術】",
        ]
    ) + "\n"
    description = f"{book_name}の要点を仕事と日常で使える視点に絞り、明日から実践できる行動までわかりやすく丁寧に解説します。"
    cover_check = _thumbnail_cover_check(asset_checks)
    thumbnail_ideas = _build_thumbnail_ideas(book_name, cover_check)
    thumbnail_comments = _build_thumbnail_comments(book_name, cover_check)
    metadata = _build_metadata(book_name)
    image_context = build_image_context(script, book_title, asset_checks)
    prompts = [_build_image_prompt_item(index, image_context, assets_by_scene.get(index)) for index in range(1, 21)]
    image_prompts = json.dumps(prompts, ensure_ascii=False, indent=2) + "\n"
    return GeneratedAssets(
        script,
        titles,
        description + "\n",
        thumbnail_ideas,
        thumbnail_comments,
        metadata,
        image_prompts,
        json.dumps(image_context, ensure_ascii=False, indent=2) + "\n",
        _build_research_scene_11(),
        _build_research_scene_15(),
    )

def _asset_context_for_prompt(asset_checks: list[AssetCheck] | None) -> str:
    if not asset_checks:
        return "入力画像チェック対象はありません。"
    return "\n".join(f"{check.key}: {check.status} / 使用画像: {check.path or 'なし'} / 注意: {check.note}" for check in asset_checks)


def _bookbase_assets_json_schema() -> dict[str, object]:
    image_prompt_properties = {
        "シーン番号": {"type": "integer"},
        "所属ブロック": {"type": "string"},
        "ブロックの役割": {"type": "string"},
        "重要ポイント番号": {"type": "string"},
        "ブロック内での役割": {"type": "string"},
        "前ブロックからの理解の流れ": {"type": "string"},
        "このシーンで伝える要点": {"type": "string"},
        "画像の目的": {"type": "string"},
        "推奨構図": {"type": "string"},
        "画面内テキスト": {"type": "string"},
        "前後画像との差別化": {"type": "string"},
        "使用画像": {"type": "string"},
        "入力画像チェック": {"type": "string"},
        "needs_review": {"type": "boolean"},
        "最終プロンプト": {"type": "string"},
        "scene_role": {"type": "string"},
        "core_message": {"type": "string"},
        "exact_text_elements": {"type": "array", "items": {"type": "string"}},
        "composition": {"type": "string"},
        "visual_motifs": {"type": "array", "items": {"type": "string"}},
        "style": {"type": "string"},
        "negative_rules": {"type": "array", "items": {"type": "string"}},
        "variation_key": {"type": "string"},
        "final_prompt": {"type": "string"},
        "fixed_role": {"type": "string"},
        "point_1_label": {"type": "string"},
        "scene_06_core_message": {"type": "string"},
        "reason_label": {"type": "string"},
        "mechanism_label": {"type": "string"},
        "effect_label": {"type": "string"},
        "visual_metaphor": {"type": "string"},
        "visual_structure": {"type": "string", "enum": ["cause_to_effect", "before_after", "hidden_mechanism", "obstacle_and_solution", "contrast"]},
    }
    return {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "scenes": {
                "type": "array",
                "minItems": 20,
                "maxItems": 20,
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "scene_number": {"type": "integer"},
                        "body": {"type": "string", "minLength": 180, "maxLength": 220},
                    },
                    "required": ["scene_number", "body"],
                },
            },
            "titles": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "pattern_a": {"type": "string"},
                    "pattern_b": {"type": "string"},
                    "pattern_c": {"type": "string"},
                },
                "required": ["pattern_a", "pattern_b", "pattern_c"],
            },
            "schedule": {
                "type": "array",
                "minItems": 5,
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {"time": {"type": "string"}, "topic": {"type": "string"}},
                    "required": ["time", "topic"],
                },
            },
            "description": {
                "type": "object",
                "additionalProperties": False,
                "properties": {"text": {"type": "string"}, "count": {"type": "integer"}},
                "required": ["text", "count"],
            },
            "comment": {"type": "array", "minItems": 3, "items": {"type": "string"}},
            "thumbnail_ideas": {"type": "string"},
            "thumbnail_comments": {"type": "string"},
            "metadata": {"type": "object", "additionalProperties": False, "properties": {}},
            "image_prompts": {
                "type": "array",
                "minItems": 20,
                "maxItems": 20,
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": image_prompt_properties,
                    "required": list(image_prompt_properties),
                },
            },
            "research_scene_11": {"type": "string"},
            "research_scene_15": {"type": "string"},
        },
        "required": [
            "scenes",
            "titles",
            "schedule",
            "description",
            "comment",
            "thumbnail_ideas",
            "thumbnail_comments",
            "metadata",
            "image_prompts",
            "research_scene_11",
            "research_scene_15",
        ],
    }


def _write_raw_ai_response(path: Path | None, text: str) -> None:
    if path is None:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _write_ai_json_parse_error_report(error_dir: Path | None, text: str) -> None:
    if error_dir is None:
        return
    error_dir.mkdir(parents=True, exist_ok=True)
    (error_dir / "raw_ai_response.txt").write_text(text, encoding="utf-8")
    (error_dir / "error_report.md").write_text(
        "\n".join(
            [
                "エラー種別：AI応答JSONパース失敗",
                "原因：OpenAI APIの応答が単一JSONとして解釈できませんでした",
                "発生箇所：generator.py / generate_ai_assets / json.loads(text)",
                "対応：raw_ai_response.txt を確認し、JSON schema指定または出力形式を修正してください",
                "",
            ]
        ),
        encoding="utf-8",
    )


def generate_ai_assets(
    source_text: str,
    book_name: str,
    rules_text: str,
    *,
    model: str,
    asset_checks: list[AssetCheck] | None = None,
    raw_response_path: Path | None = None,
    error_dir: Path | None = None,
) -> GeneratedAssets:
    from openai import OpenAI

    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    prompt = f"""
Book BaseのYouTube制作補助として、以下の入力本文から成果物を作成してください。
必ずルールを守り、APIで指定されたJSON schemaに一致する単一JSONオブジェクトのみを返してください。
JSONの前後に説明文、Markdown、コードフェンス、複数JSONを付けないでください。

書籍名: {book_name}

制作ルール:
{rules_text}

入力本文:
{source_text}

入力画像チェック結果:
{_asset_context_for_prompt(asset_checks)}

返却JSONキー:
scenes, titles, description, thumbnail_ideas, thumbnail_comments, metadata, image_prompts, research_scene_11, research_scene_15

原稿生成は、内部で必ず次の工程に分けてから最終JSONへ反映してください。Step 1: 入力本文から本のテーマ、著者、読者の悩み、中心メッセージ、会社員への接続点、3つの重要ポイントを抽出する。Step 2: 最新ルールに沿って20シーンの役割を設計する。Step 3: 各シーン180〜220字で初稿を作る。Step 4: Book Baseらしい読み上げ原稿へリライトする。Step 5: 20シーン、各180〜220字、全体3600〜4400字を検証する。Step 6: 形式・文字数・文体のどれかがNGなら再リライトする。
Book Base文体として、説明文ではなく視聴者への語りかけにしてください。短い文、中くらいの文、少し長い文を混ぜ、句読点を自然に置き、語尾を単調にしないでください。「また」「さらに」「そして」の機械的な連発を避け、「ここで大事なのは」「たとえば」「会社員の感覚で言うと」「実は」などを流れに合わせて自然に使ってください。会議、報連相、上司への相談、後輩への指摘、チャットでの一言など、会社員が自分ごと化できる具体場面を、本の内容に沿う範囲で入れてください。
以下のAIっぽい表現は避けてください: 「効果的と言われています」「が特徴です」「について探っていきます」「ヒントが満載です」「第一人者です」「検証済みです」「とされています」「の重要性が示されています」「と言われています」「可能になるのです」。
scene_07は具体的な研究・調査・公的データに寄せ、出典が弱い場合は断定せずNEEDS_REVIEWを本文またはresearch情報に残してください。scene_11は確認可能な人物・出来事だけを使い、確認できない実在企業・人物名は出さないでください。scene_15は発言者・原文・文脈を確認できる名言だけを使い、確認できない場合は断定せずNEEDS_REVIEWにしてください。
完成前に、読みたくなる言い回し、一文の長さ、句読点、接続詞、語尾、会社員目線、AIっぽさ、本の内容との一致、シーン役割、次シーンへの流れを5点満点で自己採点し、平均4点未満なら再生成してください。

scenesは必ず20件の配列にし、各要素はscene_number（1〜20の整数）とbody（見出しを含まない本文）のみで返してください。Python側でscript.mdをレンダリングします。bodyは各シーン180〜220字、本文内改行なしの1段落、箇条書きなしにしてください。
titlesはpattern_a/pattern_b/pattern_cの構造化JSON、scheduleはtime/topicの配列、descriptionはtext/countの構造化JSON、commentは3行の配列で返してください。metadataは空のオブジェクトで構いません（Python側でMarkdownに整形します）。
thumbnail_commentsはPattern A/B/Cの方向性・コメント・狙い・出力ファイル名・使用画像・needs_reviewを含めてください。
image_promptsは20件の配列にし、各要素に「シーン番号」「所属ブロック」「ブロックの役割」「重要ポイント番号」「ブロック内での役割」「前ブロックからの理解の流れ」「このシーンで伝える要点」「画像の目的」「推奨構図」「画面内テキスト」「前後画像との差別化」「使用画像」「入力画像チェック」「needs_review」「最終プロンプト」を必ず含めてください。
画像生成前提として、内部で image_context.json 相当の book_title, author_name, current_theme, quiz, three_key_points, assets を原稿と入力画像チェックから抽出してください。scene_01〜scene_05は「固定役割」と「可変内容」を必ず分離し、具体的な正解文言、テーマ語句、ポイント語句、タイトル、著者名、book_cover/authorパスは毎回の原稿とinputから生成してください。scene_06の固定役割は「重要ポイント①の理由・背景・仕組み説明」です。scene_06ではscene_05の重要ポイント①とscene_06本文から、point_1_label, scene_06_core_message, reason_label, mechanism_label, effect_label, visual_metaphor, visual_structureを毎回抽出してください。visual_structureはcause_to_effect / before_after / hidden_mechanism / obstacle_and_solution / contrastから内容に合わせて1つ選び、構図に反映してください。scene_06のexact_text_elementsは原稿由来の短いラベル3つ以内、各15文字以内にし、特定の本や過去テーマの語句をテンプレートに固定しないでください。scene_06ではgeneric emotional icons、generic business person image、机・付箋・ノートだけの雰囲気画像、scene_05と同じ構図を禁止してください。恒久テンプレートに今回の本だけの言葉を固定しないでください。各sceneのexact_text_elementsを必ず原稿由来で作り、最終プロンプトには必ず次の英文を入れてください: Use only the following Japanese text elements exactly as written. Do not add any other Japanese or English text.
scene_11とscene_15の人物参考画像はユーザー入力必須ではありません。scene_11は原稿生成後に重要ポイント②を補強する実在人物と確認済み実話を選び、人物名・概要・実話・重要ポイント②とのつながり・確認した出典・画像生成時の表現方針をresearch_scene_11にMarkdownで記録してください。
scene_15は原稿生成後に重要ポイント③を補強する確認済み名言を選び、名言・発言者・概要・意味・重要ポイント③とのつながり・確認した出典・画像生成時の表現方針をresearch_scene_15にMarkdownで記録してください。
出典確認できない実話や名言は断定せず、別候補に差し替えるかNEEDS_REVIEWを明記してください。人物画像が取得できない場合は顔を想像で描かず、シルエット・行動場面・名言カード・静物構図で代替してください。
""".strip()
    validation_errors: list[str] = []
    last_text = ""
    last_data: Any = None
    for attempt in range(1, 4):
        attempt_prompt = prompt
        if validation_errors:
            attempt_prompt += "\n\n前回の原稿は以下の理由でNGです。NG箇所だけでなく全体を見直し、Book Base最新ルールを満たすscenes配列として再生成してください。\n" + "\n".join(f"- {error}" for error in validation_errors)
        response = client.responses.create(
            model=model,
            input=attempt_prompt,
            text={
                "format": {
                    "type": "json_schema",
                    "name": "bookbase_assets",
                    "strict": True,
                    "schema": _bookbase_assets_json_schema(),
                }
            },
        )
        text = response.output_text
        last_text = text
        _write_raw_ai_response(raw_response_path, text)
        try:
            data = json.loads(text)
            last_data = data
        except json.JSONDecodeError as exc:
            _write_ai_json_parse_error_report(error_dir, text)
            raise AIResponseJSONParseError("AI応答JSONパース失敗") from exc
        try:
            script = render_script_from_scenes(data["scenes"])
            validation_errors = validate_bookbase_script(script)
            if validation_errors:
                continue
            return GeneratedAssets(
                script=script,
                titles=render_titles(data["titles"]),
                description=render_description(data["description"]),
                thumbnail_ideas=_ensure_markdown_text(data["thumbnail_ideas"], "thumbnail_ideas"),
                thumbnail_comments=_ensure_markdown_text(data.get("thumbnail_comments", ""), "thumbnail_comments"),
                metadata=render_metadata(data),
                image_prompts=render_image_prompts(data["image_prompts"]),
                image_context=json.dumps(build_image_context(script, book_name, asset_checks), ensure_ascii=False, indent=2) + "\n",
                research_scene_11=_ensure_markdown_text(data.get("research_scene_11", _build_research_scene_11()), "research_scene_11"),
                research_scene_15=_ensure_markdown_text(data.get("research_scene_15", _build_research_scene_15()), "research_scene_15"),
            )
        except (KeyError, ValueError) as exc:
            validation_errors = [str(exc)]
            if attempt < 3:
                continue
            _write_ai_json_validation_error_report(error_dir, str(exc), data)
            raise AIResponseValidationError("AI応答JSON型検証失敗") from exc
    if error_dir is not None:
        error_dir.mkdir(parents=True, exist_ok=True)
        (error_dir / "raw_ai_response.txt").write_text(last_text, encoding="utf-8")
        (error_dir / "parsed_ai_response.json").write_text(json.dumps(last_data, ensure_ascii=False, indent=2), encoding="utf-8")
        (error_dir / "error_report.md").write_text(
            "\n".join([
                "エラー種別：原稿形式・文字数違反",
                "原因：AI生成原稿がBook Baseの最新ルールを満たしませんでした",
                "違反内容：",
                *[f"- {error}" for error in validation_errors],
                "対応：",
                "- 原稿生成プロンプトまたはJSON schemaを修正してください",
                "- scenes配列で受け取り、Python側でscript.mdをレンダリングしてください",
                "",
            ]),
            encoding="utf-8",
        )
    raise AIResponseValidationError("原稿形式・文字数違反")
