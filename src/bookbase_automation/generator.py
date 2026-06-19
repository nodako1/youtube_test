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
    scene9 = _scene_body(script, 9)
    scene10 = _scene_body(script, 10)
    scene11 = _scene_body(script, 11)
    scene12 = _scene_body(script, 12)
    scene13 = _scene_body(script, 13)
    scene14 = _scene_body(script, 14)
    scene15 = _scene_body(script, 15)
    scene16 = _scene_body(script, 16)
    scene17 = _scene_body(script, 17)
    scene18 = _scene_body(script, 18)
    scene20 = _scene_body(script, 20)
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
        "source_text": script,
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
        "scene_bodies": {"scene_05": scene5, "scene_06": scene6, "scene_07": scene7, "scene_09": scene9, "scene_10": scene10, "scene_11": scene11, "scene_12": scene12, "scene_13": scene13, "scene_14": scene14, "scene_15": scene15, "scene_16": scene16, "scene_17": scene17, "scene_18": scene18, "scene_20": scene20},
        "assets": {
            "book_cover": _asset_path(asset_checks, "scene_03_current_book_cover"),
            "author_reference": _asset_path(asset_checks, "scene_04_author_reference"),
            "related_book_cover": _asset_path(asset_checks, "scene_19_related_book_cover"),
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


def _scene_08_composition() -> str:
    return "中央に上品な登録カードを置き、カードに『チャンネル登録』、下に小さく『本の学びを仕事へ』を配置する。周囲に本、ノート、ペン、しおり、コーヒーを控えめに置き、背景は淡いクリーム色でティールとゴールドのアクセントを使う。scene_07の資料・グラフ・レポート構図とは明確に変える。"


def _scene_08_structured_prompt(context: dict[str, object]) -> dict[str, object]:
    elements = ["チャンネル登録", "本の学びを仕事へ"]
    composition = _scene_08_composition()
    visual_motifs = ["登録カード", "本", "ノート", "ペン", "しおり", "柔らかい光"]
    negative_rules = [
        "英語テキストを入れない",
        "赤い派手な登録ボタンにしない",
        "押し売り感を出さない",
        "長文CTAを入れない",
        "scene_07の資料・グラフ構図と被らせない",
    ]
    final_prompt = f"""Create a 16:9 landscape video-insert image for Book Base, a Japanese business book YouTube channel. Use a refined watercolor illustration style with a premium, calm, elegant atmosphere. Use a soft cream-white and beige background with teal and subtle gold accents. Include a small natural Book Base logo placed unobtrusively.

This is Scene 08. Its fixed role is a subscription CTA for the Book Base channel. The image should invite viewers to subscribe in an elegant, non-pushy way. It should feel like a calm invitation to keep learning from business books, not a loud advertisement. Book Base delivers popular books from the perspective of applying book insights to work and income growth. Do not include any current book title, author name, Key Point 1 content, Scene 07 evidence data, or book-specific keywords.

{TEXT_LOCK_INSTRUCTION}:
{_text_block(elements)}

Composition:
{composition}

Visual motifs:
- elegant subscription card
- books or business book motif
- notebook and pen
- calm desk setup
- subtle notification or bookmark icon
- soft light
- enough whitespace
- premium watercolor texture

Keep the image clean and easy to understand at a glance. Use minimal Japanese text only. Do not place long script text. Avoid English text, avoid red flashy subscribe-button design, avoid aggressive advertising, avoid clutter, and avoid repeating the Scene 07 report/data composition."""
    return {
        "scene": 8,
        "fixed_role": "チャンネル登録CTA",
        "scene_role": "チャンネル登録CTA",
        "core_message": "Book Baseの学びを継続して受け取るための自然な登録案内",
        "cta_tone": "elegant_non_pushy",
        "exact_text_elements": elements,
        "composition": composition,
        "visual_motifs": visual_motifs,
        "style": _COMMON_STYLE_FOR_SCHEMA,
        "negative_rules": negative_rules,
        "variation_key": "scene-08-elegant-non-pushy-subscription-card",
        "final_prompt": final_prompt,
    }

def _scene_09_point_type(scene9_body: str) -> str:
    if re.search(r"習慣|毎日|続け|日々|ルーティン", scene9_body):
        return "habit"
    if re.search(r"手順|ステップ|流れ|進め方|順番|プロセス", scene9_body):
        return "process"
    if re.search(r"比較|対比|違い|一方|普通|従来|ではなく", scene9_body):
        return "contrast"
    if re.search(r"スキル|技術|使い方|活用|フレーズ|技法|実践", scene9_body):
        return "skill"
    if re.search(r"型|フレーム|整理法|枠組み|テンプレート", scene9_body):
        return "framework"
    if re.search(r"考え方|視点|前提|捉え|発想|マインド", scene9_body):
        return "mindset"
    return "method"


def _scene_09_composition(point_2_type: str) -> str:
    if point_2_type in {"mindset", "contrast"}:
        return "構図C：視点切り替え型。左に前のポイントを小さく薄く、右に『重要ポイント②』カードと現在の視覚比喩を置き、上品な余白と細い矢印で2つ目へ移ったことを示す。会話人物にはしない。"
    if point_2_type in {"method", "skill", "process"}:
        return "構図D：実践方法の入口型。左または中央に『重要ポイント②』カード、右にノート・手順カード・ツールアイコンなど現在内容に合う入口モチーフを置く。scene_08のCTAカードやscene_05の導入カードと被らせない。"
    if point_2_type in {"habit", "framework"}:
        return "構図B：次のステップ型。ロードマップや階段の2段目に『重要ポイント②』を置き、習慣や型に合う象徴モチーフを添える。scene_05の1点ズーム構図とは変える。"
    return "構図A：第2ポイントカード型。中央または左側に『重要ポイント②』カード、右側に現在のpoint_2_typeに合った象徴モチーフを置く。"


def _scene_09_structured_prompt(context: dict[str, object]) -> dict[str, object]:
    point = context["three_key_points"][1]
    scene_bodies = context.get("scene_bodies", {})
    scene9_body = str(scene_bodies.get("scene_09", "")) if isinstance(scene_bodies, dict) else ""
    point_2_label = _short_label(re.sub(r"^重要ポイントの2つ目は", "", scene9_body), str(point["label"]), 14)
    core_message = _short_label(scene9_body or str(point["core_message"]), str(point["label"]), 30)
    point_2_type = _scene_09_point_type(scene9_body)
    point_2_short_message = _short_label(re.split(r"。|、", scene9_body)[1] if "、" in scene9_body else core_message, "次の視点へ", 15)
    elements = ["重要ポイント②", point_2_label[:15], point_2_short_message[:15]]
    visual_metaphor = "current-script-derived metaphor for Key Point 2, such as a second step, next card, roadmap turn, method notebook, framework board, habit calendar, or contrast panels selected to match point_2_type"
    composition = _scene_09_composition(point_2_type)
    visual_motifs = ["第2ポイントカード", "次のステップ", "細い矢印", "現在内容に合う象徴モチーフ", "余白"]
    final_prompt = f"""Create a 16:9 landscape video-insert image for Book Base, a Japanese business book YouTube channel. Use a refined watercolor illustration style with a premium, calm, elegant atmosphere. Use a soft cream-white and beige background with teal and subtle gold accents. Include a small natural Book Base logo placed unobtrusively.

This is Scene 09. Its fixed role is to introduce Key Point 2. The image should make viewers understand that the video is moving into the second important point. Do not create a generic business conversation image. Do not hard-code any topic from a previous book. Build the visual message from the current script only.

Current Key Point 2:
{point_2_label}

Current Scene 09 core message:
{core_message}

Point 2 type:
{point_2_type}

{TEXT_LOCK_INSTRUCTION}:
{_text_block(elements)}

Visual metaphor:
{visual_metaphor}

Composition:
{composition}

Visual motifs:
{', '.join(visual_motifs)}

Keep the image clean and easy to understand at a glance. Use minimal Japanese text only. Do not place long script text. Avoid clutter, avoid generic conversation scenes, avoid over-explaining, avoid English text, and avoid repeating the Scene 08 CTA composition or Scene 05 Key Point 1 composition."""
    return {"scene": 9, "fixed_role": "重要ポイント②の導入", "scene_role": "重要ポイント②の導入", "point_2_label": point_2_label, "core_message": core_message, "point_2_core_message": core_message, "point_2_type": point_2_type, "visual_metaphor": visual_metaphor, "exact_text_elements": elements, "composition": composition, "visual_motifs": visual_motifs, "style": _COMMON_STYLE_FOR_SCHEMA, "negative_rules": ["会話シーンを固定しない", "視点変更を固定しない", "特定テーマを固定しない", "scene_05と同じ構図にしない", "scene_08のCTA構図にしない", "長文や英語テキストを入れない"], "variation_key": f"scene-09-key-point-2-{point_2_type}-introduction", "final_prompt": final_prompt}

def _scene_10_visual_structure(scene10_body: str) -> str:
    if re.search(r"前|後|改善|変化|習慣|ではなく|代わり|置き換", scene10_body):
        return "before_after"
    if re.search(r"手順|ステップ|順番|まず|次に|最後|流れ", scene10_body):
        return "step_demo"
    if re.search(r"比較|対比|違い|普通|従来|良い|悪い|一方", scene10_body):
        return "comparison"
    if re.search(r"複数|やること|行動|実践|仕事|生活|転用|活用", scene10_body):
        return "action_map"
    if re.search(r"型|フレーム|整理法|チェックリスト|判断基準|基準", scene10_body):
        return "framework_demo"
    return "example_scene"


def _scene_10_composition(visual_structure: str) -> str:
    compositions = {
        "before_after": "before_after：変化前の小さな曇ったカードから、変化後の明るい実践カードへ視線が流れる構図。Scene 09の重要ポイントカード構図を繰り返さず、具体的な使用前後が分かる小道具と余白で見せる。",
        "step_demo": "step_demo：3つ以内の実践ステップを、机上のカードや道しるべのように斜めに配置する構図。Scene 09の導入カードではなく、手元で順に使うイメージにする。",
        "example_scene": "example_scene：現在の原稿に合う一つの具体場面を、人物に寄せすぎず道具・メモ・場面の象徴で見せる構図。Scene 11の実話エピソード風の肖像や歴史場面にはしない。",
        "comparison": "comparison：2つの短い選択肢や考え方を、左右固定のsplit-screenではなく、重なったカードや天秤風の上品な比較で見せる構図。Scene 09の導入カードと差を出す。",
        "action_map": "action_map：具体行動へ落とす小さな地図やルート、チェックポイントを配置する構図。Scene 09の入口感ではなく、実際に進める使い方を示す。",
        "framework_demo": "framework_demo：現在の内容に合う型・チェックリスト・判断基準を、ホワイトボード風ではなく上品なワークシートとして見せる構図。",
    }
    return compositions[visual_structure]


def _scene_10_structured_prompt(context: dict[str, object]) -> dict[str, object]:
    point = context["three_key_points"][1]
    scene_bodies = context.get("scene_bodies", {})
    scene9_body = str(scene_bodies.get("scene_09", "")) if isinstance(scene_bodies, dict) else ""
    scene10_body = str(scene_bodies.get("scene_10", "")) if isinstance(scene_bodies, dict) else ""
    point_2_label = _short_label(re.sub(r"^重要ポイントの2つ目は", "", scene9_body), str(point["label"]), 14)
    core_source = scene10_body or str(point["core_message"])
    scene_10_core_message = _short_label(core_source, str(point["core_message"]), 34)
    clauses = [c for c in re.split(r"。|、", core_source) if c]
    example_label = _short_label(clauses[0] if clauses else core_source, point_2_label, 12)
    application_label = _short_label(next((c for c in clauses if re.search(r"使|実践|手順|方法|行動|活用|試", c)), scene_10_core_message), "使い方", 12)
    result_label = _short_label(next((c for c in clauses if re.search(r"変化|理解|反応|効果|結果|でき|わか|分か", c)), scene_10_core_message), "変化が見える", 12)
    visual_structure = _scene_10_visual_structure(scene10_body)
    visual_metaphor = "current-script-derived practical metaphor for making Key Point 2 concrete, selected from the current Scene 10 example, steps, comparison, application, or practice image"
    elements = [example_label[:15], application_label[:15], result_label[:15]]
    composition = _scene_10_composition(visual_structure)
    visual_motifs = ["原稿由来の具体例", "実践カード", "短いキーワード", "Scene 09と異なる構図", "余白"]
    final_prompt = f"""Create a 16:9 landscape video-insert image for Book Base, a Japanese business book YouTube channel. Use a refined watercolor illustration style with a premium, calm, elegant atmosphere. Use a soft cream-white and beige background with teal and subtle gold accents. Include a small natural Book Base logo placed unobtrusively.

This is Scene 10. Its fixed role is to make Key Point 2 concrete through an example, comparison, practical step, or application image. The image should help viewers understand how Key Point 2 works in practice. Do not create a generic cause-and-effect flowchart unless the current script actually requires it. Do not hard-code any topic from a previous book. Build the visual message from the current script only.

Current Key Point 2:
{point_2_label}

Current Scene 10 core message:
{scene_10_core_message}

Visual structure:
{visual_structure}

{TEXT_LOCK_INSTRUCTION}:
{_text_block(elements)}

Visual metaphor:
{visual_metaphor}

Composition:
{composition}

Visual motifs:
{', '.join(visual_motifs)}

Keep the image clean and easy to understand at a glance. Use minimal Japanese text only. Do not place long script text. Avoid clutter, avoid generic split-screen flowcharts, avoid generic business people, avoid English text, and avoid repeating the Scene 09 composition."""
    return {"scene": 10, "fixed_role": "重要ポイント②の具体化", "scene_role": "重要ポイント②の具体化", "core_message": scene_10_core_message, "point_2_label": point_2_label, "scene_10_core_message": scene_10_core_message, "example_label": example_label, "application_label": application_label, "result_label": result_label, "visual_structure": visual_structure, "visual_metaphor": visual_metaphor, "exact_text_elements": elements, "composition": composition, "visual_motifs": visual_motifs, "style": _COMMON_STYLE_FOR_SCHEMA, "negative_rules": ["split-screenを固定しない", "cause-and-effectを固定しない", "ビジネス会話シーンを固定しない", "scene_09と同じ構図にしない", "scene_11の実話エピソード風にしない", "長文や英語テキストを入れない"], "variation_key": f"scene-10-key-point-2-concrete-{visual_structure}", "final_prompt": final_prompt}


def _scene_11_episode_type(scene11_body: str) -> str:
    if re.search(r"企業|会社|組織|メーカー|社|チーム", scene11_body):
        return "company"
    if re.search(r"出来事|事件|歴史|運動|制度|政策", scene11_body):
        return "historical_event"
    if re.search(r"調査|公的|裁判|事例|ケース", scene11_body):
        return "public_case"
    if re.search(r"人物|著名|経営者|創業者|氏|さん", scene11_body):
        return "person"
    return "symbolic_only"


def _scene_11_verification_status(scene11_body: str) -> str:
    if re.search(r"NEEDS_REVIEW|未確認|出典不明|確認できない|根拠が弱い|曖昧|不確か", scene11_body, re.I):
        return "needs_review"
    if re.search(r"確認済み|検証済み|出典|一次資料|公的|公式|論文|報告書|資料で確認", scene11_body):
        return "verified"
    return "needs_review"


def _scene_11_visual_mode(episode_type: str, verification_status: str) -> str:
    if verification_status == "verified" and episode_type != "symbolic_only":
        return "named_episode"
    if verification_status == "needs_review" and episode_type in {"person", "company", "historical_event", "public_case"}:
        return "silhouette_episode"
    return "symbolic_action"


def _scene_11_composition(visual_mode: str) -> str:
    compositions = {
        "named_episode": "構図A：中央に「実話エピソード」のカードを置き、周囲に検証済みエピソードを象徴する資料、会議メモ、行動シーンを控えめに配置する。顔の再現ではなく行動と教訓を主役にし、Scene 10の具体例・手順図解とは違うエピソードカード型にする。",
        "silhouette_episode": "構図D：人物や組織を特定しすぎない後ろ姿・横顔シルエットと、資料、ノート、仕事場面のモチーフで実話補強を示す。顔やロゴを描かず、Scene 10の具体例画像と混ざらないようカード中心にする。",
        "symbolic_action": "構図B：人物名より行動を見せる。資料を渡す、記録する、チームで確認する、決断するなどの象徴的な行動を水彩で描き、未検証の実在名や顔を出さない。",
    }
    return compositions[visual_mode]


def _scene_11_structured_prompt(context: dict[str, object]) -> dict[str, object]:
    point = context["three_key_points"][1]
    scene_bodies = context.get("scene_bodies", {})
    scene9_body = str(scene_bodies.get("scene_09", "")) if isinstance(scene_bodies, dict) else ""
    scene10_body = str(scene_bodies.get("scene_10", "")) if isinstance(scene_bodies, dict) else ""
    scene11_body = str(scene_bodies.get("scene_11", "")) if isinstance(scene_bodies, dict) else ""
    point_2_label = _short_label(re.sub(r"^重要ポイントの2つ目は", "", scene9_body), str(point["label"]), 14)
    scene_11_core_message = _short_label(scene11_body or scene10_body, str(point["core_message"]), 34)
    episode_type = _scene_11_episode_type(scene11_body)
    verification_status = _scene_11_verification_status(scene11_body)
    visual_mode = _scene_11_visual_mode(episode_type, verification_status)
    name_match = re.search(r"(?:人物名|企業名|出来事名|発言者|創業者|経営者)?[：:、]?\s*([一-龥ァ-ヴーA-Za-z0-9・＆&\\. ]{2,24})(?:の|は|が|氏|さん)", scene11_body)
    episode_name = _short_label(name_match.group(1), "", 18) if (name_match and verification_status == "verified") else None
    action_label = _short_label(next((c for c in re.split(r"。|、", scene11_body) if re.search(r"行動|実践|見直|記録|共有|決断|改善|続け|変え", c)), scene11_body), "行動で補強", 12)
    lesson_label = _short_label(next((c for c in re.split(r"。|、", scene11_body + scene10_body) if re.search(r"つながり|教訓|重要|姿勢|仕組み|考え方|判断", c)), scene_11_core_message), "教訓を仕事へ", 12)
    text2 = episode_name if verification_status == "verified" and episode_name else ("象徴シーン" if verification_status == "needs_review" else "NEEDS_REVIEW")
    elements = ["実話エピソード", text2[:15], lesson_label[:15]]
    composition = _scene_11_composition(visual_mode)
    visual_motifs = ["実話エピソードカード", "資料", "行動シーン", "短い教訓ラベル", "Scene 10と異なる構図"]
    final_prompt = f"""Create a 16:9 landscape video-insert image for Book Base, a Japanese business book YouTube channel. Use a refined watercolor illustration style with a premium, calm, elegant atmosphere. Use a soft cream-white and beige background with teal and subtle gold accents. Include a small natural Book Base logo placed unobtrusively.

This is Scene 11. Its fixed role is to reinforce Key Point 2 with a real-life episode. The episode must be based on current script research. Do not hard-code any person, company, or historical figure from a previous book. Do not invent a real-life episode. If verification is weak, use a silhouette or symbolic action scene instead of a named person.

Current Key Point 2:
{point_2_label}

Current Scene 11 core message:
{scene_11_core_message}

Episode type:
{episode_type}

Verification status:
{verification_status}

Visual mode:
{visual_mode}

{TEXT_LOCK_INSTRUCTION}:
{_text_block(elements)}

Composition:
{composition}

Visual motifs:
{', '.join(visual_motifs)}

Keep the image clean and easy to understand at a glance. Use minimal Japanese text only. Do not place long script text. Avoid clutter, avoid fake historical portraits, avoid invented company imagery, avoid overly realistic faces, avoid hard-coded Toyota or any previous-book topic, and avoid repeating the Scene 10 composition."""
    return {"scene": 11, "fixed_role": "重要ポイント②の実話エピソード補強", "scene_role": "重要ポイント②の実話エピソード補強", "core_message": scene_11_core_message, "point_2_label": point_2_label, "scene_11_core_message": scene_11_core_message, "episode_type": episode_type, "episode_name": episode_name, "episode_role_label": "実話の当事者" if episode_type == "person" else "実話の組織・出来事", "episode_action_label": action_label, "lesson_label": lesson_label, "verification_status": verification_status, "visual_mode": visual_mode, "exact_text_elements": elements, "composition": composition, "visual_motifs": visual_motifs, "style": _COMMON_STYLE_FOR_SCHEMA, "negative_rules": ["Toyotaや特定企業名を固定しない", "特定人物名を固定しない", "未検証の人物名・企業名・顔を出さない", "portrait中心にしない", "scene_10と同じ構図にしない", "長文や英語テキストを入れない"], "variation_key": f"scene-11-real-episode-{visual_mode}", "final_prompt": final_prompt}


def _scene_13_point_type(scene13_body: str) -> str:
    if re.search(r"判断基準|選び方|見極め|基準|決め方|優先", scene13_body):
        return "decision_rule"
    if re.search(r"型|フレーム|整理法|枠組み|テンプレート|構造", scene13_body):
        return "framework"
    if re.search(r"習慣|続け|継続|日々|毎日|積み上げ|ルーティン", scene13_body):
        return "habit"
    if re.search(r"解決|打ち手|改善策|対策|乗り越|解消", scene13_body):
        return "solution"
    if re.search(r"考え方|姿勢|前提|向き合|視点|本質|捉え方", scene13_body):
        return "mindset"
    if re.search(r"実践|行動|使い方|活用|試す|始める|移す|フレーズ", scene13_body):
        return "practice"
    return "final_perspective"


def _scene_13_composition(point_3_type: str) -> str:
    if point_3_type in {"practice", "solution"}:
        return "構図C：実践への橋渡し型。左に『重要ポイント③』カード、中央から右へ光の道・橋・矢印を伸ばし、理論から実践や解決へ移る入口を示す。チェックリスト、planner、手元ノート、作業完了シーンにはしない。"
    if point_3_type in {"framework", "decision_rule"}:
        return "構図D：整理された型の提示型。中央に第3ポイントカード、右側に整理された枠・判断カード・シンプルな図を置き、3つ目の方法や基準が見えるようにする。scene_09の第2ポイントカードやscene_12のコメントカードとは配置を変える。"
    if point_3_type in {"habit", "final_perspective"}:
        return "構図B：最後の扉・最終ステップ型。3枚目のカード、最終ステップ、光の扉、上品な道のモチーフで、動画が最後の重要ポイントへ入ることを示す。実践完了や日常タスク整理に寄せすぎない。"
    return "構図A：第3ポイントカード型。中央または左側に『重要ポイント③』カード、右側に現在のpoint_3_typeに合った象徴モチーフを置き、最後の大きな学びへの切り替わりを見せる。"


def _scene_13_structured_prompt(context: dict[str, object]) -> dict[str, object]:
    point = context["three_key_points"][2]
    scene_bodies = context.get("scene_bodies", {})
    scene13_body = str(scene_bodies.get("scene_13", "")) if isinstance(scene_bodies, dict) else ""
    point_3_label = _short_label(re.sub(r"^重要ポイントの3つ目は", "", scene13_body), str(point["label"]), 14)
    point_3_core_message = _short_label(scene13_body or str(point["core_message"]), str(point["label"]), 34)
    point_3_type = _scene_13_point_type(scene13_body)
    clauses = [c for c in re.split(r"。|、", scene13_body) if c]
    point_3_short_message = _short_label(next((c for c in clauses[1:] if c), point_3_core_message), "最後の視点へ", 15)
    elements = ["重要ポイント③", point_3_label[:15], point_3_short_message[:15]]
    visual_metaphor = "current-script-derived metaphor for Key Point 3, such as the third card, final door, last step, light path, bridge to practice, framework board, habit path, or decision compass selected to match point_3_type"
    scene_13_composition = _scene_13_composition(point_3_type)
    visual_motifs = ["第3ポイントカード", "最後の扉", "光の道", "現在内容に合う象徴モチーフ", "余白"]
    final_prompt = f"""Create a 16:9 landscape video-insert image for Book Base, a Japanese business book YouTube channel. Use a refined watercolor illustration style with a premium, calm, elegant atmosphere. Use a soft cream-white and beige background with teal and subtle gold accents. Include a small natural Book Base logo placed unobtrusively.

This is Scene 13. Its fixed role is to introduce Key Point 3. The image should make viewers understand that the video is moving into the third and final major point. Do not create a generic checklist or planner image unless the current script actually requires it. Do not hard-code any topic from a previous book. Build the visual message from the current script only.

Current Key Point 3:
{point_3_label}

Current Scene 13 core message:
{point_3_core_message}

Point 3 type:
{point_3_type}

{TEXT_LOCK_INSTRUCTION}:
{_text_block(elements)}

Visual metaphor:
{visual_metaphor}

Composition:
{scene_13_composition}

Visual motifs:
{', '.join(visual_motifs)}

Keep the image clean and easy to understand at a glance. Use minimal Japanese text only. Do not place long script text. Avoid clutter, avoid generic checklist images, avoid close-up hands writing unless necessary, avoid English text, and avoid repeating the Scene 09 or Scene 12 composition."""
    return {"scene": 13, "fixed_role": "重要ポイント③の導入", "scene_role": "重要ポイント③の導入", "point_3_label": point_3_label, "core_message": point_3_core_message, "point_3_core_message": point_3_core_message, "point_3_type": point_3_type, "visual_metaphor": visual_metaphor, "exact_text_elements": elements, "composition": scene_13_composition, "visual_motifs": visual_motifs, "style": _COMMON_STYLE_FOR_SCHEMA, "negative_rules": ["チェックリストを固定しない", "plannerを固定しない", "手元ノート構図を固定しない", "scene_09と同じ構図にしない", "scene_12と同じ構図にしない", "scene_18の実践完了画像と混ぜない", "長文や英語テキストを入れない"], "variation_key": f"scene-13-key-point-3-{point_3_type}-introduction", "final_prompt": final_prompt}



def _scene_14_visual_structure(scene14_body: str) -> str:
    if re.search(r"手順|ステップ|順番|まず|次に|最後|流れ|段階", scene14_body):
        return "step_demo"
    if re.search(r"前|後|変化|改善|比べ|違い|Before|After", scene14_body, flags=re.I):
        return "before_after"
    if re.search(r"ノート|チェックリスト|表|カード|フレーム|型|道具|ツール", scene14_body):
        return "tool_use"
    if re.search(r"判断基準|基準|フレームワーク|枠組み|当てはめ|選び方|見極め", scene14_body):
        return "framework_application"
    if re.search(r"例えば|たとえば|場面|ケース|仕事|日常|相談|読書|整理|休息|お金|会議|上司|チャット", scene14_body):
        return "scenario_demo"
    return "practical_example"


def _scene_14_composition(visual_structure: str) -> str:
    compositions = {
        "practical_example": "構図A：現在の原稿に出てくる具体例を、人物や手元を小さめにした実践場面として描く。scene_13の重要ポイントカードを繰り返さず、scene_18の全体実践・まとめ行動よりも一つの使い方に絞る。",
        "step_demo": "構図B：左から右へ3つ以内の小さなステップカードを並べ、現在のscene_14本文にある使い方の流れだけを見せる。長い手順説明やgeneric checklistにはしない。",
        "before_after": "構図C：左に実践前、右に実践後の変化を余白多めに対比し、中央に小さな矢印や光を置く。scene_13の導入カードやscene_18の日常実践シーンとは別構図にする。",
        "tool_use": "構図D：ノート、カード、表、チェック欄など現在の内容に合う道具を一つ主役にし、使い方が分かる手元または俯瞰構図にする。道具名や固定テーマをテンプレート化しない。",
        "scenario_demo": "構図E：現在の原稿にある具体場面だけを小さなシナリオとして描く。会議や上司対応に固定せず、必要な場合だけその場面を使う。",
        "framework_application": "構図F：判断基準や型を実際の対象に当てはめている様子を、カードやシンプルな枠で示す。抽象的な重要ポイントカードだけにしない。",
    }
    return compositions.get(visual_structure, compositions["practical_example"])


def _scene_14_structured_prompt(context: dict[str, object]) -> dict[str, object]:
    point = context["three_key_points"][2]
    scene_bodies = context.get("scene_bodies", {})
    scene13_body = str(scene_bodies.get("scene_13", "")) if isinstance(scene_bodies, dict) else ""
    scene14_body = str(scene_bodies.get("scene_14", "")) if isinstance(scene_bodies, dict) else ""
    point_3_label = _short_label(re.sub(r"^重要ポイントの3つ目は", "", scene13_body), str(point["label"]), 14)
    scene_14_core_message = _short_label(scene14_body or str(point["core_message"]), str(point["label"]), 34)
    clauses = [c for c in re.split(r"。|、", scene14_body) if c]
    example_context_label = _short_label(next((c for c in clauses if re.search(r"例えば|たとえば|場面|時|場合|仕事|日常|相談|読書|整理|休息|お金|会議|上司|チャット", c)), scene_14_core_message), "具体場面", 12)
    action_label = _short_label(next((c for c in clauses if re.search(r"使|行|書|選|考|試|始|整理|当てはめ|見直|伝え|返", c)), scene_14_core_message), "実践する", 12)
    result_label = _short_label(next((c for c in clauses if re.search(r"でき|変わ|続|和ら|役立|分か|進|減|増|整|改善", c)), str(point["core_message"])), "変化が見える", 12)
    elements = [example_context_label, action_label, result_label]
    visual_structure = _scene_14_visual_structure(scene14_body)
    visual_metaphor = "current-script-derived metaphor for concretizing Key Point 3, such as a single use-case card, step path, before-after bridge, tool-in-hand, scenario vignette, or framework being applied"
    composition = _scene_14_composition(visual_structure)
    visual_motifs = ["原稿由来の具体場面", "3つ以内の短い日本語ラベル", "小さな実践モチーフ", "scene_13とは違う構図", "scene_18とは違う一例への絞り込み"]
    final_prompt = f"""Create a 16:9 landscape video-insert image for Book Base, a Japanese business book YouTube channel. Use a refined watercolor illustration style with a premium, calm, elegant atmosphere. Use a soft cream-white and beige background with teal and subtle gold accents. Include a small natural Book Base logo placed unobtrusively.

This is Scene 14. Its fixed role is to make Key Point 3 concrete through a practical example, usage scene, step, or application image. The image should help viewers understand how Key Point 3 works in practice. Do not create a generic meeting scene unless the current script actually requires it. Do not hard-code any topic from a previous book. Build the visual message from the current script only.

Current Key Point 3:
{point_3_label}

Current Scene 14 core message:
{scene_14_core_message}

Visual structure:
{visual_structure}

{TEXT_LOCK_INSTRUCTION}:
{_text_block(elements)}

Visual metaphor:
{visual_metaphor}

Composition:
{composition}

Visual motifs:
{', '.join(visual_motifs)}

Keep the image clean and easy to understand at a glance. Use minimal Japanese text only. Do not place long script text. Avoid clutter, avoid generic meeting scenes, avoid generic business people, avoid English text, and avoid repeating the Scene 13 composition or the later Scene 18 implementation composition."""
    return {"scene": 14, "fixed_role": "重要ポイント③の具体化", "scene_role": "重要ポイント③の具体化", "point_3_label": point_3_label, "core_message": scene_14_core_message, "scene_14_core_message": scene_14_core_message, "example_context_label": example_context_label, "action_label": action_label, "result_label": result_label, "visual_structure": visual_structure, "visual_metaphor": visual_metaphor, "exact_text_elements": elements, "composition": composition, "visual_motifs": visual_motifs, "style": _COMMON_STYLE_FOR_SCHEMA, "negative_rules": ["meetingを固定しない", "businessperson calmly respondingを固定しない", "会議や返答シーンに固定しない", "ただの人物イラストにしない", "scene_13と同じ重要ポイントカードにしない", "scene_18の全体実践シーンと混ぜない", "長文や英語テキストを入れない"], "variation_key": f"scene-14-key-point-3-concrete-{visual_structure}", "final_prompt": final_prompt}


def _scene_15_attribution_status(scene15_body: str) -> str:
    if re.search(r"NEEDS_REVIEW|未確認|出典不明|確認できない|根拠が弱い|曖昧|不確か|AIが作った", scene15_body, re.I):
        return "unverified" if re.search(r"出典不明|AIが作った|誰の言葉か不明", scene15_body) else "needs_review"
    if re.search(r"確認済み|検証済み|出典|一次資料|著作|原文|公的|公式|文献で確認|資料で確認", scene15_body):
        return "verified"
    return "needs_review"


def _scene_15_source_type(scene15_body: str, attribution_status: str) -> str:
    if attribution_status == "unverified":
        return "symbolic_only"
    if re.search(r"要約|思想|考え方|エッセンス|言い換えると|要するに", scene15_body):
        return "paraphrase"
    if re.search(r"『[^』]+』|本書|著作|書籍|一節", scene15_body):
        return "book"
    if re.search(r"名言|発言|言葉|氏|さん|人物|著者|心理学者|哲学者|経営者", scene15_body):
        return "person"
    return "paraphrase"


def _scene_15_visual_mode(attribution_status: str, quote_source_type: str) -> str:
    if attribution_status == "verified" and quote_source_type in {"person", "book", "public_domain_quote"}:
        return "named_quote"
    if attribution_status == "unverified":
        return "symbolic_quote_scene"
    return "quote_card"


def _scene_15_composition(visual_mode: str) -> str:
    compositions = {
        "named_quote": "構図D：控えめ人物＋引用型。verified の場合のみ、人物または出典は小さく控えめにし、主役は中央の引用カードにする。参照画像がない場合は実在人物の顔を正確に再現しようとせず、水彩のシルエット寄りにする。Scene 14の具体例構図とは分ける。",
        "quote_card": "構図A：引用カード型。中央に上品な quote card を置き、短い一節と lesson label を最小限で見せる。周囲に本、ノート、しおりを余白多めに配置し、人物名や顔は出さない。Scene 14の具体例画像を繰り返さない。",
        "still_life": "構図B：静物・余白型。ノート、カード、ペン、しおり、本などの still life で、短い一節が重要ポイント③を支える余韻を作る。人物や顔を出さず、長文引用も入れない。",
        "symbolic_quote_scene": "構図C：象徴場面型。光、道、扉、整う机、小さな変化を示すモチーフなどで言葉の意味を象徴する。出典が弱い前提で、人物名・顔・断定的な引用表現は使わない。",
    }
    return compositions[visual_mode]


def _scene_15_structured_prompt(context: dict[str, object]) -> dict[str, object]:
    point = context["three_key_points"][2]
    scene_bodies = context.get("scene_bodies", {})
    scene13_body = str(scene_bodies.get("scene_13", "")) if isinstance(scene_bodies, dict) else ""
    scene14_body = str(scene_bodies.get("scene_14", "")) if isinstance(scene_bodies, dict) else ""
    scene15_body = str(scene_bodies.get("scene_15", "")) if isinstance(scene_bodies, dict) else ""
    point_3_label = _short_label(re.sub(r"^重要ポイントの3つ目は", "", scene13_body), str(point["label"]), 14)
    scene_15_core_message = _short_label(scene15_body or scene14_body or str(point["core_message"]), str(point["label"]), 34)
    attribution_status = _scene_15_attribution_status(scene15_body)
    quote_source_type = _scene_15_source_type(scene15_body, attribution_status)
    source_match = re.search(r"(?:発言者|引用元|出典|著者|心理学者|哲学者|経営者)?[：:、]?\s*([一-龥ァ-ヴーA-Za-z0-9・＆&\\. ]{2,24})(?:は|が|氏|さん|の『|『)", scene15_body)
    quote_source_name = _short_label(source_match.group(1), "", 18) if source_match and attribution_status == "verified" else None
    quote_match = re.search(r"「([^」]{2,24})」", scene15_body)
    quote_excerpt_label = _short_label(quote_match.group(1) if quote_match else scene15_body, "考え方のヒント", 12)
    lesson_label = _short_label(next((c for c in re.split(r"。|、", scene15_body + scene14_body) if re.search(r"つなが|支え|補強|実践|行動|考え方|姿勢|ヒント", c)), scene_15_core_message), "実践の支え", 12)
    visual_mode = _scene_15_visual_mode(attribution_status, quote_source_type)
    if visual_mode == "named_quote":
        elements = [quote_excerpt_label[:18], str(quote_source_name or "出典確認済み")[:15], lesson_label[:15]]
    elif attribution_status == "unverified":
        elements = ["考え方のヒント", quote_excerpt_label[:18], lesson_label[:15]]
    else:
        elements = ["印象的な一節", quote_excerpt_label[:18], lesson_label[:15]]
    composition = _scene_15_composition(visual_mode)
    visual_motifs = ["短い引用カード", "本とノート", "余白", "控えめな光", "Scene 14と異なる構図"]
    final_prompt = f"""Create a 16:9 landscape video-insert image for Book Base, a Japanese business book YouTube channel. Use a refined watercolor illustration style with a premium, calm, elegant atmosphere. Use a soft cream-white and beige background with teal and subtle gold accents. Include a small natural Book Base logo placed unobtrusively.

This is Scene 15. Its fixed role is to reinforce Key Point 3 with a quotation, short excerpt, notable line, or distilled idea. The quote or idea must be based on the current script and current research. Do not hard-code any quote from a previous book. If attribution is uncertain, do not show a named person or face. Use a quote card, still-life composition, or symbolic quote scene instead.

Current Key Point 3:
{point_3_label}

Current Scene 15 core message:
{scene_15_core_message}

Quote source type:
{quote_source_type}

Attribution status:
{attribution_status}

Visual mode:
{visual_mode}

{TEXT_LOCK_INSTRUCTION}:
{_text_block(elements)}

Composition:
{composition}

Visual motifs:
{', '.join(visual_motifs)}

Keep the image clean and easy to understand at a glance. Use minimal Japanese text only. Do not place long script text. Avoid clutter, avoid long verbatim quotes, avoid invented attributions, avoid realistic faces, avoid hard-coded previous-book quotes, and avoid repeating the Scene 14 composition."""
    return {"scene": 15, "fixed_role": "重要ポイント③の引用・名言補強", "scene_role": "重要ポイント③の引用・名言補強", "point_3_label": point_3_label, "core_message": scene_15_core_message, "scene_15_core_message": scene_15_core_message, "quote_source_type": quote_source_type, "quote_source_name": quote_source_name, "quote_excerpt_label": quote_excerpt_label, "lesson_label": lesson_label, "attribution_status": attribution_status, "visual_mode": visual_mode, "exact_text_elements": elements, "composition": composition, "visual_motifs": visual_motifs, "style": _COMMON_STYLE_FOR_SCHEMA, "negative_rules": ["特定の名言を固定しない", "特定人物名を固定しない", "未確認の人物名・顔を出さない", "長文引用を入れない", "scene_14と同じ構図にしない", "英語テキストを入れない"], "variation_key": f"scene-15-quote-reinforcement-{visual_mode}", "final_prompt": final_prompt}

def _scene_12_visual_structure(scene12_body: str) -> str:
    if re.search(r"型|整理|構造|図解|ポイント|要点|流れ|比較", scene12_body):
        return "learning_diagram"
    if re.search(r"会話|伝え|相談|共有|話|コミュニケーション|やり取り|対話", scene12_body):
        return "concept_map"
    if re.search(r"本|学び|メモ|振り返|ノート", scene12_body):
        return "notebook_summary"
    return "key_point_card"


def _scene_12_composition(visual_structure: str) -> str:
    compositions = {
        "learning_diagram": "構図A：中央に本の学びを表す整理図・2〜3個の要点カードを大きく置く。コメント促しは右下の小さな吹き出しに1要素だけ添え、主役にしない。",
        "concept_map": "構図B：本の考え方を示す概念マップや関係図を主役にする。会話の雰囲気は補助線や小さな吹き出しで表し、コメント促しは端に控えめに置く。",
        "notebook_summary": "構図C：本とノートの落ち着いたデスク上に、学びの要点整理・図解ラベルを大きく見せる。コメント促しは右下の小さな付箋か吹き出しで短く添える。",
        "key_point_card": "構図D：重要ポイント②の学びをまとめた上品なカードを中央に置き、図解や要点を主役にする。コメントCTAはカード外の小さな補助エリアに1要素だけ配置する。",
    }
    return compositions.get(visual_structure, compositions["key_point_card"])


def _scene_12_learning_label(scene11_body: str, scene10_body: str, scene9_body: str) -> str:
    source = scene11_body or scene10_body or scene9_body
    for pattern in [
        r"(?:大事なのは|ポイントは|つまり|要するに|ここでの学びは)([^。！？]{2,18})",
        r"([^。！？、]{2,18}(?:整える|見直す|置き換える|伝える|受け止める|考える|選ぶ))",
        r"([^。！？、]{2,16}(?:型|習慣|視点|工夫|整理|学び|要点))",
    ]:
        match = re.search(pattern, source)
        if match:
            return _short_label(match.group(1), "学びの整理", 14)
    return _short_label(source, "学びの整理", 14)


def _scene_12_cta_label(scene12_body: str) -> str:
    candidates = ["似た経験はコメントで", "あなたならどうしますか？", "似たことありますか？", "コメントで教えてください"]
    if re.search(r"どう|なら|場合", scene12_body):
        return candidates[1]
    if re.search(r"似た|経験", scene12_body):
        return candidates[0]
    if re.search(r"ありますか", scene12_body):
        return candidates[2]
    return candidates[3]


def _scene_12_experience_label(scene12_body: str, scene10_body: str, scene9_body: str) -> str:
    question_match = re.search(r"([^。！？]*(?:経験|悩んだ|迷った|見直した|感じた|活かせた)[^。！？]*[？?])", scene12_body)
    source = question_match.group(1) if question_match else scene12_body or scene10_body or scene9_body
    source = re.sub(r"みなさんも|あなたも|仕事で|日常で|もし|似たような経験があれば|ぜひ|コメント欄で教えてください|ありますか[？?]?", "", source)
    candidates = [
        r"([^。！？、]{2,18}(?:経験|悩み|迷い|不安|見直し|工夫|失敗|改善))",
        r"([^。！？、]{2,16}(?:した|できた|感じた|迷った|悩んだ|見直した))",
    ]
    for pattern in candidates:
        match = re.search(pattern, source)
        if match:
            label = _short_label(match.group(1), "似た経験", 16)
            if not re.search(r"コメント|キーワード|一言", label):
                return label if label.endswith("経験") else f"{label}経験"[:16]
    fallback = _short_label(scene10_body or scene9_body, "似た経験", 12)
    return fallback if fallback.endswith("経験") else f"{fallback}経験"[:16]


def _scene_12_structured_prompt(context: dict[str, object]) -> dict[str, object]:
    scene_bodies = context.get("scene_bodies", {})
    scene9_body = str(scene_bodies.get("scene_09", "")) if isinstance(scene_bodies, dict) else ""
    scene10_body = str(scene_bodies.get("scene_10", "")) if isinstance(scene_bodies, dict) else ""
    scene11_body = str(scene_bodies.get("scene_11", "")) if isinstance(scene_bodies, dict) else ""
    scene12_body = str(scene_bodies.get("scene_12", "")) if isinstance(scene_bodies, dict) else ""
    comment_question_match = re.search(r"([^。！？]*(?:経験|ありますか|どうでしたか|教えてください)[^。！？]*[？?])", scene12_body)
    comment_question = comment_question_match.group(1) if comment_question_match else scene12_body
    experience_label = _scene_12_experience_label(scene12_body, scene10_body, scene9_body)
    learning_label = _scene_12_learning_label(scene11_body, scene10_body, scene9_body)
    cta_label = _scene_12_cta_label(scene12_body)
    visual_structure = _scene_12_visual_structure(" ".join([scene12_body, scene11_body, scene10_body, scene9_body]))
    composition = _scene_12_composition(visual_structure)
    elements = [learning_label, "要点整理", cta_label]
    final_prompt = f"""Create a 16:9 landscape video-insert image for Book Base, a Japanese business book YouTube channel. Use a refined watercolor illustration style with a premium, calm, elegant atmosphere. Use a soft cream-white and beige background with teal and subtle gold accents. Include a small natural Book Base logo placed unobtrusively.

This is Scene 12. Its fixed role is a comment CTA, but the CTA must not be the main subject. Make the book's learning, key idea, diagram, and conceptual summary from Scenes 09-11 the visual focus. Add the comment prompt only as one small supporting Japanese text element in a lower-corner speech bubble or small auxiliary area. Do not hard-code any topic from a previous book. Build all labels from the current script only.

Current comment question:
{comment_question}

Learning label:
{learning_label}

Comment CTA label:
{cta_label}

Use only the following Japanese text elements exactly as written. The first two are main learning/diagram text; the comment CTA is the final single small supporting element. Do not add any other Japanese or English text:
{_text_block(elements)}

Visual structure:
{visual_structure}

Composition:
{composition}

Visual motifs:
- book learning diagram
- key point summary cards
- concept map or notebook labels
- small lower-corner speech bubble for the CTA
- calm desk setup
- enough whitespace
- premium watercolor texture

Keep the image clean and easy to understand at a glance. Use minimal Japanese text only. Do not place long script text. Avoid English text, avoid keyword-comment prompts, avoid making the comment CTA the main subject, avoid the fixed three-part CTA set, avoid aggressive CTA design, avoid clutter, and avoid repeating the Scene 08 subscription CTA composition."""
    return {"scene": 12, "fixed_role": "コメントCTA", "scene_role": "本の学びを主役にしたコメントCTA", "current_theme": str(context.get("current_theme", "現在の動画テーマ")), "comment_question": comment_question, "experience_label": experience_label, "learning_label": learning_label, "cta_label": cta_label, "visual_structure": visual_structure, "exact_text_elements": elements, "composition": composition, "visual_motifs": ["book learning diagram", "key point summary cards", "concept map or notebook labels", "small lower-corner speech bubble for the CTA", "calm desk setup", "enough whitespace", "premium watercolor texture"], "style": _COMMON_STYLE_FOR_SCHEMA, "negative_rules": ["英語テキストを入れない", "Similar experience?を入れない", "Subscribe風にしない", "キーワード型コメント促しにしない", "長文コメント文を入れない", "コメントCTAを主役にしない", "あなたの経験は？・experience_label・コメントで教えてくださいの3点セットを固定しない", "scene_08の登録CTA構図を繰り返さない"], "variation_key": f"scene-12-learning-first-comment-cta-{visual_structure}", "core_message": learning_label, "final_prompt": final_prompt}


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
        "固定役割：メリットや前向きな変化を直感的に伝えるBook BaseのYouTubeサムネイル",
        "コメント：仕事が軽くなる思考法",
        "benefit_trigger_label：この本の学びで仕事や考え方が軽くなり、実務に前向きな改善が起こりそうという期待",
        "benefit_style：intelligent_simplicity",
        "visual_structure：desk_layout_cover_focus",
        "exact_text_elements：仕事が軽くなる思考法（1要素のみ）",
        f"狙い：{book_name}から得られる前向きな変化を、仕事改善のベネフィットとして伝える。",
        "出力ファイル名：thumbnail_B_benefit.png",
        f"使用画像：{cover_path}",
        f"needs_review：{needs_review}",
        "",
        "Pattern C：",
        "方向性：逆張り・好奇心型",
        "固定役割：逆張り・意外性・好奇心を刺激するBook BaseのYouTubeサムネイル",
        "コメント：考える前に整える",
        "curiosity_trigger_label：考えるより先に整えるという一見矛盾した順序に、意味を知りたくなる知的な違和感",
        "contrarian_angle_label：よく考えれば解決するという思い込みを少しずらす",
        "curiosity_style：subtle_contradiction",
        "visual_structure：unexpected_split_layout",
        "exact_text_elements：考える前に整える（1要素のみ）",
        f"狙い：{book_name}の主張を、普通の努力論とは違う意外性のある入口に変換し、危機感や直球ベネフィットではなく意味を知りたい好奇心で引く。",
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
        ("Pattern B", "thumbnail_B_benefit.png", "誘惑・ベネフィット型", "仕事が軽くなる思考法", "thumbnail pattern B benefit, fixed role: communicate the positive benefit viewers may gain from the book, benefit_trigger_label: work and thinking may become lighter and clearer, benefit_style: intelligent_simplicity, visual_structure: desk_layout_cover_focus, large current book cover as key visual, one exact Japanese text element only, bright aspirational desk layout, calm structured whitespace, avoid cheap self-help design and overhyped success imagery"),
        ("Pattern C", "thumbnail_C_curiosity.png", "逆張り・好奇心型", "考える前に整える", "thumbnail pattern C contrarian curiosity, fixed role: trigger curiosity through an unexpected or slightly contrarian idea, curiosity_trigger_label: intellectual discomfort that makes viewers wonder why preparation comes before thinking, contrarian_angle_label: shift the assumption that thinking harder comes first, curiosity_style: subtle_contradiction, visual_structure: unexpected_split_layout, large current book cover as key visual, one exact Japanese text element only, curiosity-driven unexpected layout, calm structured whitespace, subtle intellectual surprise, avoid meaningless quirky design, cheap clickbait, warning tension, and straightforward benefit appeal"),
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
            "verification_status：needs_review",
            "visual_mode：symbolic_action",
            "画像内人物名・企業名：verification_status が verified の場合のみ使用可。",
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
            "fixed_role：重要ポイント③の引用・名言補強",
            "point_3_label：未確定。原稿生成後に重要ポイント③から抽出します。",
            "scene_15_core_message：未確定。scene_15本文と調査結果から抽出します。",
            "quote_source_type：symbolic_only",
            "quote_source_name：null",
            "quote_excerpt_label：未確定。画像内は短い引用句または要約句だけにします。",
            "lesson_label：未確定。重要ポイント③とのつながりを短く表します。",
            "attribution_status：needs_review",
            "visual_mode：quote_card",
            "確認した出典：未取得。誤引用の可能性を確認後に attribution_status を verified / needs_review / unverified で更新してください。",
            "画像生成時の表現方針：verified でない場合は人物名・顔を出さず、quote card / still-life / symbolic composition で表現します。長い引用文や過去テーマの固定名言は使いません。",
            f"自動取得ステータス：{status}",
        ]
    ) + "\n"


