from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass(frozen=True)
class CheckResult:
    name: str
    status: str
    detail: str


def _scene_bodies(script: str) -> list[str]:
    parts = re.split(r"^##\s+Scene\s+\d+\s*$", script, flags=re.MULTILINE)
    return [part.strip() for part in parts[1:] if part.strip()]


def build_quality_report(script: str, titles: str, image_prompts: str) -> str:
    scenes = _scene_bodies(script)
    total_chars = len(re.sub(r"\s+", "", script))
    results = [
        CheckResult("全20シーン", "OK" if len(scenes) == 20 else "NG", f"検出シーン数: {len(scenes)}"),
        CheckResult("全体3600〜4400字", "OK" if 3600 <= total_chars <= 4400 else "注意", f"現在の文字数目安: {total_chars}"),
        CheckResult("シーン8に登録促し", "OK" if len(scenes) >= 8 and "チャンネル登録" in scenes[7] else "注意", "シーン8を確認してください"),
        CheckResult("シーン12にコメント促し", "OK" if len(scenes) >= 12 and "コメント" in scenes[11] else "注意", "シーン12を確認してください"),
        CheckResult("シーン17が総評", "OK" if len(scenes) >= 17 and "総評" in scenes[16] else "注意", "シーン17を確認してください"),
        CheckResult("タイトル案A/B/C", "OK" if all(label in titles for label in ["A", "B", "C"]) else "注意", "3案あるか確認してください"),
        CheckResult("画像プロンプト20件", "OK" if image_prompts.count("scene") >= 20 else "注意", "20シーン分あるか確認してください"),
    ]
    lines = ["# 品質チェック結果", ""]
    for result in results:
        lines.append(f"- {result.name}: {result.status}（{result.detail}）")
    lines.extend(
        [
            "",
            "## 修正推奨",
            "- 注意またはNGの項目がある場合は、動画作成前にKoichiさんが内容を確認してください。",
            "- 自動生成結果は最終稿ではなく、品質担保のための確認前提の下書きです。",
        ]
    )
    return "\n".join(lines) + "\n"
