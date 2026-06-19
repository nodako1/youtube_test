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
FORBIDDEN_SCENE_1_PHRASES = ["選択肢は、", "1つ目", "2つ目", "3つ目", "少し考えてみてください。"]
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


def build_quality_report(script: str, titles: str, image_prompts: str, description: str = "") -> str:
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
        CheckResult("シーン1統計クイズ", "OK" if all(token in scene_1 for token in ["A.", "B.", "C.", "調査", "それでは正解を発表します。"]) else "NG", "ABC選択肢、調査、締め文を確認してください"),
        CheckResult("シーン1禁止表現なし", "OK" if not any(phrase in scene_1 for phrase in FORBIDDEN_SCENE_1_PHRASES) else "NG", "禁止表現を確認してください"),
        CheckResult("シーン2正解発表とテーマ接続", "OK" if "正解" in scene_2 and any(token in scene_2 for token in ["テーマ", "本", "会社員"]) else "NG", "正解発表からテーマへ接続してください"),
        CheckResult("シーン3本紹介固定文", "OK" if "今回紹介するのは、" in scene_3 and "こちらの本になります。" in scene_3 else "NG", "固定文を確認してください"),
        CheckResult("シーン4著者紹介と3ポイント", "OK" if "著者" in scene_4 and "3つ" in scene_4 else "NG", "著者紹介と3つの重要ポイントを確認してください"),
        CheckResult("シーン5冒頭固定", "OK" if scene_5.startswith(SCENE_5_PREFIX) else "NG", f"必須開始文: {SCENE_5_PREFIX}"),
        CheckResult("シーン7研究・データ補強", "OK" if any(token in scene_7 for token in ["研究", "調査", "データ", "論文", "公的"]) else "NG", "研究・データ補強を入れてください"),
        CheckResult("シーン8チャンネル登録固定文", "OK" if SCENE_8_CTA in scene_8 else "NG", "固定CTAを変えずに入れてください"),
        CheckResult("シーン9冒頭固定", "OK" if scene_9.startswith(SCENE_9_PREFIX) else "NG", f"必須開始文: {SCENE_9_PREFIX}"),
        CheckResult("シーン11実話エピソード", "OK" if any(token in scene_11 for token in ["実話", "経営者", "歴史", "著名人", "有名", "ビル・ゲイツ", "孫正義", "ウォーレン・バフェット"]) else "NG", "確認済み実話を入れてください"),
        CheckResult("シーン12コメント促進形式", "OK" if "経験はありますか？" in scene_12 and "もし似たような経験があれば、ぜひコメント欄で教えてください。" in scene_12 else "NG", "固定フォーマットを確認してください"),
        CheckResult("シーン13冒頭固定", "OK" if scene_13.startswith(SCENE_13_PREFIX) else "NG", f"必須開始文: {SCENE_13_PREFIX}"),
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
