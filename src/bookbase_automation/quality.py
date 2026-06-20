from __future__ import annotations

import json
import re
from dataclasses import dataclass

SCENE_MIN_CHARS = 180
SCENE_MAX_CHARS = 220
TOTAL_MIN_CHARS = 3600
TOTAL_MAX_CHARS = 4400
DESCRIPTION_MIN_CHARS = 50
DESCRIPTION_MAX_CHARS = 60
SCENE_5_PREFIX = "重要ポイントの1つ目は"
SCENE_9_PREFIX = "重要ポイントの2つ目は"
SCENE_13_PREFIX = "重要ポイントの3つ目は"
SCENE_17_PREFIX = "今回の内容をおさらいすると"
SCENE_8_CTA = "このチャンネルでは、話題の本を、日々の仕事や年収アップにどう活かせるかという視点でお届けしています。興味のある方は、ぜひチャンネル登録お願いします。"
SCENE_16_BOOK_GUIDE = "もし気になった方は、ぜひ本書を手に取ってみてください。"
SCENE_20_CLOSING = "参考になった方は、高評価やハイプで応援していただけると嬉しいです。それでは、また次回の動画でお会いしましょう。最後までご視聴ありがとうございました。"
SCENE_1_PREFIX = "こんにちは！人生の土台作りをサポートするブックベースです！いきなりですが、"
SCENE_1_CLOSING = "それでは正解を発表します。"
FORBIDDEN_SCENE_1_PHRASES = ["選択肢は、", "1つ目", "2つ目", "3つ目", "少し考えてみてください。", "ある調査によると"]


def _scene_1_quiz_errors(scene_1: str) -> list[str]:
    errors: list[str] = []
    if not scene_1.startswith(SCENE_1_PREFIX):
        errors.append("固定開始文なし")
    if not scene_1.endswith(SCENE_1_CLOSING):
        errors.append("固定締め文なし")
    if "正解は" in scene_1 or re.search(r"正解[：:、は]*[ABCＡＢＣ]", scene_1):
        errors.append("シーン1で正解を明かしています")
    if "調査" not in scene_1:
        errors.append("調査出典なし")
    if not re.search(r"(会社|団体|法人|省|庁|機構|協会|研究所|サービス|メディア|大学|機関).{0,30}調査", scene_1):
        errors.append("会社・団体の説明不足")
    if not re.search(r"だったと思いますか。", scene_1):
        errors.append("クイズ文末が指定形式ではありません")
    for letter in "ABC":
        option = re.search(rf"{letter}[、.．]\s*([^ABCＡＢＣ。]+)", scene_1)
        if not option:
            errors.append(f"選択肢{letter}なし")
            continue
        if not re.search(r"\d", option.group(1)) or not re.search(r"％|%|人|社|件|割|円|時間|分|点", option.group(1)):
            errors.append(f"選択肢{letter}に具体的数値・単位なし")
    return errors

STYLE_CHECK_ITEMS = [
    "読みたくなる言い回し",
    "一文の長さの変化",
    "句読点の自然さ",
    "接続詞の自然さ",
    "語尾の変化",
    "会社員目線",
    "AIっぽさの少なさ",
    "本の内容との一致",
    "シーン間の流れ",
]

AI_LIKE_SCRIPT_PHRASES = [
    "効果的と言われています",
    "が特徴です",
    "について探っていきます",
    "ヒントが満載です",
    "第一人者です",
    "検証済みです",
    "とされています",
    "の重要性が示されています",
    "と言われています",
    "可能になるのです",
]

NATURAL_CONNECTORS = [
    "ここで大事なのは",
    "つまり",
    "たとえば",
    "一方で",
    "ここが怖いところで",
    "会社員の感覚で言うと",
    "ここから分かるのは",
    "だからこそ",
    "逆に言えば",
    "実は",
    "ここで本書が教えてくれるのは",
]

BUSINESS_CONTEXT_TERMS = [
    "会議", "報連相", "上司", "相談", "後輩", "指摘", "同僚", "雑談",
    "評価", "面談", "納期", "チャット", "チーム", "会社員", "仕事",
]