def _scene_19_connection_type(current_text: str, related_text: str) -> str:
    combined = f"{current_text} {related_text}"
    if re.search(r"お金|資産|投資|家計|生活設計|人生設計|将来", combined):
        return "money_or_life_application"
    if re.search(r"一方|逆|対比|やめる|続ける|休み|頑張", combined):
        return "contrast_and_deepen"
    if re.search(r"実践|応用|仕事|生活|日常|習慣|行動", combined):
        return "practical_extension"
    if re.search(r"次|さらに|深ま|広が|進め|つな", combined):
        return "next_step"
    return "same_theme"


def _scene_19_visual_structure(connection_type: str) -> str:
    mapping = {
        "same_theme": "book_bridge",
        "next_step": "light_path",
        "practical_extension": "flowing_pages",
        "contrast_and_deepen": "ribbon_connection",
        "money_or_life_application": "two_books_perspective",
    }
    return mapping.get(connection_type, "book_bridge")


def _scene_19_composition(visual_structure: str) -> str:
    mapping = {
        "book_bridge": "構図A：左側に今回の本、右側に過去動画の本を置き、2冊の間を柔らかく光る橋でつなぐ。学びの橋渡しを自然に見せ、商品広告の横並びにはしない。",
        "light_path": "構図A：現在の本から過去動画の本へ、淡い光の道が続く。次の学びへ自然に進む印象にし、強い矢印やクリック誘導は使わない。",
        "flowing_pages": "構図B：今回の本のページから光や紙片が流れて別の本へつながる。本から本へ学びが広がる印象を出し、説明文で埋めない。",
        "ribbon_connection": "構図D：2冊の本を細いリボンややわらかな線で控えめにつなぐ。広告感を抑え、上品でミニマルな関連性を見せる。",
        "two_books_perspective": "構図C：手前に今回の本、奥に関連する過去動画の本を置き、淡い線や光で奥行きのある関係性を見せる。締めの余韻ではなく接続を主役にする。",
    }
    return mapping.get(visual_structure, mapping["book_bridge"])


