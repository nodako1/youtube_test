import json
from datetime import date
from pathlib import Path

from bookbase_automation.generator import generate_fallback_assets
from bookbase_automation.image_generation import build_image_targets, composite_scene03_book_cover
from bookbase_automation.input_assets import FlatInputSelection
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


def test_scene_02_fallback_prompt_is_structured_and_text_limited():
    assets = generate_fallback_assets("本のメモ", "テスト本")
    prompts = json.loads(assets.image_prompts)
    scene_02 = prompts[1]

    assert scene_02["scene"] == 2
    assert scene_02["scene_role"] == "クイズ正解発表とテーマへの橋渡し"
    assert scene_02["core_message"]
    assert scene_02["exact_text_elements"][0].startswith("正解は")
    assert len(scene_02["exact_text_elements"]) == 3
    assert "Use only the following Japanese text elements exactly as written" in scene_02["final_prompt"]
    assert "Correct answer B" not in scene_02["final_prompt"]
    assert "Avoid repeating Scene 01 composition" in scene_02["final_prompt"]


def test_scene_03_fallback_prompt_requires_real_cover_composite():
    assets = generate_fallback_assets("本のメモ", "否定しない言い換え事典")
    prompts = json.loads(assets.image_prompts)
    scene_03 = prompts[2]

    assert scene_03["scene"] == 3
    assert scene_03["reference_image_required"] is True
    assert scene_03["exact_text_elements"][0] == "今回の一冊"
    assert scene_03["exact_text_elements"][1]
    assert scene_03["post_process"]["composite_real_book_cover"] is True
    assert "Do not draw or recreate the book cover" in scene_03["final_prompt"]
    assert "Do not draw or recreate the book cover" in scene_03["final_prompt"]


def test_scene_03_target_keeps_cover_reference_but_prompt_generates_background(tmp_path: Path):
    cover = tmp_path / "20260619_book_cover.webp"
    cover.write_bytes(b"cover")
    selection = FlatInputSelection(
        run_date=date(2026, 6, 19),
        date_key="20260619",
        current_sources=[],
        current_book_covers=[cover],
        current_authors=[],
        related_sources=[],
        related_book_covers=[],
    )
    assets = generate_fallback_assets("本のメモ", "否定しない言い換え事典")

    [target] = build_image_targets(tmp_path / "output", assets.image_prompts, selection, scene03_only=True)

    assert target.references == (cover,)
    assert "actual book cover will be composited later" in target.prompt
    assert "Leave prominent clean space" in target.prompt


def test_scene_04_prompt_uses_author_reference_only_when_available(tmp_path: Path):
    from bookbase_automation.assets import AssetCheck

    missing_assets = generate_fallback_assets("本のメモ", "否定しない言い換え事典")
    missing_scene_04 = json.loads(missing_assets.image_prompts)[3]
    assert missing_scene_04["scene"] == 4
    assert missing_scene_04["exact_text_elements"][:2] == ["著者紹介", "3つの重要ポイント"]
    assert all(text[0] in "①②③" for text in missing_scene_04["exact_text_elements"][2:])
    assert "No author reference is available" in missing_scene_04["final_prompt"]
    assert "do not imagine a face" in missing_scene_04["final_prompt"]
    assert "silhouette" in missing_scene_04["final_prompt"]

    check = AssetCheck(4, "scene_04_author_reference", "著者参考", "OK", "assets/scene_04_author_reference.jpg", "使用画像")
    referenced_assets = generate_fallback_assets("本のメモ", "否定しない言い換え事典", [check])
    referenced_scene_04 = json.loads(referenced_assets.image_prompts)[3]
    assert referenced_scene_04["reference_image_path"] == "assets/scene_04_author_reference.jpg"
    assert "refined watercolor illustration" in referenced_scene_04["final_prompt"]
    assert "silhouette" not in referenced_scene_04["final_prompt"].lower()



def test_scene_05_fallback_prompt_introduces_key_point_1_psychology():
    assets = generate_fallback_assets("本のメモ", "否定しない言い換え事典")
    prompts = json.loads(assets.image_prompts)
    scene_05 = prompts[4]

    assert scene_05["scene"] == 5
    assert scene_05["scene_role"] == "重要ポイント①の導入"
    assert scene_05["core_message"]
    assert scene_05["exact_text_elements"][0] == "重要ポイント①"
    assert "Use only the following Japanese text elements exactly as written" in scene_05["final_prompt"]
    assert "Watercolor scene of a business person at a desk" not in scene_05["final_prompt"]
    assert "One image, one message" in scene_05["final_prompt"]

def test_composite_scene_03_book_cover_preserves_16_9_output(tmp_path: Path):
    import pytest

    Image = pytest.importorskip("PIL.Image")

    background = tmp_path / "background.png"
    cover = tmp_path / "cover.webp"
    Image.new("RGB", (1536, 1024), (240, 235, 225)).save(background)
    Image.new("RGB", (600, 900), (20, 120, 160)).save(cover)

    image_bytes = composite_scene03_book_cover(background.read_bytes(), cover)
    output = tmp_path / "scene_03.png"
    output.write_bytes(image_bytes)
    rendered = Image.open(output)

    assert rendered.size == (1536, 864)