WEAK_TITLE_HOOK_PHRASES = [
    "知らないと損",
    "保存版",
    "誰でもできる",
    "会社員必見",
    "仕事がラクに",
    "意外な秘訣",
    "知っておかないと損",
    "驚きの効果",
    "すぐ使える",
    "人間関係が変わる",
    "今すぐ見て",
    "完全解説",
    "まとめ",
]


@dataclass(frozen=True)
class CheckResult:
    name: str
    status: str
    detail: str


def _compact_length(text: str) -> int:
    return len(re.sub(r"\s+", "", text))


def count_scene_body_chars(body: str) -> int:
    return len(body.strip())


def _scene_bodies(script: str) -> dict[int, str]:
    matches = list(re.finditer(r"^【シーン(?P<number>\d+)】\s*$", script, flags=re.MULTILINE))
    scenes: dict[int, str] = {}
    for index, match in enumerate(matches):
        number = int(match.group("number"))
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(script)
        scenes[number] = script[start:end].strip()
    return scenes


def _ordered_scene_bodies(script: str) -> list[str]:
    scenes = _scene_bodies(script)
    return [scenes[index] for index in range(1, 21) if index in scenes]




def _key_point_intro_depth_ok(body: str) -> bool:
    if not body:
        return False
    has_belief = any(token in body for token in ["思い込み", "誤解", "ありがち", "多く", "つい", "普通", "一般", "現場"])
    has_structure = any(token in body for token in ["構造", "仕組み", "背景", "本質", "なぜ", "本書では", "前提"])
    has_consequence = any(token in body for token in ["放置", "見ない", "知らない", "続ける", "失", "崩", "ズレ", "つなが", "起き"])
    has_takeaway = any(token in body for token in ["理解する必要", "見直す", "学ぶ", "まず", "ここを", "だからこそ"])
    no_meta = not any(token in body for token in ["省略", "改行", "プロンプト", "指示文", "のままにします"])
    shallow_end = body.endswith(("大切です。", "重要です。", "意識しましょう。"))
    return has_belief and has_structure and has_consequence and has_takeaway and no_meta and not shallow_end

def _intro_image_prompt_depth_ok(items: list[dict[str, object]], scene: int) -> bool:
    item = next((it for it in items if str(it.get("シーン番号", it.get("scene", ""))) == str(scene)), None)
    if not item:
        return False
    text = json.dumps(item, ensure_ascii=False)
    return all(token in text for token in ["重要ポイント", "主張", "図解", "まとめ", "誤解"]) and not any(token in text for token in ["見出しだけ", "抽象背景だけ"] if token == text.strip())

def _load_image_prompt_items(image_prompts: str) -> list[dict[str, object]]:
    try:
        data = json.loads(image_prompts)
    except json.JSONDecodeError:
        return []
    if not isinstance(data, list):
        return []
    return [item for item in data if isinstance(item, dict)]


def _image_prompt_block_errors(items: list[dict[str, object]]) -> list[str]:
    expected_blocks = {
        **{scene: "シーン1〜4：冒頭導入・クイズ・本紹介・重要ポイント提示" for scene in range(1, 5)},
        **{scene: "シーン5〜8：重要ポイント1" for scene in range(5, 9)},
        **{scene: "シーン9〜12：重要ポイント2" for scene in range(9, 13)},
        **{scene: "シーン13〜16：重要ポイント3" for scene in range(13, 17)},
        **{scene: "シーン17〜20：おさらい・実践・関連動画接続・締め" for scene in range(17, 21)},
    }
    errors: list[str] = []
    by_scene = {int(item.get("シーン番号", item.get("scene", 0))): item for item in items if str(item.get("シーン番号", item.get("scene", ""))).isdigit()}
    for scene, expected in expected_blocks.items():
        item = by_scene.get(scene)
        if item is None:
            errors.append(f"シーン{scene}: 未検出")
            continue
        if item.get("所属ブロック") != expected:
            errors.append(f"シーン{scene}: 所属ブロック不一致")
    return errors


