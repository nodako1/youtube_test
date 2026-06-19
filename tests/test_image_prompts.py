import json

from bookbase_automation.generator import generate_fallback_assets
from bookbase_automation.rules import load_rules


def test_fallback_image_prompts_include_block_metadata():
    assets = generate_fallback_assets("本のメモ", "テスト本")
    prompts = json.loads(assets.image_prompts)

    assert len(prompts) == 20
    assert prompts[4]["所属ブロック"] == "シーン5〜8：重要ポイント1"
    assert prompts[8]["重要ポイント番号"] == "重要ポイント2"
    assert prompts[12]["推奨構図"].startswith("整理されたデスク")
    assert "Book Base logo" in prompts[0]["最終プロンプト"]
    assert "前後画像との差別化" in prompts[0]


def test_load_rules_includes_image_block_and_scene_rules(tmp_path):
    rules_dir = tmp_path / "rules"
    scene_dir = rules_dir / "image_scene_rules"
    scene_dir.mkdir(parents=True)
    (rules_dir / "script_rules.md").write_text("script", encoding="utf-8")
    (rules_dir / "image_rules_common.md").write_text("common", encoding="utf-8")
    (rules_dir / "image_block_rules.md").write_text("block", encoding="utf-8")
    (scene_dir / "scene_05.md").write_text("scene five", encoding="utf-8")

    loaded = load_rules(rules_dir)

    assert "# image_rules_common.md" in loaded
    assert "# image_block_rules.md" in loaded
    assert "# image_scene_rules/scene_05.md" in loaded