def _scene_19_structured_prompt(context: dict[str, object]) -> dict[str, object]:
    scene_bodies = context.get("scene_bodies", {})
    scene18_body = str(scene_bodies.get("scene_18", "")) if isinstance(scene_bodies, dict) else ""
    current_label = _short_label(str(context.get("current_theme", "")) or scene18_body, "今回の学び", 12)
    related_source = str(context.get("source_text", ""))
    related_section = related_source.split("# scene_19_related", 1)[-1] if "# scene_19_related" in related_source else related_source
    related_label = _short_label(related_section, "関連する学び", 12)
    connection_type = _scene_19_connection_type(current_label + scene18_body, related_label + related_section)
    visual_structure = _scene_19_visual_structure(connection_type)
    composition = _scene_19_composition(visual_structure)
    connection_reason = _short_label(f"{current_label}から{related_label}へ理解が広がる", "学びが自然につながる", 28)
    message_by_type = {
        "same_theme": "理解が深まる",
        "next_step": "次の一冊へ",
        "practical_extension": "学びがつながる",
        "contrast_and_deepen": "理解が深まる",
        "money_or_life_application": "学びがつながる",
    }
    connection_message = message_by_type.get(connection_type, "学びがつながる")
    current_cover = context["assets"].get("book_cover") if isinstance(context.get("assets"), dict) else None
    related_cover = context["assets"].get("related_book_cover") if isinstance(context.get("assets"), dict) else None
    elements = [connection_message]
    final_prompt = f"""Create a 16:9 landscape video-insert image for Book Base, a Japanese business book YouTube channel. Use a refined watercolor illustration style with a premium, calm, elegant, sophisticated atmosphere. Use a soft cream-white and beige background with teal and subtle gold accents. Include a small natural Book Base logo placed unobtrusively.

This is Scene 19. Its fixed role is to naturally connect the current book with a related book from a past video. The image should communicate continuity of learning, broader understanding, and a gentle path toward the next related learning. It must not look like a simple advertisement, a clickbait banner, or a product promotion. Do not make it a closing or thank-you scene like Scene 20.

Use the reference image as the current book cover:
{current_cover or 'current book cover reference unavailable'}

Use the related past-video book cover as the second book when available:
{related_cover or 'related book cover reference unavailable'}

Current book label:
{current_label}

Related past-video book label:
{related_label}

Connection reason:
{connection_reason}

Connection type:
{connection_type}

Visual structure:
{visual_structure}

{TEXT_LOCK_INSTRUCTION}:
{_text_block(elements)}

Composition:
{composition}

Visual motifs:
- two books connected naturally
- softly glowing bridge, light path, flowing pages, or subtle ribbon
- calm structured whitespace
- premium watercolor texture
- gentle teal and subtle gold accents
- sophisticated and inviting atmosphere

Keep the image clean and easy to understand at a glance. Use minimal Japanese text only. Do not place long script text. Avoid clutter, avoid English text, avoid advertisement-like design, avoid clickbait CTA, avoid excessive arrows, and avoid making the two books look unrelated."""
    return {"scene": 19, "fixed_role": "現在の本と関連過去動画の本を自然につなぐ接続シーン", "scene_role": "現在の本と関連過去動画の本を自然につなぐ接続シーン", "current_book_label": current_label, "related_book_label": related_label, "connection_reason": connection_reason, "connection_message": connection_message, "connection_type": connection_type, "visual_structure": visual_structure, "reference_image_path": current_cover, "related_book_cover_path": related_cover, "exact_text_elements": elements, "composition": composition, "visual_motifs": ["two books connected naturally", "softly glowing bridge", "light path", "flowing pages", "subtle ribbon", "calm structured whitespace"], "style": _COMMON_STYLE_FOR_SCHEMA, "negative_rules": ["CTA文を入れない", "広告バナー風にしない", "2冊をただ横に並べない", "参照画像だけを大きく表示しない", "過去動画側の本を省略しない", "英語テキストを入れない", "scene_20の締め画像にしない"], "variation_key": f"scene-19-learning-connection-{visual_structure}", "core_message": connection_message, "final_prompt": final_prompt}