def _image_prompt_required_field_errors(items: list[dict[str, object]]) -> list[str]:
    required = [
        "シーン番号",
        "所属ブロック",
        "ブロックの役割",
        "重要ポイント番号",
        "ブロック内での役割",
        "前ブロックからの理解の流れ",
        "このシーンで伝える要点",
        "画像の目的",
        "推奨構図",
        "画面内テキスト",
        "前後画像との差別化",
        "使用画像",
        "入力画像チェック",
        "needs_review",
        "最終プロンプト",
    ]
    errors: list[str] = []
    for index, item in enumerate(items, start=1):
        missing = [field for field in required if field not in item or item[field] in {"", None}]
        if missing:
            errors.append(f"item{index}: {', '.join(missing)}")
    return errors


def _image_prompt_flow_ok(items: list[dict[str, object]]) -> bool:
    by_scene = {int(item.get("シーン番号", item.get("scene", 0))): item for item in items if str(item.get("シーン番号", item.get("scene", ""))).isdigit()}
    point1 = all(by_scene.get(scene, {}).get("重要ポイント番号") == "重要ポイント1" for scene in range(5, 9))
    point2 = all(by_scene.get(scene, {}).get("重要ポイント番号") == "重要ポイント2" for scene in range(9, 13))
    point3 = all(by_scene.get(scene, {}).get("重要ポイント番号") == "重要ポイント3" for scene in range(13, 17))
    flow_text = " ".join(str(item.get("前ブロックからの理解の流れ", "")) + " " + str(item.get("推奨構図", "")) for item in items)
    return point1 and point2 and point3 and all(token in flow_text for token in ["土台", "構造", "実践"])



HARDCODED_BOOK_SPECIFIC_TERMS = [
    "正解はB",
    "相手が話しやすくなる",
    "否定しない言い換え",
    "否定しない心理効果",
    "心が開きやすい",
    "否定される",
    "防御的になる",
    "対話が止まる",
    "言い方で関係は変わる",
    "①否定しない",
    "②伝わり方",
    "③実践フレーズ",
    "否定しない言い換え事典",
    "長尾彰",
    "20260619_book_cover.webp",
    "20260619_author.jpg",
]


def _scene_rule_separation_lines(items: list[dict[str, object]]) -> list[str]:
    by_scene = {int(item.get("シーン番号", item.get("scene", 0))): item for item in items if str(item.get("シーン番号", item.get("scene", ""))).isdigit()}
    lines = ["", "【画像プロンプト恒久ルールチェック】", ""]
    for scene in range(1, 6):
        item = by_scene.get(scene, {})
        has_role = bool(item.get("scene_role") or item.get("画像の目的"))
        has_exact = bool(item.get("exact_text_elements"))
        instruction = "Use only the following Japanese text elements exactly as written. Do not add any other Japanese or English text." in str(item.get("final_prompt") or item.get("最終プロンプト") or "")
        lines.append(f"scene_{scene:02d}：固定役割と可変内容を分離：{'OK' if has_role and has_exact and instruction else 'NG'}")
    prompt_templates = []
    for item in items[:5]:
        prompt = str(item.get("final_prompt") or item.get("最終プロンプト") or "")
        prompt = re.sub(
            r"Use only the following Japanese text elements exactly as written\. Do not add any other Japanese or English text:?\n.*?(?=\nComposition:| Composition:|$)",
            "Use only the following Japanese text elements exactly as written. Do not add any other Japanese or English text.",
            prompt,
            flags=re.S,
        )
        prompt_templates.append(prompt)
    prompts = "\n".join(prompt_templates)
    leaked = [term for term in HARDCODED_BOOK_SPECIFIC_TERMS if term in prompts]
    all_exact = all(by_scene.get(scene, {}).get("exact_text_elements") for scene in range(1, 6))
    variations = [str(by_scene.get(scene, {}).get("variation_key") or by_scene.get(scene, {}).get("前後画像との差別化") or "") for scene in range(1, 6)]
    lines.append(f"今回テーマ固有語句のハードコードなし：{'OK' if not leaked else 'NG'}")
    lines.append(f"exact_text_elementsを原稿から生成：{'OK' if all_exact else 'NG'}")
    lines.append(f"隣接シーンとの差別化：{'OK' if len(set(variations)) == len(variations) and all(variations) else 'NG'}")
    if leaked:
        lines.append(f"検出語句：{', '.join(leaked)}")
    return lines


