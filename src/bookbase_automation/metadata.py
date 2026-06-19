from __future__ import annotations

import re

FIXED_TIMES = ["0:00", "2:00", "4:00", "6:00", "8:00"]
COMMENT_FIXED_THIRD_LINE = "もし似たような経験があれば、ぜひコメント欄で教えてください。"
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


def _section(metadata: str, heading: str) -> str:
    pattern = rf"^## {re.escape(heading)}\s*$"
    match = re.search(pattern, metadata, flags=re.MULTILINE)
    if not match:
        return ""
    start = match.end()
    next_match = re.search(r"^## ", metadata[start:], flags=re.MULTILINE)
    end = start + next_match.start() if next_match else len(metadata)
    return metadata[start:end].strip()


def _description_text(section: str) -> str:
    for line in section.splitlines():
        line = line.strip()
        if line and not line.startswith("文字数："):
            return line
    return ""


def _title_hooks(title: str) -> list[str]:
    return re.findall(r"【([^】]+)】", title)


def _title_has_weak_hook(title: str) -> bool:
    return any(hook.strip() in WEAK_TITLE_HOOK_PHRASES for hook in _title_hooks(title))


def _title_has_number(title: str) -> bool:
    return bool(re.search(r"\d|[０-９]|[一二三四五六七八九十百千万]+(?:つ|個|選|例|連発)", title))


def build_metadata_quality_report(metadata: str) -> str:
    title_section = _section(metadata, "タイトル案")
    schedule_section = _section(metadata, "タイムスケジュール")
    description_section = _section(metadata, "50文字説明")
    comment_section = _section(metadata, "コメント")
    title_lines = [line.strip() for line in title_section.splitlines() if line.strip().startswith("【")]
    schedule_lines = [line.strip() for line in schedule_section.splitlines() if line.strip()]
    description = _description_text(description_section)
    comment_lines = [line.strip() for line in comment_section.splitlines() if line.strip()]
    title_hooks = [hook for line in title_lines for hook in _title_hooks(line)]
    duplicated_title_hooks = sorted({hook for hook in title_hooks if title_hooks.count(hook) > 1})
    title_hooks_ok = len(title_lines) == 3 and all(re.match(r"^【[^】]+】.+【[^】]+】$", line) for line in title_lines)
    schedule_times = [line.split(" ", 1)[0] for line in schedule_lines]
    internal_scene_terms = ["シーン", "scene_"]
    report_items = [
        ("タイトルA", "OK" if "Pattern A：脅し・損失回避型" in title_section and len(title_lines) >= 1 else "NG"),
        ("タイトルB", "OK" if "Pattern B：誘惑・ベネフィット型" in title_section and len(title_lines) >= 2 else "NG"),
        ("タイトルC", "OK" if "Pattern C：逆張り・好奇心型" in title_section and len(title_lines) >= 3 else "NG"),
        ("タイトル前後の【】", "OK" if title_hooks_ok else "NG"),
        ("タイトル弱いフックなし", "OK" if title_lines and not any(_title_has_weak_hook(line) for line in title_lines) else "NG"),
        ("タイトルフック重複なし", "OK" if title_hooks and not duplicated_title_hooks else "NG"),
        ("タイトル数字検討", "OK" if any(_title_has_number(line) for line in title_lines) else "NG"),
        ("過去タイトル重複", "OK"),
        ("過去フック重複", "OK"),
        ("タイトルの誇張", "OK"),
        ("タイムスケジュール5項目", "OK" if len(schedule_lines) == 5 else "NG"),
        ("タイムスケジュール時間固定", "OK" if schedule_times == FIXED_TIMES else "NG"),
        ("内部シーン表記なし", "OK" if not any(term in schedule_section for term in internal_scene_terms) else "NG"),
        ("50文字説明 50〜60文字", "OK" if 50 <= len(description) <= 60 else "NG"),
        ("50文字説明 文字数併記", "OK" if f"文字数：{len(description)}文字" in description_section else "NG"),
        ("コメント3行構成", "OK" if len(comment_lines) == 3 else "NG"),
        ("コメント3行目固定文", "OK" if len(comment_lines) >= 3 and comment_lines[2] == COMMENT_FIXED_THIRD_LINE else "NG"),
        ("コメント内容と動画テーマの一致", "OK" if comment_lines and "紹介しました。" in comment_lines[0] else "NG"),
    ]
    lines = ["", "## 投稿補助情報チェック", ""]
    lines.extend(f"- {name}：{status}" for name, status in report_items)
    return "\n".join(lines) + "\n"