def _scene_20_closing_emotion(text: str) -> str:
    if re.search(r"ありがとう|感謝|見てくれ|ご視聴", text):
        return "appreciative"
    if re.search(r"明日|一歩|前|変え|始め|進", text):
        return "hopeful"
    if re.search(r"振り返|考え|内省|重ね|見つめ", text):
        return "reflective"
    if re.search(r"静か|落ち着|余韻|受け止め", text):
        return "serene"
    return "warm"


def _scene_20_closing_type(text: str, emotion: str) -> str:
    if emotion == "appreciative":
        return "warm_thank_you"
    if re.search(r"次の一冊|次回|また", text):
        return "next_book_invitation"
    if re.search(r"持ち帰|日常|明日|活か|行動", text):
        return "learning_takeaway"
    if emotion in {"serene", "reflective"}:
        return "quiet_reflection"
    return "gentle_finish"


def _scene_20_visual_structure(emotion: str, closing_type: str) -> str:
    if closing_type == "next_book_invitation":
        return "window_light"
    if closing_type == "learning_takeaway":
        return "calm_tabletop"
    if closing_type == "quiet_reflection":
        return "home_office_wide"
    if emotion == "appreciative":
        return "hand_and_book"
    return "closing_book"


def _scene_20_composition(visual_structure: str) -> str:
    mapping = {
        "closing_book": "構図A：静かなホームオフィスで、やさしく本を閉じる手元を中心に描く。一冊を読み終えた読後感を見せ、作業中や実践途中の雰囲気にはしない。",
        "quiet_desk": "構図B：人物を大きく出さず、整った机に本・ノート・ペンを余白多めに置く。学びを静かに受け取った後の余韻を中心にする。",
        "window_light": "構図B：窓からやわらかい朝の光が入り、机上の本とノートを包む。明日への前向きさを穏やかに出し、CTAや誘導表現にはしない。",
        "hand_and_book": "構図A：手元と本を近めに見せ、読み終えた本にそっと触れる温度感を描く。感謝と余韻を主役にし、長い文字や広告風レイアウトを避ける。",
        "home_office_wide": "構図D：静かなホームオフィス全体を少し引いて見せ、机・窓辺・本を上品な余白で配置する。関連動画接続や2冊の本の導線は入れない。",
        "calm_tabletop": "構図C：本、ペン、ノート、コーヒーを俯瞰で静物画のように置き、余白と水彩の質感で締めの空気を表現する。チェックリスト中心の実践画像にしない。",
    }
    return mapping.get(visual_structure, mapping["closing_book"])