def _scene_19_quality_lines(items: list[dict[str, object]]) -> list[str]:
    by_scene = {int(item.get("シーン番号", item.get("scene", 0))): item for item in items if str(item.get("シーン番号", item.get("scene", ""))).isdigit()}
    item = by_scene.get(19, {})
    prompt = str(item.get("final_prompt") or item.get("最終プロンプト") or "")
    exact = item.get("exact_text_elements") if isinstance(item.get("exact_text_elements"), list) else []
    fixed_role = str(item.get("fixed_role") or item.get("scene_role") or "")
    forbidden_cta = ["関連動画を見てください", "こちらもおすすめ", "クリック", "今すぐ見る"]
    lines = ["", "【scene_19 画像品質チェック】", ""]
    lines.append(f"scene_19固定役割に合っている：{'OK' if '現在の本と関連過去動画の本を自然につなぐ接続シーン' in fixed_role else 'NG'}")
    lines.append(f"現在の本と関連過去動画の本をつなぐ画像になっている：{'OK' if item.get('current_book_label') and item.get('related_book_label') and 'two books connected naturally' in prompt else 'NG'}")
    lines.append(f"単なる広告・CTA画像になっていない：{'OK' if not any(token in prompt for token in forbidden_cta) and 'advertisement-like' in prompt else 'NG'}")
    lines.append(f"2冊の本の関係性が connection_reason として定義されている：{'OK' if item.get('connection_reason') else 'NG'}")
    lines.append(f"connection_type が設定されている：{'OK' if item.get('connection_type') in {'same_theme', 'next_step', 'practical_extension', 'contrast_and_deepen', 'money_or_life_application'} else 'NG'}")
    lines.append(f"visual_structure が設定されている：{'OK' if item.get('visual_structure') in {'book_bridge', 'light_path', 'flowing_pages', 'ribbon_connection', 'two_books_perspective'} else 'NG'}")
    lines.append(f"参照画像が現在の本として扱われている：{'OK' if 'Use the reference image as the current book cover' in prompt and item.get('reference_image_path') else 'NG'}")
    lines.append(f"過去動画側の本が省略されていない：{'OK' if item.get('related_book_cover_path') or 'related past-video book cover as the second book' in prompt else 'NG'}")
    lines.append(f"画像内テキストが1要素以内：{'OK' if len(exact) <= 1 else 'NG'}")
    lines.append(f"英語テキストなし：{'OK' if 'Do not add any other Japanese or English text' in prompt and 'Avoid clutter, avoid English text' in prompt else 'NG'}")
    lines.append(f"指定外テキストなし：{'OK' if 'Use only the following Japanese text elements exactly as written' in prompt else 'NG'}")
    lines.append(f"文字量が多すぎない：{'OK' if len(exact) <= 1 and all(len(str(text)) <= 15 for text in exact) else 'NG'}")
    lines.append(f"scene_20の締め画像と役割が混ざっていない：{'OK' if 'Do not make it a closing or thank-you scene like Scene 20' in prompt or 'scene_20' in ''.join(map(str, item.get('negative_rules', []))) else 'NG'}")
    lines.append(f"広告バナー風になっていない：{'OK' if 'clickbait banner' in prompt and not any(token in prompt for token in forbidden_cta) else 'NG'}")
    return lines

def _sentence_lengths(text: str) -> list[int]:
    parts = [part.strip() for part in re.split(r"[。！？]", text) if part.strip()]
    return [len(part) for part in parts]


def _ending_tokens(text: str) -> list[str]:
    endings: list[str] = []
    for sentence in [part.strip() for part in re.split(r"[。！？]", text) if part.strip()]:
        match = re.search(r"(なんです|ではないでしょうか|かもしれません|ということです|してみてください|感じるはずです|見えてきます|につながります|と言えます|です|ます|でした|ました|ましょう|ません)$", sentence)
        if match:
            endings.append(match.group(1))
    return endings


