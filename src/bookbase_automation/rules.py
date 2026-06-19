from __future__ import annotations

from pathlib import Path

RULE_FILES = [
    "script_rules.md",
    "title_rules.md",
    "image_rules.md",
    "image_rules_common.md",
    "image_block_rules.md",
    "input_asset_rules.md",
    "thumbnail_rules.md",
    "metadata_rules.md",
    "quality_checklist.md",
]


def load_rules(rules_dir: Path) -> str:
    sections: list[str] = []
    for filename in RULE_FILES:
        path = rules_dir / filename
        if path.exists():
            sections.append(f"# {filename}\n\n{path.read_text(encoding='utf-8').strip()}")
    scene_rules_dir = rules_dir / "image_scene_rules"
    if scene_rules_dir.exists():
        for path in sorted(scene_rules_dir.glob("scene_*.md")):
            sections.append(f"# image_scene_rules/{path.name}\n\n{path.read_text(encoding='utf-8').strip()}")
    return "\n\n---\n\n".join(sections)