def _scene_20_supporting_objects(visual_structure: str) -> list[str]:
    mapping = {
        "closing_book": ["本", "ノート", "ペン", "やわらかい朝の光"],
        "quiet_desk": ["本", "ノート", "ペン", "小さなコーヒーカップ"],
        "window_light": ["窓辺", "本", "ノート", "コーヒー"],
        "hand_and_book": ["本を閉じる手元", "整った机", "ペン", "淡い金色の光"],
        "home_office_wide": ["静かなホームオフィス", "窓辺", "本", "整った机"],
        "calm_tabletop": ["本", "ノート", "ペン", "コーヒー", "余白"],
    }
    return mapping.get(visual_structure, mapping["closing_book"])


def _scene_20_closing_text(final_message_label: str, closing_type: str) -> str:
    if 4 <= len(final_message_label) <= 16 and not re.search(r"登録|高評価|クリック|関連動画|見てください|さん|『|』", final_message_label):
        return final_message_label
    by_type = {
        "learning_takeaway": "学びを、日常へ",
        "next_book_invitation": "また次の一冊で",
        "quiet_reflection": "今日の学びを明日へ",
        "warm_thank_you": "今日の学びを明日へ",
        "gentle_finish": "学びを、日常へ",
    }
    return by_type.get(closing_type, "学びを、日常へ")


def _scene_20_final_message_label(scene20_body: str, context: dict[str, object]) -> str:
    label = _short_label(scene20_body or str(context.get("current_theme", "")), "学びを、日常へ", 16)
    book_title = str(context.get("book_title", ""))
    if book_title:
        label = label.replace(book_title, "")
    label = re.sub(r"登録|高評価|クリック|関連動画|見てください|ご視聴|ありがとう|さん|『|』", "", label).strip("。,.、")
    if len(label) < 4:
        return "学びを、日常へ"
    return label[:16]