def build_style_quality_scores(script: str, source_text: str = "") -> dict[str, int]:
    scenes = _ordered_scene_bodies(script)
    full_text = "".join(scenes)
    lengths = _sentence_lengths(full_text)
    endings = _ending_tokens(full_text)
    connector_hits = sum(1 for token in NATURAL_CONNECTORS if token in full_text)
    business_hits = sum(1 for token in BUSINESS_CONTEXT_TERMS if token in full_text)
    ai_like_hits = sum(full_text.count(token) for token in AI_LIKE_SCRIPT_PHRASES)
    question_overuse = any(body.count("？") > 1 for body in scenes)
    source_keywords = [token for token in re.findall(r"[一-龥ぁ-んァ-ヶA-Za-z0-9]{3,}", source_text) if token in full_text]
    varied_lengths = bool(lengths) and min(lengths) <= 25 and max(lengths) >= 45 and (max(lengths) - min(lengths)) >= 25
    comma_ratio_ok = bool(lengths) and 0.25 <= (full_text.count("、") / max(1, len(lengths))) <= 3.5
    ending_diversity = len(set(endings))
    repeated_ending_ratio = max((endings.count(e) for e in set(endings)), default=0) / max(1, len(endings))
    avg_scene_len_ok = len(scenes) == 20 and all(SCENE_MIN_CHARS <= count_scene_body_chars(scene) <= SCENE_MAX_CHARS for scene in scenes)
    return {
        "読みたくなる言い回し": 5 if any(token in full_text for token in ["こんな経験", "少し想像", "ここ、", "実はこれ", "気になる"]) and not question_overuse else 4,
        "一文の長さの変化": 5 if varied_lengths else 3,
        "句読点の自然さ": 5 if comma_ratio_ok else 3,
        "接続詞の自然さ": 5 if connector_hits >= 4 else 4 if connector_hits >= 2 else 3,
        "語尾の変化": 5 if ending_diversity >= 6 and repeated_ending_ratio <= 0.45 else 4 if ending_diversity >= 4 else 3,
        "会社員目線": 5 if business_hits >= 8 else 4 if business_hits >= 5 else 3,
        "AIっぽさの少なさ": 5 if ai_like_hits == 0 else 3 if ai_like_hits <= 2 else 1,
        "本の内容との一致": 5 if source_keywords or not source_text.strip() else 4 if avg_scene_len_ok else 3,
        "シーン間の流れ": 5 if avg_scene_len_ok and all(token in full_text for token in [SCENE_5_PREFIX, SCENE_9_PREFIX, SCENE_13_PREFIX, SCENE_17_PREFIX]) else 3,
    }


def _style_quality_report_lines(script: str, source_text: str = "") -> list[str]:
    scores = build_style_quality_scores(script, source_text)
    average = sum(scores.values()) / len(STYLE_CHECK_ITEMS)
    lines = ["", "【文体品質チェック】", ""]
    for item in STYLE_CHECK_ITEMS:
        lines.append(f"{item}：{scores[item]}/5")
    lines.append(f"平均点：{average:.1f}/5")
    lines.append(f"判定：{'OK' if average >= 4.0 else 'REWRITE_REQUIRED'}")
    return lines

def _title_hooks(titles: str) -> list[str]:
    return [hook.strip() for hook in re.findall(r"【([^】]+)】", titles)]


def _title_lines(titles: str) -> list[str]:
    return [line.strip() for line in titles.splitlines() if re.search(r"【[^】]+】", line)]


def _title_has_front_and_back_hooks(line: str) -> bool:
    body = re.sub(r"^[ABCＡＢＣ][.)．。]\s*", "", line).strip()
    return bool(re.match(r"^【[^】]+】.+【[^】]+】$", body))


def _has_weak_title_hook(titles: str) -> bool:
    return any(hook in WEAK_TITLE_HOOK_PHRASES for hook in _title_hooks(titles))


def _has_title_number(titles: str) -> bool:
    return bool(re.search(r"\d|[０-９]|[一二三四五六七八九十百千万]+(?:つ|個|選|例|連発)", titles))


def _has_single_paragraph_scene_bodies(scenes: dict[int, str]) -> bool:
    return all("\n" not in body for body in scenes.values())


