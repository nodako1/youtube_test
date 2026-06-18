from __future__ import annotations

from pathlib import Path

RULE_FILES = [
    "script_rules.md",
    "title_rules.md",
    "image_rules.md",
    "thumbnail_rules.md",
    "quality_checklist.md",
]


def load_rules(rules_dir: Path) -> str:
    sections: list[str] = []
    for filename in RULE_FILES:
        path = rules_dir / filename
        if path.exists():
            sections.append(f"# {filename}\n\n{path.read_text(encoding='utf-8').strip()}")
    return "\n\n---\n\n".join(sections)