def _scene_20_structured_prompt(context: dict[str, object]) -> dict[str, object]:
    scene_bodies = context.get("scene_bodies", {})
    scene20_body = str(scene_bodies.get("scene_20", "")) if isinstance(scene_bodies, dict) else ""
    final_message_label = _scene_20_final_message_label(scene20_body, context)
    closing_emotion = _scene_20_closing_emotion(scene20_body)
    viewer_aftertaste_label = _short_label(scene20_body, "温かい余韻", 12)
    closing_type = _scene_20_closing_type(scene20_body, closing_emotion)
    visual_structure = _scene_20_visual_structure(closing_emotion, closing_type)
    supporting_objects = _scene_20_supporting_objects(visual_structure)
    closing_text = _scene_20_closing_text(final_message_label, closing_type)
    elements = [closing_text]
    composition = _scene_20_composition(visual_structure)
    final_prompt = f"""Create a 16:9 landscape video-insert image for Book Base, a Japanese business book YouTube channel. Use a refined watercolor illustration style with a premium, calm, warm, elegant atmosphere. Use a soft cream-white and beige background with teal and subtle gold accents. Include a small natural Book Base logo placed unobtrusively.

This is Scene 20. Its fixed role is to close the video warmly and leave viewers with a calm aftertaste, appreciation, and a positive feeling. The image should feel like the quiet moment after finishing a meaningful book. It must not become a recap scene, a practical work scene, a related-video promotion, or a CTA banner.

Final message:
{final_message_label}

Closing emotion:
{closing_emotion}

Viewer aftertaste:
{viewer_aftertaste_label}

Closing type:
{closing_type}

Visual structure:
{visual_structure}

Supporting objects:
{', '.join(supporting_objects)}

{TEXT_LOCK_INSTRUCTION}:
{_text_block(elements)}

Composition:
{composition}

Visual motifs:
- a gentle hand closing a book
- quiet home office
- soft morning light
- calm desk with a book, notebook, pen, or coffee
- serene and appreciative mood
- warm cream and subtle gold tones
- premium watercolor texture
- calm structured whitespace

Keep the image clean, warm, and easy to understand at a glance. Use minimal Japanese text only. Do not place long script text. Avoid clutter, avoid English text, avoid CTA wording, avoid advertisement-like design, avoid related-video connection motifs, and avoid turning the image into a recap or practical work scene."""
    return {"scene": 20, "fixed_role": "動画全体を温かく締めるクロージングシーン", "scene_role": "動画全体を温かく締めるクロージングシーン", "final_message_label": final_message_label, "closing_emotion": closing_emotion, "viewer_aftertaste_label": viewer_aftertaste_label, "closing_type": closing_type, "visual_structure": visual_structure, "supporting_objects": supporting_objects, "exact_text_elements": elements, "composition": composition, "visual_motifs": ["a gentle hand closing a book", "quiet home office", "soft morning light", "calm desk with a book, notebook, pen, or coffee", "serene and appreciative mood", "warm cream and subtle gold tones", "premium watercolor texture", "calm structured whitespace"], "style": _COMMON_STYLE_FOR_SCHEMA, "negative_rules": ["3つのポイントをまとめる構図にしない", "チェックリストやタスクカード中心にしない", "過去動画接続や2冊の本を入れない", "CTA文を入れない", "広告バナー風にしない", "英語テキストを入れない", "長文や指定外テキストを入れない"], "variation_key": f"scene-20-closing-{closing_type}-{visual_structure}", "core_message": final_message_label, "final_prompt": final_prompt}

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
        role_map = {9: "重要ポイント2の導入", 10: "重要ポイント2の具体化", 11: "重要ポイント2の実話エピソード補強", 12: "重要ポイント2の締め＋コメント促し"}
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
    scene_08_prompt = _scene_08_structured_prompt(context) if scene == 8 else None
    scene_09_prompt = _scene_09_structured_prompt(context) if scene == 9 else None
    scene_10_prompt = _scene_10_structured_prompt(context) if scene == 10 else None
    scene_11_prompt = _scene_11_structured_prompt(context) if scene == 11 else None
    scene_12_prompt = _scene_12_structured_prompt(context) if scene == 12 else None
    scene_13_prompt = _scene_13_structured_prompt(context) if scene == 13 else None
    scene_14_prompt = _scene_14_structured_prompt(context) if scene == 14 else None
    scene_15_prompt = _scene_15_structured_prompt(context) if scene == 15 else None
    scene_16_prompt = _scene_16_structured_prompt(context) if scene == 16 else None
    scene_17_prompt = _scene_17_structured_prompt(context) if scene == 17 else None
    scene_18_prompt = _scene_18_structured_prompt(context) if scene == 18 else None
    scene_19_prompt = _scene_19_structured_prompt(context) if scene == 19 else None
    scene_20_prompt = _scene_20_structured_prompt(context) if scene == 20 else None
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
        asset_note = "scene_15は原稿生成後に重要ポイント③を補強する引用・一節・思想要約を抽出し、attribution_statusがverifiedの場合のみ人物名や出典名を限定的に反映します。verifiedでない場合は人物名・顔を出さず、引用カード・静物構図・象徴構図で代替します。"
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
    elif scene_08_prompt:
        purpose = str(scene_08_prompt["scene_role"])
        text = " / ".join(scene_08_prompt["exact_text_elements"])
        differentiation = "scene_07の資料・グラフ・レポート構図から、上品な登録カード中心のCTA構図へ変える"
        prompt = str(scene_08_prompt["final_prompt"])
        recommended_composition = str(scene_08_prompt["composition"])
    elif scene_09_prompt:
        purpose = str(scene_09_prompt["scene_role"])
        text = " / ".join(scene_09_prompt["exact_text_elements"])
        differentiation = "scene_08のCTA構図から本編へ戻り、scene_05の重要ポイント①導入とは異なる第2ポイント導入構図へ変える"
        prompt = str(scene_09_prompt["final_prompt"])
        recommended_composition = str(scene_09_prompt["composition"])
    elif scene_10_prompt:
        purpose = str(scene_10_prompt["scene_role"])
        text = " / ".join(scene_10_prompt["exact_text_elements"])
        differentiation = "scene_09の重要ポイント②導入カードから、原稿由来の具体例・手順・比較・実践イメージへ構図を変える"
        prompt = str(scene_10_prompt["final_prompt"])
        recommended_composition = str(scene_10_prompt["composition"])
    elif scene_11_prompt:
        purpose = str(scene_11_prompt["scene_role"])
        text = " / ".join(scene_11_prompt["exact_text_elements"])
        differentiation = "scene_10の具体化構図から、実話エピソードカードまたは象徴的な行動シーンへ変える"
        prompt = str(scene_11_prompt["final_prompt"])
        recommended_composition = str(scene_11_prompt["composition"])
    elif scene_12_prompt:
        purpose = str(scene_12_prompt["scene_role"])
        text = " / ".join(scene_12_prompt["exact_text_elements"])
        differentiation = "scene_11の実話エピソード補強から、コメント欄への自然な参加を促すCTA構図へ変える。scene_08の登録CTAとは混同させない"
        prompt = str(scene_12_prompt["final_prompt"])
        recommended_composition = str(scene_12_prompt["composition"])
    elif scene_13_prompt:
        purpose = str(scene_13_prompt["scene_role"])
        text = " / ".join(scene_13_prompt["exact_text_elements"])
        differentiation = "scene_12のコメントCTAから本編へ戻り、scene_09の重要ポイント②導入やscene_18の実践画像と混ざらない第3ポイント導入構図へ変える"
        prompt = str(scene_13_prompt["final_prompt"])
        recommended_composition = str(scene_13_prompt["composition"])
    elif scene_14_prompt:
        purpose = str(scene_14_prompt["scene_role"])
        text = " / ".join(scene_14_prompt["exact_text_elements"])
        differentiation = "scene_13の重要ポイント③導入から、原稿由来の具体例・使い方・手順に一段具体化する。scene_18の全体実践画像とは混ぜない"
        prompt = str(scene_14_prompt["final_prompt"])
        recommended_composition = str(scene_14_prompt["composition"])
    elif scene_15_prompt:
        purpose = str(scene_15_prompt["scene_role"])
        text = " / ".join(scene_15_prompt["exact_text_elements"])
        differentiation = "scene_14の重要ポイント③具体例から、引用・一節・思想要約で補強するカード／静物／象徴構図へ変える"
        prompt = str(scene_15_prompt["final_prompt"])
        recommended_composition = str(scene_15_prompt["composition"])
    elif scene_16_prompt:
        purpose = str(scene_16_prompt["scene_role"])
        text = " / ".join(scene_16_prompt["exact_text_elements"])
        differentiation = "scene_03の本紹介・大きな表紙構図ではなく、読書の余韻と残りの価値を伝える控えめな案内構図へ変える"
        prompt = str(scene_16_prompt["final_prompt"])
        recommended_composition = str(scene_16_prompt["composition"])
        asset_note = "実ブックカバーを使う場合は後処理で控えめに合成し、AIには表紙を描かせません。" if scene_16_prompt["visual_mode"] == "real_cover_composite" else "実ブックカバーを使わず、タイトルのない一般的な本・開いた本・読書机で表現します。"
    elif scene_17_prompt:
        purpose = str(scene_17_prompt["scene_role"])
        text = " / ".join(scene_17_prompt["exact_text_elements"])
        differentiation = "scene_04のこれから話す予告構図ではなく、3ポイントを学び終えた後の総整理・到達感のある流れ構図へ変える。scene_20の締め挨拶とも混ぜない"
        prompt = str(scene_17_prompt["final_prompt"])
        recommended_composition = str(scene_17_prompt["composition"])
    elif scene_18_prompt:
        purpose = str(scene_18_prompt["scene_role"])
        text = " / ".join(scene_18_prompt["exact_text_elements"])
        differentiation = "scene_17の総整理から、手を動かして本の学びを仕事や日常へ移す実践途中の構図へ変える。scene_20の締めの余韻とも混ぜない"
        prompt = str(scene_18_prompt["final_prompt"])
        recommended_composition = str(scene_18_prompt["composition"])
    elif scene_19_prompt:
        purpose = str(scene_19_prompt["scene_role"])
        text = " / ".join(scene_19_prompt["exact_text_elements"])
        differentiation = "scene_18の実践化から、今回の本と過去動画の本をつなぐ接続シーンへ変える。scene_20の締め挨拶や広告CTAとは混ぜない"
        prompt = str(scene_19_prompt["final_prompt"])
        recommended_composition = str(scene_19_prompt["composition"])
        asset_note = "scene_19では今回の本の表紙を現在の本として扱い、関連過去動画の本も省略せず2冊の接続を描きます。" if used_image != "なし" else "scene_19：NEEDS_REVIEW。理由：関連過去動画側の本のブックカバーが見つかりません。2冊目を省略せず、入力確認後に生成してください。"
    elif scene_20_prompt:
        purpose = str(scene_20_prompt["scene_role"])
        text = " / ".join(scene_20_prompt["exact_text_elements"])
        differentiation = "scene_19の関連動画接続から、1冊の本・手元・静かな机・窓辺の光で動画全体を温かく締めるクロージング構図へ変える。scene_18の実践途中とも混ぜない"
        prompt = str(scene_20_prompt["final_prompt"])
        recommended_composition = str(scene_20_prompt["composition"])
    else:
        recommended_composition = composition_by_point[point]
        prompt = (
            "16:9 watercolor illustration for a premium Japanese business book YouTube channel, "
            "soft cream white beige teal and gold palette, small natural Book Base logo in the upper-right or lower-right, "
            f"scene {scene}, {meta['所属ブロック']}, {meta['ブロック内での役割']}, "
            f"{recommended_composition}, no long text, one clear message, avoid repeating adjacent composition"
        )
    structured_prompt = scene_01_prompt or scene_02_prompt or scene_03_prompt or scene_04_prompt or scene_05_prompt or scene_06_prompt or scene_07_prompt or scene_08_prompt or scene_09_prompt or scene_10_prompt or scene_11_prompt or scene_12_prompt or scene_13_prompt or scene_14_prompt or scene_15_prompt or scene_16_prompt or scene_17_prompt or scene_18_prompt or scene_19_prompt or scene_20_prompt
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
        "最終プロンプト": prompt + (f", reference image: {used_image}, asset note: {asset_note}" if scene not in {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19} else ""),
        "scene": scene,
        "prompt": prompt,
        "scene_role": structured_prompt["scene_role"] if structured_prompt else meta["ブロック内での役割"],
        "core_message": structured_prompt["core_message"] if structured_prompt else "現在のシーン原稿から最も重要な要点を1つだけ抽出する",
        "exact_text_elements": structured_prompt["exact_text_elements"] if structured_prompt else [text],
        "composition": structured_prompt["composition"] if structured_prompt else recommended_composition,
        "visual_motifs": structured_prompt["visual_motifs"] if structured_prompt else [recommended_composition],
        "style": structured_prompt["style"] if structured_prompt else _COMMON_STYLE_FOR_SCHEMA,
        "negative_rules": structured_prompt["negative_rules"] if structured_prompt else ["長文を入れない", "指定外の文字を入れない", "前後シーンと同じ構図にしない"],
        "variation_key": structured_prompt["variation_key"] if structured_prompt else differentiation,
        "final_prompt": prompt,
        **({"reference_image_required": scene_03_prompt["reference_image_required"], "reference_image_path": scene_03_prompt["reference_image_path"], "post_process": scene_03_prompt["post_process"]} if scene_03_prompt else {}),
        **({"reference_image_required": scene_04_prompt["reference_image_required"], "reference_image_path": scene_04_prompt["reference_image_path"], "reference_image_usage": scene_04_prompt["reference_image_usage"]} if scene_04_prompt else {}),
        **({"fixed_role": scene_06_prompt["fixed_role"], "point_1_label": scene_06_prompt["point_1_label"], "scene_06_core_message": scene_06_prompt["scene_06_core_message"], "reason_label": scene_06_prompt["reason_label"], "mechanism_label": scene_06_prompt["mechanism_label"], "effect_label": scene_06_prompt["effect_label"], "visual_metaphor": scene_06_prompt["visual_metaphor"], "visual_structure": scene_06_prompt["visual_structure"]} if scene_06_prompt else {}),
        **({"fixed_role": scene_07_prompt["fixed_role"], "point_1_label": scene_07_prompt["point_1_label"], "scene_07_core_message": scene_07_prompt["scene_07_core_message"], "evidence_type": scene_07_prompt["evidence_type"], "evidence_label": scene_07_prompt["evidence_label"], "key_finding_label": scene_07_prompt["key_finding_label"], "source_confidence": scene_07_prompt["source_confidence"], "visual_structure": scene_07_prompt["visual_structure"]} if scene_07_prompt else {}),
        **({"fixed_role": scene_08_prompt["fixed_role"], "cta_tone": scene_08_prompt["cta_tone"]} if scene_08_prompt else {}),
        **({"fixed_role": scene_09_prompt["fixed_role"], "point_2_label": scene_09_prompt["point_2_label"], "point_2_core_message": scene_09_prompt["point_2_core_message"], "point_2_type": scene_09_prompt["point_2_type"], "visual_metaphor": scene_09_prompt["visual_metaphor"]} if scene_09_prompt else {}),
        **({"fixed_role": scene_10_prompt["fixed_role"], "point_2_label": scene_10_prompt["point_2_label"], "scene_10_core_message": scene_10_prompt["scene_10_core_message"], "example_label": scene_10_prompt["example_label"], "application_label": scene_10_prompt["application_label"], "result_label": scene_10_prompt["result_label"], "visual_structure": scene_10_prompt["visual_structure"], "visual_metaphor": scene_10_prompt["visual_metaphor"]} if scene_10_prompt else {}),
        **({"fixed_role": scene_11_prompt["fixed_role"], "point_2_label": scene_11_prompt["point_2_label"], "scene_11_core_message": scene_11_prompt["scene_11_core_message"], "episode_type": scene_11_prompt["episode_type"], "episode_name": scene_11_prompt["episode_name"], "episode_role_label": scene_11_prompt["episode_role_label"], "episode_action_label": scene_11_prompt["episode_action_label"], "lesson_label": scene_11_prompt["lesson_label"], "verification_status": scene_11_prompt["verification_status"], "visual_mode": scene_11_prompt["visual_mode"]} if scene_11_prompt else {}),
        **({"fixed_role": scene_12_prompt["fixed_role"], "current_theme": scene_12_prompt["current_theme"], "comment_question": scene_12_prompt["comment_question"], "experience_label": scene_12_prompt["experience_label"], "learning_label": scene_12_prompt["learning_label"], "cta_label": scene_12_prompt["cta_label"], "visual_structure": scene_12_prompt["visual_structure"]} if scene_12_prompt else {}),
        **({"fixed_role": scene_13_prompt["fixed_role"], "point_3_label": scene_13_prompt["point_3_label"], "point_3_core_message": scene_13_prompt["point_3_core_message"], "point_3_type": scene_13_prompt["point_3_type"], "visual_metaphor": scene_13_prompt["visual_metaphor"]} if scene_13_prompt else {}),
        **({"fixed_role": scene_14_prompt["fixed_role"], "point_3_label": scene_14_prompt["point_3_label"], "scene_14_core_message": scene_14_prompt["scene_14_core_message"], "example_context_label": scene_14_prompt["example_context_label"], "action_label": scene_14_prompt["action_label"], "result_label": scene_14_prompt["result_label"], "visual_structure": scene_14_prompt["visual_structure"], "visual_metaphor": scene_14_prompt["visual_metaphor"]} if scene_14_prompt else {}),
        **({"fixed_role": scene_15_prompt["fixed_role"], "point_3_label": scene_15_prompt["point_3_label"], "scene_15_core_message": scene_15_prompt["scene_15_core_message"], "quote_source_type": scene_15_prompt["quote_source_type"], "quote_source_name": scene_15_prompt["quote_source_name"], "quote_excerpt_label": scene_15_prompt["quote_excerpt_label"], "lesson_label": scene_15_prompt["lesson_label"], "attribution_status": scene_15_prompt["attribution_status"], "visual_mode": scene_15_prompt["visual_mode"]} if scene_15_prompt else {}),
        **({"fixed_role": scene_16_prompt["fixed_role"], "book_title": scene_16_prompt["book_title"], "book_cover_path": scene_16_prompt["book_cover_path"], "remaining_value_label": scene_16_prompt["remaining_value_label"], "read_invitation_label": scene_16_prompt["read_invitation_label"], "visual_mode": scene_16_prompt["visual_mode"], "post_process": scene_16_prompt["post_process"]} if scene_16_prompt else {}),
        **({"fixed_role": scene_17_prompt["fixed_role"], "point_1_label": scene_17_prompt["point_1_label"], "point_2_label": scene_17_prompt["point_2_label"], "point_3_label": scene_17_prompt["point_3_label"], "overall_takeaway_label": scene_17_prompt["overall_takeaway_label"], "point_relationship": scene_17_prompt["point_relationship"], "visual_structure": scene_17_prompt["visual_structure"]} if scene_17_prompt else {}),
        **({"fixed_role": scene_18_prompt["fixed_role"], "practice_theme_label": scene_18_prompt["practice_theme_label"], "application_context": scene_18_prompt["application_context"], "practice_action_label": scene_18_prompt["practice_action_label"], "viewer_takeaway_label": scene_18_prompt["viewer_takeaway_label"], "practice_type": scene_18_prompt["practice_type"], "visual_structure": scene_18_prompt["visual_structure"], "supporting_objects": scene_18_prompt["supporting_objects"]} if scene_18_prompt else {}),
        **({"fixed_role": scene_19_prompt["fixed_role"], "current_book_label": scene_19_prompt["current_book_label"], "related_book_label": scene_19_prompt["related_book_label"], "connection_reason": scene_19_prompt["connection_reason"], "connection_message": scene_19_prompt["connection_message"], "connection_type": scene_19_prompt["connection_type"], "visual_structure": scene_19_prompt["visual_structure"], "reference_image_path": scene_19_prompt["reference_image_path"], "related_book_cover_path": scene_19_prompt["related_book_cover_path"]} if scene_19_prompt else {}),
        **({"fixed_role": scene_20_prompt["fixed_role"], "final_message_label": scene_20_prompt["final_message_label"], "closing_emotion": scene_20_prompt["closing_emotion"], "viewer_aftertaste_label": scene_20_prompt["viewer_aftertaste_label"], "closing_type": scene_20_prompt["closing_type"], "visual_structure": scene_20_prompt["visual_structure"], "supporting_objects": scene_20_prompt["supporting_objects"]} if scene_20_prompt else {}),
    }




def _scene_18_application_context(scene18_body: str) -> str:
    if re.search(r"仕事|職場|会議|上司|部下|資料|タスク|納期|評価|実務|報連相", scene18_body):
        if re.search(r"日常|生活|家庭|朝|毎日|習慣|暮らし", scene18_body):
            return "both"
        return "work"
    if re.search(r"日常|生活|家庭|朝|毎日|習慣|暮らし", scene18_body):
        return "daily_life"
    return "both"


def _scene_18_practice_type(scene18_body: str) -> str:
    patterns = [
        ("communication", r"伝え|言い換|話|聞く|相手|会話|相談|説明|コミュニケーション"),
        ("emotional_control", r"不安|怒り|焦り|ストレス|落ち着|気持ち|余裕|リセット"),
        ("decision_making", r"判断|選ぶ|迷い|基準|決め|意思決定"),
        ("habit_building", r"習慣|毎日|続け|積み重ね|小さく|継続"),
        ("reflection", r"振り返|見直|内省|気づき|書き出|次に活か"),
        ("task_execution", r"タスク|着手|進め|実務|作業|行動へ|実行"),
        ("planning", r"計画|整理|優先順位|予定|明日|今日|準備"),
    ]
    for practice_type, pattern in patterns:
        if re.search(pattern, scene18_body):
            return practice_type
    return "planning"