def _has_exact_scene_sequence(scenes: dict[int, str]) -> bool:
    return sorted(scenes) == list(range(1, 21))



def _scene_2_bridge_ok(scene_2: str) -> bool:
    if not scene_2 or "正解" not in scene_2:
        return False
    if not re.search(r"そこで今回は、.+について学んでいきます。$", scene_2):
        return False
    if any(meta in scene_2 for meta in ["省略不可", "改行入れません", "のままにします", "プロンプト", "指示文"]):
        return False
    has_meaning = any(token in scene_2 for token in ["意味します", "ということです", "示しています", "見えてきます", "捉えています"])
    has_gap = any(token in scene_2 for token in ["一見", "と思われがち", "世間", "一般", "ズレ", "実は", "しかし"])
    has_book_need = "本書" in scene_2 and any(token in scene_2 for token in ["学ぶ", "知る", "見る", "必要", "大事"])
    return has_meaning and has_gap and has_book_need

def build_quality_report(script: str, titles: str, image_prompts: str, description: str = "", source_text: str = "") -> str:
    scene_map = _scene_bodies(script)
    scenes = _ordered_scene_bodies(script)
    scene_lengths = [count_scene_body_chars(scene) for scene in scenes]
    total_chars = sum(scene_lengths)
    out_of_range = [
        f"シーン{index}: {length}字"
        for index, length in enumerate(scene_lengths, start=1)
        if not SCENE_MIN_CHARS <= length <= SCENE_MAX_CHARS
    ]
    hooks = _title_hooks(titles)
    title_lines = _title_lines(titles)
    image_items = _load_image_prompt_items(image_prompts)
    image_block_errors = _image_prompt_block_errors(image_items)
    image_field_errors = _image_prompt_required_field_errors(image_items)
    duplicated_hooks = sorted({hook for hook in hooks if hooks.count(hook) > 1})
    description_length = _compact_length(description)
    scene_1 = scene_map.get(1, "")
    scene_2 = scene_map.get(2, "")
    scene_3 = scene_map.get(3, "")
    scene_4 = scene_map.get(4, "")
    scene_5 = scene_map.get(5, "")
    scene_7 = scene_map.get(7, "")
    scene_8 = scene_map.get(8, "")
    scene_9 = scene_map.get(9, "")
    scene_11 = scene_map.get(11, "")
    scene_12 = scene_map.get(12, "")
    scene_13 = scene_map.get(13, "")
    scene_15 = scene_map.get(15, "")
    scene_16 = scene_map.get(16, "")
    scene_17 = scene_map.get(17, "")
    scene_18 = scene_map.get(18, "")
    scene_19 = scene_map.get(19, "")
    scene_20 = scene_map.get(20, "")

    heading_format_ok = not bool(re.search(r"^【シーン\d+】\S", script, flags=re.MULTILINE)) and _has_exact_scene_sequence(scene_map)
    scene_gap_ok = bool(re.search(r"^【シーン1】\n", script)) and all(f"\n\n【シーン{index}】\n" in script for index in range(2, 21))
    bullet_pattern = re.compile(r"(^|\n)\s*(?:[-*・]|\d+[.)．、])\s+")
    no_bullets = all(not bullet_pattern.search(body) for body in scene_map.values())
    body_one_paragraph_ok = _has_single_paragraph_scene_bodies(scene_map)

    results = [
        CheckResult("【シーン1】〜【シーン20】形式", "OK" if _has_exact_scene_sequence(scene_map) else "NG", f"検出シーン: {sorted(scene_map)}"),
        CheckResult("シーン本文1段落", "OK" if body_one_paragraph_ok else "NG", "シーン内改行なし"),
        CheckResult("シーン間空行", "OK" if scene_gap_ok else "NG", "各シーンの間に空行1行"),
        CheckResult("シーン本文箇条書きなし", "OK" if no_bullets else "NG", "Markdown箇条書き・番号リストなし"),
        CheckResult(
            "各シーン180〜220字",
            "OK" if len(scenes) == 20 and not out_of_range else "NG",
            "全シーン範囲内" if not out_of_range else ", ".join(out_of_range),
        ),
        CheckResult("全体3600〜4400字", "OK" if TOTAL_MIN_CHARS <= total_chars <= TOTAL_MAX_CHARS else "NG", f"現在の文字数目安: {total_chars}"),
        CheckResult("50〜60文字説明", "OK" if DESCRIPTION_MIN_CHARS <= description_length <= DESCRIPTION_MAX_CHARS else "NG", f"現在の説明文字数: {description_length}"),
        CheckResult("シーン1統計クイズ", "OK" if not _scene_1_quiz_errors(scene_1) else "NG", " / ".join(_scene_1_quiz_errors(scene_1)) or "固定開始文、出典説明、数値選択肢、締め文を確認済み"),
        CheckResult("シーン1禁止表現なし", "OK" if not any(phrase in scene_1 for phrase in FORBIDDEN_SCENE_1_PHRASES) else "NG", "禁止表現を確認してください"),
        CheckResult("シーン2正解発表・意味づけ・学習接続", "OK" if _scene_2_bridge_ok(scene_2) else "NG", "正解発表→意味づけ→世間とのズレ→本の内容を学ぶ必要性→そこで今回は〜について学んでいきます。の順で接続してください"),
        CheckResult("シーン3本紹介固定文", "OK" if "今回紹介するのは、" in scene_3 and "こちらの本になります。" in scene_3 else "NG", "固定文を確認してください"),
        CheckResult("シーン4著者紹介と3ポイント", "OK" if "著者" in scene_4 and "3つ" in scene_4 else "NG", "著者紹介と3つの重要ポイントを確認してください"),
        CheckResult("シーン5冒頭固定", "OK" if scene_5.startswith(SCENE_5_PREFIX) else "NG", f"必須開始文: {SCENE_5_PREFIX}"),
        CheckResult("シーン5導入の深さ", "OK" if _key_point_intro_depth_ok(scene_5) else "NG", "主張→誤解→構造→悪影響→学ぶ意味を入れてください"),
        CheckResult("シーン7研究・データ補強", "OK" if any(token in scene_7 for token in ["研究", "調査", "データ", "論文", "公的"]) else "NG", "研究・データ補強を入れてください"),
        CheckResult("シーン8チャンネル登録固定文", "OK" if SCENE_8_CTA in scene_8 else "NG", "固定CTAを変えずに入れてください"),
        CheckResult("シーン9冒頭固定", "OK" if scene_9.startswith(SCENE_9_PREFIX) else "NG", f"必須開始文: {SCENE_9_PREFIX}"),
        CheckResult("シーン9導入の深さ", "OK" if _key_point_intro_depth_ok(scene_9) else "NG", "主張→誤解→構造→悪影響→学ぶ意味を入れてください"),
        CheckResult("シーン11実話エピソード", "OK" if any(token in scene_11 for token in ["実話", "経営者", "歴史", "著名人", "有名", "ビル・ゲイツ", "孫正義", "ウォーレン・バフェット"]) else "NG", "確認済み実話を入れてください"),
        CheckResult("シーン12コメント促進形式", "OK" if "経験はありますか？" in scene_12 and "もし似たような経験があれば、ぜひコメント欄で教えてください。" in scene_12 else "NG", "固定フォーマットを確認してください"),
        CheckResult("シーン13冒頭固定", "OK" if scene_13.startswith(SCENE_13_PREFIX) else "NG", f"必須開始文: {SCENE_13_PREFIX}"),
        CheckResult("シーン13導入の深さ", "OK" if _key_point_intro_depth_ok(scene_13) else "NG", "主張→誤解→構造→悪影響→学ぶ意味を入れてください"),
        CheckResult("シーン15名言補強", "OK" if "名言" in scene_15 or "言葉" in scene_15 else "NG", "確認済み名言を入れてください"),
        CheckResult("シーン16本書案内固定文", "OK" if SCENE_16_BOOK_GUIDE in scene_16 and "概要欄" not in scene_16 else "NG", "本書案内固定文と概要欄誘導なしを確認してください"),
        CheckResult("シーン17おさらい開始", "OK" if scene_17.startswith(SCENE_17_PREFIX) else "NG", f"必須開始文: {SCENE_17_PREFIX}"),
        CheckResult("シーン18実践", "OK" if any(token in scene_18 for token in ["実践", "仕事", "日常", "明日", "行動"]) else "NG", "仕事や日常への実践に落とし込んでください"),
        CheckResult("シーン19関連動画接続", "OK" if any(token in scene_19 for token in ["関連動画", "過去動画", "そちらもあわせてご視聴ください"]) else "NG", "関連動画への自然な接続を入れてください"),
        CheckResult("シーン20締め固定文", "OK" if SCENE_20_CLOSING in scene_20 else "NG", "固定締め文を変えずに入れてください"),
        CheckResult("タイトル案A/B/C", "OK" if all(label in titles for label in ["A", "B", "C"]) else "NG", "3案あるか確認してください"),
        CheckResult("タイトル前後の【】", "OK" if len(title_lines) >= 3 and all(_title_has_front_and_back_hooks(line) for line in title_lines[:3]) else "NG", "【冒頭フック】メインタイトル【後方フック】形式を確認してください"),
        CheckResult("タイトルの【】フック重複", "OK" if hooks and not duplicated_hooks else "NG", "重複なし" if hooks and not duplicated_hooks else f"重複または未検出: {', '.join(duplicated_hooks) or 'フックなし'}"),
        CheckResult("タイトル弱いフックなし", "OK" if hooks and not _has_weak_title_hook(titles) else "NG", "禁止された弱いフック語を単独使用していないか確認してください"),
        CheckResult("タイトル数字検討", "OK" if _has_title_number(titles) else "NG", "数字化できる要素がある場合は数字を入れてください"),
        CheckResult("画像プロンプト20件", "OK" if len(image_items) == 20 else "NG", f"検出件数: {len(image_items)}"),
        CheckResult("画像プロンプト必須メタ情報", "OK" if image_items and not image_field_errors else "NG", "全項目あり" if not image_field_errors else "; ".join(image_field_errors[:3])),
        CheckResult("画像プロンプト所属ブロック", "OK" if image_items and not image_block_errors else "NG", "全シーン一致" if not image_block_errors else "; ".join(image_block_errors[:5])),
        CheckResult("重要ポイント画像の理解の流れ", "OK" if image_items and _image_prompt_flow_ok(image_items) else "NG", "重要ポイント1=土台、2=構造、3=実践の流れを確認してください"),
        CheckResult("導入画像5/9/13の情報量", "OK" if image_items and all(_intro_image_prompt_depth_ok(image_items, scene) for scene in [5, 9, 13]) else "NG", "番号・主張・補足・図解・まとめ帯・誤解対比を入れてください"),
    ]
    lines = [
        "# 品質チェック結果",
        "",
        "【原稿形式チェック】",
        "",
        f"シーン数：{len(scene_map)} / 20",
        f"見出し形式：{'OK' if heading_format_ok else 'NG'}",
        f"シーン間空行：{'OK' if scene_gap_ok else 'NG'}",
        f"本文1段落：{'OK' if body_one_paragraph_ok else 'NG'}",
        f"全体文字数：{total_chars}字 / 3600〜4400字",
        "",
        "【シーン別文字数】",
        "",
    ]
    for index in range(1, 21):
        length = count_scene_body_chars(scene_map.get(index, ""))
        status = "OK" if SCENE_MIN_CHARS <= length <= SCENE_MAX_CHARS else "NG"
        lines.append(f"シーン{index}：{length}字 {status}")
    lines.extend(_style_quality_report_lines(script, source_text))
    lines.extend(_scene_rule_separation_lines(image_items))
    lines.extend(_scene_19_quality_lines(image_items))
    lines.extend(["", "## 詳細チェック", ""])
    for result in results:
        lines.append(f"- {result.name}: {result.status}（{result.detail}）")
    lines.extend(
        [
            "",
            "## 修正推奨",
            "- NGの項目が1つでもある場合は、提出前に再生成または手修正してください。",
            "- 事実確認が必要な統計、研究、実話、名言は、Koichiさんの確認対象として扱ってください。",
            "- 自動生成結果は最終稿ではなく、品質担保のための確認前提の下書きです。",
        ]
    )
    return "\n".join(lines) + "\n"
