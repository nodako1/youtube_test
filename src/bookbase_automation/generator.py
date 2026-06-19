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


@dataclass(frozen=True)
class GeneratedAssets:
    script: str
    titles: str
    description: str
    thumbnail_ideas: str
    thumbnail_comments: str
    metadata: str
    image_prompts: str
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
        role_map = {5: "重要ポイント1の導入", 6: "重要ポイント1の説明・理由", 7: "重要ポイント1の具体化・日常への接続", 8: "重要ポイント1の締め＋登録促し"}
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


def _build_image_prompt_item(scene: int, asset_check: AssetCheck | None = None) -> dict[str, str | int]:
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
    prompt = (
        "16:9 watercolor illustration for a premium Japanese business book YouTube channel, "
        "soft cream white beige teal and gold palette, small natural Book Base logo in the upper-right or lower-right, "
        f"scene {scene}, {meta['所属ブロック']}, {meta['ブロック内での役割']}, "
        f"{composition_by_point[point]}, no long text, one clear message, avoid repeating adjacent composition"
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
        "推奨構図": composition_by_point[point],
        "画面内テキスト": text,
        "前後画像との差別化": differentiation,
        "使用画像": used_image,
        "入力画像チェック": asset_note,
        "needs_review": bool((asset_check and asset_check.status == "MISSING" and scene in {3, 19}) or scene in {11, 15}),
        "最終プロンプト": prompt + f", reference image: {used_image}, asset note: {asset_note}",
        "scene": scene,
        "prompt": prompt,
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
        1: "人材サービス会社が社会人に行った調査では、仕事の悩みは知識不足より整理不足から生まれることが多いとされています。では、忙しい会社員が最初に見直すべきものは何でしょうか。A.根性 B.思考の整理 C.残業時間。それでは正解を発表します。",
        2: "正解はBの思考の整理です。数字や調査結果を見ると、会社員の悩みは能力そのものより、情報をどう扱うかで大きく変わります。今回のテーマは、本の内容を仕事の判断に変える方法です。",
        3: f"今回紹介するのは、{author}さんの『{book_title}』こちらの本になります。本書の要点は、知識を増やすだけでなく、目の前の課題に使える形へ整えることです。会社員にとっては、迷いを減らし行動を早める武器になります。",
        4: "著者の経歴で注目したいのは、複雑なテーマを実生活に結びつけて語っている点です。今回の重要ポイントは3つあります。問題を見える化すること、背景を捉えること、最後に小さく実践へ移すことです。",
        5: "重要ポイントの1つ目は問題を見える化することです。仕事で迷う時ほど、原因は能力不足ではなく、考える材料が頭の中で混ざっていることにあります。まず何に困っているのかを言葉にすると、次の行動が見えます。",
        6: "問題を見える化すると、上司の評価、納期、会議の発言なども分けて考えられます。本書のメモでは、感情と事実を切り分ける視点が重要です。不安をそのまま抱えるより、事実を書き出す方が前に進めます。",
        7: "心理学の研究でも、悩みを書き出す行為は認知的負荷を下げると説明されます。公的データや調査でも、仕事のストレスは曖昧な不安で強まりやすいものです。本書の整理法は、科学的にも納得しやすい考え方です。",
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
    prompts = [_build_image_prompt_item(index, assets_by_scene.get(index)) for index in range(1, 21)]
    image_prompts = json.dumps(prompts, ensure_ascii=False, indent=2) + "\n"
    return GeneratedAssets(
        script,
        titles,
        description + "\n",
        thumbnail_ideas,
        thumbnail_comments,
        metadata,
        image_prompts,
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

scenesは必ず20件の配列にし、各要素はscene_number（1〜20の整数）とbody（見出しを含まない本文）のみで返してください。Python側でscript.mdをレンダリングします。bodyは各シーン180〜220字、本文内改行なしの1段落、箇条書きなしにしてください。
titlesはpattern_a/pattern_b/pattern_cの構造化JSON、scheduleはtime/topicの配列、descriptionはtext/countの構造化JSON、commentは3行の配列で返してください。metadataは空のオブジェクトで構いません（Python側でMarkdownに整形します）。
thumbnail_commentsはPattern A/B/Cの方向性・コメント・狙い・出力ファイル名・使用画像・needs_reviewを含めてください。
image_promptsは20件の配列にし、各要素に「シーン番号」「所属ブロック」「ブロックの役割」「重要ポイント番号」「ブロック内での役割」「前ブロックからの理解の流れ」「このシーンで伝える要点」「画像の目的」「推奨構図」「画面内テキスト」「前後画像との差別化」「使用画像」「入力画像チェック」「needs_review」「最終プロンプト」を必ず含めてください。
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