def _scene_18_visual_structure(practice_type: str, application_context: str) -> str:
    if application_context == "both":
        return "work_life_bridge"
    return {
        "planning": "morning_planning",
        "communication": "calm_action_scene",
        "habit_building": "checklist_flow",
        "reflection": "notebook_and_tasks",
        "task_execution": "desk_focus",
        "emotional_control": "calm_action_scene",
        "decision_making": "notebook_and_tasks",
    }.get(practice_type, "desk_focus")


def _scene_18_composition(visual_structure: str) -> str:
    mapping = {
        "desk_focus": "構図A：朝のやわらかい光が入る整理されたデスクを斜め上から見せ、ノート・手帳・タスクカードに手を伸ばして本の学びを今日の行動へ移している瞬間を描く。ただPCに向かうだけにしない。",
        "morning_planning": "構図A：窓際の朝の光の中で、人物が手帳と小さなチェックリストを整え、今日試す行動を一つ選んでいる。前向きな開始感を出し、締めの余韻にはしない。",
        "checklist_flow": "構図C：左の学びメモから右の小さなタスクカードへ、短いカードの流れで行動化を見せる。手元がチェックを入れる途中で、scene_17のまとめ図解にはしない。",
        "calm_action_scene": "構図B：人物の顔を大きく出さず、ノートに一つ書く手元や付箋を貼る所作を主役にする。静かに実践している途中の空気を出し、読後の締め画像にしない。",
        "notebook_and_tasks": "構図B：開いたノート、手帳、付箋、タスクカードを中心に、学びを一つの具体行動へ変える整理された手元を描く。文字量を増やさずビジュアルで実用感を伝える。",
        "work_life_bridge": "構図D：整理された仕事机に、手帳・生活用の小物・朝の飲み物を控えめに置き、仕事と日常の両方で小さく試せる橋渡しを描く。広告風や締めの余韻にはしない。",
    }
    return mapping.get(visual_structure, mapping["desk_focus"])


def _scene_18_supporting_objects(practice_type: str, visual_structure: str) -> list[str]:
    base = ["ノート", "手帳", "付箋"]
    by_type = {
        "planning": ["チェックリスト", "予定カード", "小さなカレンダー"],
        "communication": ["会話メモ", "言い換えカード", "ペン"],
        "habit_building": ["習慣トラッカー", "小さなチェックカード", "朝の飲み物"],
        "reflection": ["振り返りノート", "ペン", "小さな時計"],
        "task_execution": ["タスクカード", "優先順位メモ", "ペン"],
        "emotional_control": ["深呼吸メモ", "余白のある手帳", "温かい飲み物"],
        "decision_making": ["判断基準カード", "選択肢メモ", "ペン"],
    }
    objects = base + by_type.get(practice_type, ["チェックリスト", "タスクカード"])
    if visual_structure == "work_life_bridge":
        objects.append("日常につながる小さな小物")
    return list(dict.fromkeys(objects))[:7]


def _scene_18_structured_prompt(context: dict[str, object]) -> dict[str, object]:
    scene_bodies = context.get("scene_bodies", {})
    scene18_body = str(scene_bodies.get("scene_18", "")) if isinstance(scene_bodies, dict) else ""
    points = context.get("three_key_points", [])
    point_labels = " ".join(str(point.get("label", "")) for point in points if isinstance(point, dict))
    extraction_source = f"{scene18_body} {point_labels} {context.get('current_theme', '')}"
    practice_theme_label = _short_label(extraction_source, "学びを実践する", 12)
    application_context = _scene_18_application_context(scene18_body or extraction_source)
    practice_action_label = _short_label(scene18_body, "小さく行動する", 12)
    viewer_takeaway_label = _short_label(scene18_body, "今日から実践", 12)
    practice_type = _scene_18_practice_type(scene18_body or extraction_source)
    visual_structure = _scene_18_visual_structure(practice_type, application_context)
    supporting_objects = _scene_18_supporting_objects(practice_type, visual_structure)
    composition = _scene_18_composition(visual_structure)
    practice_text = viewer_takeaway_label if 4 <= len(viewer_takeaway_label) <= 15 else "今日から実践"
    elements = [practice_text]
    final_prompt = f"""Create a 16:9 landscape video-insert image for Book Base, a Japanese business book YouTube channel. Use a refined watercolor illustration style with a premium, calm, elegant atmosphere. Use a soft cream-white and beige background with teal and subtle gold accents. Include a small natural Book Base logo placed unobtrusively.

This is Scene 18. Its fixed role is to show how the learning from the book can be applied in work or daily life. The image should help viewers imagine putting the ideas into action. It must not become a generic office scene or a simple desk-working image.

Practice theme:
{practice_theme_label}

Application context:
{application_context}

Practice action:
{practice_action_label}

Viewer takeaway:
{viewer_takeaway_label}

Practice type:
{practice_type}

Visual structure:
{visual_structure}

Supporting objects:
{', '.join(supporting_objects)}

{TEXT_LOCK_INSTRUCTION}:
{_text_block(elements)}

Composition:
{composition}

Visual motifs:
- organized desk
- notebook, planner, checklist, sticky notes, or task cards
- soft morning light
- hopeful and focused atmosphere
- calm structured whitespace
- premium watercolor texture
- gentle teal and subtle gold accents

Keep the image clean and easy to understand at a glance. Use minimal Japanese text only. Do not place long script text. Avoid clutter, avoid English text, avoid generic office stock-image feeling, avoid broken Japanese text, and avoid turning the image into a closing or recap scene."""
    return {"scene": 18, "fixed_role": "本の学びを仕事や日常に落とし込む実践シーン", "scene_role": "本の学びを仕事や日常に落とし込む実践シーン", "practice_theme_label": practice_theme_label, "application_context": application_context, "practice_action_label": practice_action_label, "viewer_takeaway_label": viewer_takeaway_label, "practice_type": practice_type, "visual_structure": visual_structure, "supporting_objects": supporting_objects, "exact_text_elements": elements, "composition": composition, "visual_motifs": ["organized desk", "notebook, planner, checklist, sticky notes, or task cards", "soft morning light", "hopeful and focused atmosphere", "calm structured whitespace", "premium watercolor texture", "gentle teal and subtle gold accents"], "style": _COMMON_STYLE_FOR_SCHEMA, "negative_rules": ["ただPCに向かっているだけにしない", "汎用オフィス画像にしない", "scene_17のまとめ図にしない", "scene_20の締め画像にしない", "英語テキストを入れない", "長文やCTAを入れない"], "variation_key": f"scene-18-practice-{practice_type}-{visual_structure}", "core_message": viewer_takeaway_label, "final_prompt": final_prompt}

def _scene_17_point_relationship(point_labels: list[str], scene17_body: str) -> str:
    combined = " ".join(point_labels + [scene17_body])
    if re.search(r"違い|比較|ではなく|一方|そのうえで|使う|実践", combined):
        return "compare_then_apply"
    if re.search(r"実践|行動|使う|活か|試す|始める|つなげ", combined):
        return "insight_to_action"
    if re.search(r"土台|応用|定着|積み上|段階|深め", combined):
        return "layered"
    if re.search(r"気づ|変え|続け|進め|前へ", combined):
        return "progressive"
    return "sequential"


def _scene_17_visual_structure(point_relationship: str) -> str:
    mapping = {
        "sequential": "recap_flow",
        "layered": "ladder_progression",
        "progressive": "three_step_path",
        "compare_then_apply": "summary_board",
        "insight_to_action": "three_step_path",
    }
    return mapping.get(point_relationship, "recap_flow")


def _scene_17_composition(visual_structure: str) -> str:
    mapping = {
        "recap_flow": "構図A：左から右へ①→②→③の順に整理カードを配置し、細い線や矢印で学びの流れをつなぐ。scene_04の予告見取り図ではなく、学び終えた後の振り返り感と到達感を出す。",
        "three_step_path": "構図D：①から②を通って③へ進む道筋やステップを描き、ここまで解説してきた学びが行動へ近づく印象にする。著者紹介や締めの挨拶要素は入れない。",
        "recap_cards": "構図A：3枚の整理カードを並べるが、必ず矢印や細い接続線で関係性を示す。単なる3カードやScene 04の予告カードにしない。",
        "summary_board": "構図C：中央の上品なまとめボードに見出しを置き、周囲に①②③の整理カードを配置して本全体を俯瞰できる総整理にする。",
        "ladder_progression": "構図B：①→②→③が少しずつ上がる階段・積み上げ構図にし、理解が順番に深まって到達する印象を出す。",
    }
    return mapping.get(visual_structure, mapping["recap_flow"])


def _scene_17_structured_prompt(context: dict[str, object]) -> dict[str, object]:
    points = context["three_key_points"]
    scene_bodies = context.get("scene_bodies", {})
    scene17_body = str(scene_bodies.get("scene_17", "")) if isinstance(scene_bodies, dict) else ""
    labels = [_short_label(str(point.get("label", "")), f"ポイント{i}", 12) for i, point in enumerate(points, 1)]
    while len(labels) < 3:
        labels.append(f"ポイント{len(labels) + 1}")
    point_relationship = _scene_17_point_relationship(labels, scene17_body)
    visual_structure = _scene_17_visual_structure(point_relationship)
    composition = _scene_17_composition(visual_structure)
    overall_takeaway_label = _short_label(scene17_body or str(context.get("current_theme", "")), "学びを整理する", 14)
    summary_heading = "今回のまとめ"
    elements = [summary_heading, f"① {labels[0]}", f"② {labels[1]}", f"③ {labels[2]}"]
    final_prompt = f"""Create a 16:9 landscape video-insert image for Book Base, a Japanese business book YouTube channel. Use a refined watercolor illustration style with a premium, calm, elegant atmosphere. Use a soft cream-white and beige background with teal and subtle gold accents. Include a small natural Book Base logo placed unobtrusively.

This is Scene 17. Its fixed role is to recap the three key points and summarize the core learning of the book. The image should help viewers quickly reorganize what they have learned so far. Do not create a generic three-card image without meaning. Do not hard-code any topic from a previous book. Build the labels from the current script only.

The three key points should not be treated as isolated parallel items. Show them as an ordered learning flow that deepens understanding step by step.

Point relationship:
{point_relationship}

Visual structure:
{visual_structure}

{TEXT_LOCK_INSTRUCTION}:
{_text_block(elements)}

Composition:
{composition}

Visual motifs:
- elegant recap cards
- subtle connecting arrows or lines
- summary board or flow layout
- calm structured whitespace
- premium watercolor texture
- gentle teal and gold accents

Keep the image clean and easy to understand at a glance. Use minimal Japanese text only. Do not place long script text. Avoid clutter, avoid English text, avoid a preview-like Scene 04 layout, and avoid making the three points look unrelated."""
    return {"scene": 17, "fixed_role": "3つの重要ポイントの総整理・総評", "scene_role": "3つの重要ポイントの総整理・総評", "point_1_label": labels[0], "point_2_label": labels[1], "point_3_label": labels[2], "overall_takeaway_label": overall_takeaway_label, "point_relationship": point_relationship, "visual_structure": visual_structure, "exact_text_elements": elements, "composition": composition, "visual_motifs": ["elegant recap cards", "subtle connecting arrows or lines", "summary board or flow layout", "calm structured whitespace", "premium watercolor texture", "gentle teal and gold accents"], "style": _COMMON_STYLE_FOR_SCHEMA, "negative_rules": ["英語テキストを入れない", "Points 1 / 2 / 3を使わない", "単なる3カードにしない", "scene_04の予告構図にしない", "scene_20の締め挨拶と混ぜない", "長文総評を入れない"], "variation_key": f"scene-17-recap-{visual_structure}", "core_message": overall_takeaway_label, "final_prompt": final_prompt}

def _scene_16_visual_mode(cover: str | None, scene16_body: str) -> str:
    if cover:
        return "real_cover_composite"
    if re.search(r"開いた|ページ|具体例|詳しく|学べ", scene16_body):
        return "open_book"
    if re.search(r"机|ノート|ペン|しおり|余韻", scene16_body):
        return "desk_still_life"
    return "generic_book"


def _scene_16_composition(visual_mode: str) -> str:
    mapping = {
        "generic_book": "構図B：タイトルのない一般的な本に手がそっと伸びる。本を大きく見せすぎず、余白と読書灯で自然な読書案内にする。",
        "real_cover_composite": "構図D：実ブックカバーを右または左に控えめに後処理合成するための清潔な余白を残し、背景は落ち着いた読書机にする。scene_03ほど大きくしない。",
        "reading_nook": "構図A：静かな読書スペース、開いた本、しおり、ノート、読書灯を配置し、売り込みではなく余韻を中心にする。",
        "open_book": "構図A：開いた本のページ、しおり、ノート、ペンを中心に、本の中にまだ学びが残っていることを余白で表現する。",
        "desk_still_life": "構図C：本、ノート、ペン、しおり、小さなカードを静物画のように配置し、短い2語だけをカードに置く。",
    }
    return mapping.get(visual_mode, mapping["generic_book"])


