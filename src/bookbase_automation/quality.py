from __future__ import annotations

import re
from dataclasses import dataclass

SCENE_MIN_CHARS = 180
SCENE_MAX_CHARS = 220
TOTAL_MIN_CHARS = 3600
TOTAL_MAX_CHARS = 4400
DESCRIPTION_MIN_CHARS = 50
DESCRIPTION_MAX_CHARS = 60
SCENE_19_PREFIX = "最後に、今日からできる一歩を整理します。"


@dataclass(frozen=True)
class CheckResult:
    name: str
    status: str
    detail: str


def _compact_length(text: str) -> int:
    return len(re.sub(r"\s+", "", text))


def _scene_bodies(script: str) -> list[str]:
    parts = re.split(r"^##\s+Scene\s+\d+\s*$", script, flags=re.MULTILINE)
    return [part.strip() for part in parts[1:] if part.strip()]


def _title_hooks(titles: str) -> list[str]:
    return [hook.strip() for hook in re.findall(r"【([^】]+)】", titles)]


def build_quality_report(script: str, titles: str, image_prompts: str, description: str = "") -> str:
    scenes = _scene_bodies(script)
    scene_lengths = [_compact_length(scene) for scene in scenes]
    total_chars = sum(scene_lengths)
    out_of_range = [
        f"Scene {index:02d}: {length}字"
        for index, length in enumerate(scene_lengths, start=1)
        if not SCENE_MIN_CHARS <= length <= SCENE_MAX_CHARS
    ]
    hooks = _title_hooks(titles)
    duplicated_hooks = sorted({hook for hook in hooks if hooks.count(hook) > 1})
    description_length = _compact_length(description)
    scene_19 = scenes[18] if len(scenes) >= 19 else ""

    results = [
        CheckResult("全20シーン", "OK" if len(scenes) == 20 else "NG", f"検出シーン数: {len(scenes)}"),
        CheckResult(
            "各シーン180〜220字",
            "OK" if len(scenes) == 20 and not out_of_range else "NG",
            "全シーン範囲内" if not out_of_range else ", ".join(out_of_range),
        ),
        CheckResult(
            "全体3600〜4400字",
            "OK" if TOTAL_MIN_CHARS <= total_chars <= TOTAL_MAX_CHARS else "NG",
            f"現在の文字数目安: {total_chars}",
        ),
        CheckResult(
            "50〜60文字説明",
            "OK" if DESCRIPTION_MIN_CHARS <= description_length <= DESCRIPTION_MAX_CHARS else "NG",
            f"現在の説明文字数: {description_length}",
        ),
        CheckResult("シーン8に登録促し", "OK" if len(scenes) >= 8 and "チャンネル登録" in scenes[7] else "NG", "シーン8を確認してください"),
        CheckResult("シーン12にコメント促し", "OK" if len(scenes) >= 12 and "コメント" in scenes[11] else "NG", "シーン12を確認してください"),
        CheckResult("シーン17が総評", "OK" if len(scenes) >= 17 and "総評" in scenes[16] else "NG", "シーン17を確認してください"),
        CheckResult(
            "シーン19開始文固定",
            "OK" if scene_19.startswith(SCENE_19_PREFIX) else "NG",
            f"必須開始文: {SCENE_19_PREFIX}",
        ),
        CheckResult("タイトル案A/B/C", "OK" if all(label in titles for label in ["A", "B", "C"]) else "NG", "3案あるか確認してください"),
        CheckResult(
            "タイトルの【】フック重複",
            "OK" if hooks and not duplicated_hooks else "NG",
            "重複なし" if hooks and not duplicated_hooks else f"重複または未検出: {', '.join(duplicated_hooks) or 'フックなし'}",
        ),
        CheckResult("画像プロンプト20件", "OK" if image_prompts.count("scene") >= 20 else "NG", "20シーン分あるか確認してください"),
    ]
    lines = ["# 品質チェック結果", ""]
    for result in results:
        lines.append(f"- {result.name}: {result.status}（{result.detail}）")
    lines.extend(
        [
            "",
            "## 修正推奨",
            "- NGの項目がある場合は、動画作成前にKoichiさんが内容を確認し、必要に応じて再生成または手修正してください。",
            "- 自動生成結果は最終稿ではなく、品質担保のための確認前提の下書きです。",
        ]
    )
    return "\n".join(lines) + "\n"