def _scene_16_structured_prompt(context: dict[str, object]) -> dict[str, object]:
    scene_bodies = context.get("scene_bodies", {})
    scene16_body = str(scene_bodies.get("scene_16", "")) if isinstance(scene_bodies, dict) else ""
    cover = context["assets"]["book_cover"]
    remaining_value_label = _short_label(re.sub(r"もし気になった方.*", "", scene16_body), "さらに深く学ぶ", 12)
    if remaining_value_label in {"ここで紹介した以外", "もし気になった方は"} or len(remaining_value_label) < 4:
        remaining_value_label = "さらに深く学ぶ"
    read_invitation_label = "本書を手に取る"
    visual_mode = _scene_16_visual_mode(str(cover) if cover else None, scene16_body)
    composition = _scene_16_composition(visual_mode)
    elements = [remaining_value_label, read_invitation_label]
    mode_rule = ""
    if visual_mode == "real_cover_composite":
        mode_rule = "The actual book cover will be composited later from the current input book_cover image. Do not draw or recreate the book cover. Leave a clean space for the real cover. The real cover should be smaller and more subtle than in Scene 03."
    elif visual_mode == "generic_book":
        mode_rule = "Use a generic book without a readable title. Do not invent a book cover. Do not write the current book title on the cover."
    final_prompt = f"""Create a 16:9 landscape video-insert image for Book Base, a Japanese business book YouTube channel. Use a refined watercolor illustration style with a premium, calm, elegant atmosphere. Use a soft cream-white and beige background with teal and subtle gold accents. Include a small natural Book Base logo placed unobtrusively.

This is Scene 16. Its fixed role is to guide viewers to the remaining value of the book and gently invite them to read it. The image should feel like a calm reading invitation, not a sales advertisement. Do not include purchase links, store names, price, or aggressive buying language. Do not hard-code any book title from a previous video.

Current remaining value:
{remaining_value_label}

Visual mode:
{visual_mode}

{TEXT_LOCK_INSTRUCTION}:
{_text_block(elements)}

Composition:
{composition}

Visual motifs:
- book or open book
- bookmark
- notebook and pen
- quiet reading desk
- warm reading light
- calm still-life atmosphere
- enough whitespace
- premium watercolor texture

{mode_rule}

Keep the image clean and easy to understand at a glance. Use minimal Japanese text only. Do not place long script text. Avoid clutter, avoid sales-like design, avoid purchase links, avoid fake book covers, avoid English text, and avoid repeating the Scene 03 book introduction composition."""
    return {"scene": 16, "fixed_role": "本書の残りの価値案内", "scene_role": "本書の残りの価値案内", "core_message": remaining_value_label, "book_title": str(context["book_title"]), "book_cover_path": cover, "remaining_value_label": remaining_value_label, "read_invitation_label": read_invitation_label, "visual_mode": visual_mode, "exact_text_elements": elements, "composition": composition, "visual_motifs": ["book or open book", "bookmark", "notebook and pen", "quiet reading desk", "warm reading light"], "style": _COMMON_STYLE_FOR_SCHEMA, "negative_rules": ["購入リンクを入れない", "販売サイト名を入れない", "架空のブックカバーを作らない", "英語テキストを入れない", "scene_03と同じ大きな本紹介構図にしない"], "post_process": {"composite_real_book_cover": visual_mode == "real_cover_composite", "cover_width_ratio": "0.16-0.24", "smaller_than_scene_03": True}, "variation_key": f"scene-16-remaining-value-{visual_mode}", "final_prompt": final_prompt}

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
        "visual_structure": {"type": "string", "enum": ["cause_to_effect", "before_after", "hidden_mechanism", "obstacle_and_solution", "contrast", "evidence_card", "data_report", "research_board", "document_review", "chart_focus"]},
        "point_2_label": {"type": "string"},
        "point_2_core_message": {"type": "string"},
        "point_2_type": {"type": "string", "enum": ["method", "mindset", "habit", "process", "contrast", "skill", "framework"]},
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
scene_07は具体的な研究・調査・公的データに寄せ、出典が弱い場合は断定せずNEEDS_REVIEWを本文またはresearch情報に残してください。scene_11は確認可能な人物・出来事だけを使い、確認できない実在企業・人物名は出さないでください。scene_15は重要ポイント③を補強する引用・短い一節・思想要約を現在の原稿と調査結果から選び、attribution_statusをverified / needs_review / unverifiedで必ず管理してください。確認が弱い場合は人物名・顔を出さずNEEDS_REVIEWにしてください。
完成前に、読みたくなる言い回し、一文の長さ、句読点、接続詞、語尾、会社員目線、AIっぽさ、本の内容との一致、シーン役割、次シーンへの流れを5点満点で自己採点し、平均4点未満なら再生成してください。

scenesは必ず20件の配列にし、各要素はscene_number（1〜20の整数）とbody（見出しを含まない本文）のみで返してください。Python側でscript.mdをレンダリングします。bodyは各シーン180〜220字、本文内改行なしの1段落、箇条書きなしにしてください。
titlesはpattern_a/pattern_b/pattern_cの構造化JSON、scheduleはtime/topicの配列、descriptionはtext/countの構造化JSON、commentは3行の配列で返してください。metadataは空のオブジェクトで構いません（Python側でMarkdownに整形します）。
thumbnail_commentsはPattern A/B/Cの方向性・コメント・狙い・出力ファイル名・使用画像・needs_reviewを含めてください。
image_promptsは20件の配列にし、各要素に「シーン番号」「所属ブロック」「ブロックの役割」「重要ポイント番号」「ブロック内での役割」「前ブロックからの理解の流れ」「このシーンで伝える要点」「画像の目的」「推奨構図」「画面内テキスト」「前後画像との差別化」「使用画像」「入力画像チェック」「needs_review」「最終プロンプト」を必ず含めてください。
画像生成前提として、内部で image_context.json 相当の book_title, author_name, current_theme, quiz, three_key_points, assets を原稿と入力画像チェックから抽出してください。scene_01〜scene_05は「固定役割」と「可変内容」を必ず分離し、具体的な正解文言、テーマ語句、ポイント語句、タイトル、著者名、book_cover/authorパスは毎回の原稿とinputから生成してください。scene_06の固定役割は「重要ポイント①の理由・背景・仕組み説明」です。scene_06ではscene_05の重要ポイント①とscene_06本文から、point_1_label, scene_06_core_message, reason_label, mechanism_label, effect_label, visual_metaphor, visual_structureを毎回抽出してください。visual_structureはcause_to_effect / before_after / hidden_mechanism / obstacle_and_solution / contrastから内容に合わせて1つ選び、構図に反映してください。scene_06のexact_text_elementsは原稿由来の短いラベル3つ以内、各15文字以内にし、特定の本や過去テーマの語句をテンプレートに固定しないでください。scene_06ではgeneric emotional icons、generic business person image、机・付箋・ノートだけの雰囲気画像、scene_05と同じ構図を禁止してください。恒久テンプレートに今回の本だけの言葉を固定しないでください。各sceneのexact_text_elementsを必ず原稿由来で作り、最終プロンプトには必ず次の英文を入れてください: Use only the following Japanese text elements exactly as written. Do not add any other Japanese or English text.
scene_09の固定役割は「重要ポイント②の導入」です。scene_09ではscene_09本文からpoint_2_label, point_2_core_message, point_2_type(method / mindset / habit / process / contrast / skill / framework), visual_metaphorを毎回抽出してください。「重要ポイント②」以外の画像内テキストは原稿由来で動的生成し、exact_text_elementsは3つ以内にしてください。会話、言い換え、受け取り方、視点変更、2人のビジネスパーソン、コミュニケーション、相手に伝える等を恒久テンプレートに固定しないでください。scene_09の最終プロンプトは推奨テンプレートに従い、generic business conversation imageを禁止し、scene_05およびscene_08との差別化を明記してください。
scene_10の固定役割は「重要ポイント②の具体化」です。scene_10ではscene_09の重要ポイント②とscene_10本文から、point_2_label, scene_10_core_message, example_label, application_label, result_label, visual_structure, visual_metaphorを毎回抽出してください。visual_structureはbefore_after / step_demo / example_scene / comparison / action_map / framework_demoから現在の内容に合わせて1つ選び、構図に反映してください。exact_text_elementsは3つ以内、原稿由来の短い日本語のみとし、英語や長文を入れないでください。split-screen、cause and effect、flowchart、business people in conversation、コミュニケーション、言い換え、視点変更、原因と結果を恒久テンプレートに固定しないでください。scene_10はscene_09の導入カードを繰り返さず、scene_11の実話エピソード画像とも役割を分けてください。
scene_12の固定役割は「コメントCTA」ですが、コメント促しを主役にしないでください。scene_09〜scene_11の重要ポイント②の流れから、本の内容・学び・考え方・図解・要点整理をメインにし、コメントCTAは右下などの小さな吹き出しや補助エリアに短い自然な日本語1要素までで添えてください。「あなたの経験は？」「{{experience_label}}」「コメントで教えてください」の3点セットを固定化しないでください。visual_structureはlearning_diagram / concept_map / notebook_summary / key_point_cardから現在の原稿に合わせて1つ選んでください。英語テキスト、Similar experience?、Subscribe風表現、キーワード型コメント促し、長文コメント文、原稿のコメントCTA全文、コメントCTAが主役の構図、scene_08の登録CTAに似た構図を禁止してください。scene_12の最終プロンプトは、Learning label、Comment CTA label、Visual structure、Compositionを必ず含め、本の学びが主役であることを明記してください。
scene_13の固定役割は「重要ポイント③の導入」です。scene_13ではscene_13本文からpoint_3_label, point_3_core_message, point_3_type(practice / solution / mindset / framework / habit / decision_rule / final_perspective), visual_metaphorを毎回抽出してください。「重要ポイント③」以外の画像内テキストは原稿由来で動的生成し、exact_text_elementsは3つ以内にしてください。チェックリスト、planner、hands checking off、手元ノート、具体的な行動完了シーン、今回の本の重要ポイント③の具体語句を恒久テンプレートに固定しないでください。scene_13はscene_09、scene_12、scene_18との差別化を明記し、第3ポイントカード、最後の扉、最終ステップ、光の道、実践への橋渡し、整理された型の提示から現在のpoint_3_typeに合う構図を選んでください。
scene_14の固定役割は「重要ポイント③の具体化」です。scene_14ではscene_13の重要ポイント③とscene_14本文から、point_3_label, scene_14_core_message, example_context_label, action_label, result_label, visual_structure, visual_metaphorを毎回抽出してください。visual_structureはpractical_example / step_demo / before_after / tool_use / scenario_demo / framework_applicationから現在の内容に合わせて1つ選び、構図に反映してください。exact_text_elementsは3つ以内、原稿由来の短い日本語のみとし、英語や長文を入れないでください。meeting、businessperson calmly responding、会議、返答、上司への対応、コミュニケーション、言い換え、具体的フレーズを恒久テンプレートに固定しないでください。scene_14はscene_13の導入カードを繰り返さず、scene_18の全体実践シーンとも役割を分けてください。
scene_11とscene_15の人物参考画像はユーザー入力必須ではありません。scene_11の固定役割は「重要ポイント②の実話エピソード補強」です。scene_11では現在の原稿と調査結果から、point_2_label, scene_11_core_message, episode_type(person / company / historical_event / public_case / symbolic_only), episode_name, episode_role_label, episode_action_label, lesson_label, verification_status(verified / needs_review / unverified), visual_mode(named_episode / silhouette_episode / symbolic_action), exact_text_elementsを毎回作成してください。特定人物・企業・出来事（Toyota、トヨタ、豊田喜一郎、元社長、特定業界など）をテンプレートに固定しないでください。verifiedは信頼できる情報源で確認でき、人物名または企業名が明確で、重要ポイント②とのつながりが自然で、過度な脚色がない場合のみ使用してください。verifiedの場合のみ人物名・企業名を短く画像内に入れてよいです。needs_reviewの場合は人物名・企業名を画像内に出さず、シルエットまたは象徴表現にしてください。unverifiedの場合は画像生成を成功扱いにせずNEEDS_REVIEWとして記録してください。実在人物の顔を参照画像なしに正確に描こうとせず、写真のような写実表現や肖像画中心を避け、行動とエピソードの意味を主役にしてください。scene_11はscene_10の具体例画像と構図を必ず差別化してください。research_scene_11には人物名・企業名・出来事名、概要、実話、重要ポイント②とのつながり、確認した出典、verification_status、visual_mode、画像生成時の表現方針をMarkdownで記録してください。
scene_15の固定役割は「重要ポイント③の引用・名言補強」です。scene_15では現在の原稿と調査結果から、point_3_label, scene_15_core_message, quote_source_type(person / book / public_domain_quote / paraphrase / symbolic_only), quote_source_name, quote_excerpt_label, lesson_label, attribution_status(verified / needs_review / unverified), visual_mode(named_quote / quote_card / still_life / symbolic_quote_scene), exact_text_elementsを毎回作成してください。特定の名言・人物名・著作名・テーマ固定フレーズをテンプレートに固定しないでください。verifiedは引用文または要約元、発言者または出典、重要ポイント③との自然なつながりを確認でき、誤引用の可能性が低い場合のみ使用してください。needs_reviewやunverifiedでは人物名や顔を画像内に出さず、quote card / still-life / symbolic compositionを優先してください。quote_excerpt_labelは短い1フレーズにし、長い引用全文を画像内に入れないでください。scene_15はscene_14の具体例構図と必ず差別化してください。research_scene_15には固定役割、抽出データ、引用や要約、出典確認、attribution_status、visual_mode、人物名・顔の使用可否、画像生成時の表現方針をMarkdownで記録してください。
scene_17の固定役割は「3つの重要ポイントの総整理・総評」です。scene_17ではscene_05、scene_09、scene_13からpoint_1_label、point_2_label、point_3_labelを毎回抽出し、overall_takeaway_label、point_relationship(sequential / layered / progressive / compare_then_apply / insight_to_action)、visual_structure(recap_flow / three_step_path / recap_cards / summary_board / ladder_progression)、exact_text_elementsを作成してください。3つのポイントは並列ではなく順番のある学びとして整理し、summary_headingは「今回のまとめ」または「3つのポイント」のどちらか1つ、画像内テキストは見出し1つ + ①②③の最大4要素にしてください。否定しない、言い換え、伝わり方、実践フレーズ、特定著者名、特定テーマ語句など今回の本だけの言葉をテンプレートに固定しないでください。Points 1 / 2 / 3など英語テキスト、generic three-card image、scene_04の予告構図、著者紹介、scene_20の締め挨拶やCTAとの混同を禁止してください。scene_17の最終プロンプトは総整理用テンプレートに従い、Point relationship、Visual structure、Composition、Use only the following Japanese text elements exactly as writtenを必ず含めてください。
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
