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
    assert prompts[12]["推奨構図"].startswith("構図C：実践への橋渡し型")
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


def test_scene_06_fallback_prompt_explains_key_point_1_mechanism():
    assets = generate_fallback_assets("本のメモ", "否定しない言い換え事典")
    prompts = json.loads(assets.image_prompts)
    scene_06 = prompts[5]

    assert scene_06["scene"] == 6
    assert scene_06["fixed_role"] == "重要ポイント①の理由・背景・仕組み説明"
    assert scene_06["scene_role"] == "重要ポイント①の理由・背景・仕組み説明"
    assert scene_06["point_1_label"]
    assert scene_06["scene_06_core_message"]
    assert scene_06["visual_structure"] in {
        "cause_to_effect",
        "before_after",
        "hidden_mechanism",
        "obstacle_and_solution",
        "contrast",
    }
    assert 1 <= len(scene_06["exact_text_elements"]) <= 3
    assert all(len(label) <= 15 for label in scene_06["exact_text_elements"])
    assert "Use only the following Japanese text elements exactly as written" in scene_06["final_prompt"]
    assert "Do not create a generic business person image" in scene_06["final_prompt"]
    assert "avoid generic emotional icons" in scene_06["final_prompt"]
    assert "Watercolor illustration of a business person with emotional expression icons" not in scene_06["final_prompt"]


def test_scene_07_fallback_prompt_reinforces_key_point_1_with_variable_evidence():
    assets = generate_fallback_assets("本のメモ", "否定しない言い換え事典")
    prompts = json.loads(assets.image_prompts)
    scene_07 = prompts[6]

    assert scene_07["scene"] == 7
    assert scene_07["fixed_role"] == "重要ポイント①の根拠補強"
    assert scene_07["point_1_label"]
    assert scene_07["scene_07_core_message"]
    assert scene_07["evidence_type"] in {
        "research",
        "survey",
        "public_data",
        "report",
        "experiment",
        "case_data",
        "book_claim",
    }
    assert scene_07["source_confidence"] in {"verified", "needs_review", "unavailable"}
    assert scene_07["visual_structure"] in {
        "evidence_card",
        "data_report",
        "research_board",
        "document_review",
        "chart_focus",
    }
    assert len(scene_07["exact_text_elements"]) <= 3
    assert "Do not hard-code psychology research" in scene_07["final_prompt"]
    assert "Do not invent specific numbers" in scene_07["final_prompt"]
    assert "avoid repeating the Scene 06 composition" in scene_07["final_prompt"]
    assert "psychology research data" not in scene_07["final_prompt"]
    assert "科学的にも納得" not in assets.script


def test_scene_08_fallback_prompt_uses_elegant_japanese_subscription_cta():
    assets = generate_fallback_assets("本のメモ", "否定しない言い換え事典")
    prompts = json.loads(assets.image_prompts)
    scene_08 = prompts[7]

    assert scene_08["scene"] == 8
    assert scene_08["fixed_role"] == "チャンネル登録CTA"
    assert scene_08["core_message"] == "Book Baseの学びを継続して受け取るための自然な登録案内"
    assert scene_08["cta_tone"] == "elegant_non_pushy"
    assert scene_08["exact_text_elements"] == ["チャンネル登録", "本の学びを仕事へ"]
    assert "Use only the following Japanese text elements exactly as written" in scene_08["final_prompt"]
    assert "Avoid English text" in scene_08["final_prompt"]
    assert "avoid red flashy subscribe-button design" in scene_08["final_prompt"]
    assert "avoid repeating the Scene 07 report/data composition" in scene_08["final_prompt"]
    assert "Continue learning" not in scene_08["final_prompt"]
    assert "Subscribe" not in scene_08["final_prompt"]
    assert "否定しない言い換え事典" not in scene_08["final_prompt"]

def test_scene_09_fallback_prompt_introduces_key_point_2_dynamically():
    assets = generate_fallback_assets("本のメモ", "否定しない言い換え事典")
    prompts = json.loads(assets.image_prompts)
    scene_09 = prompts[8]

    assert scene_09["scene"] == 9
    assert scene_09["fixed_role"] == "重要ポイント②の導入"
    assert scene_09["point_2_label"]
    assert scene_09["point_2_core_message"]
    assert scene_09["point_2_type"] in {"method", "mindset", "habit", "process", "contrast", "skill", "framework"}
    assert scene_09["exact_text_elements"][0] == "重要ポイント②"
    assert len(scene_09["exact_text_elements"]) <= 3
    assert "Use only the following Japanese text elements exactly as written" in scene_09["final_prompt"]
    assert "Do not create a generic business conversation image" in scene_09["final_prompt"]
    assert "avoid generic conversation scenes" in scene_09["final_prompt"]
    assert "avoid repeating the Scene 08 CTA composition or Scene 05 Key Point 1 composition" in scene_09["final_prompt"]
    assert "two business people in conversation" not in scene_09["final_prompt"]
    assert "shift of perspective" not in scene_09["final_prompt"]

def test_scene_10_fallback_prompt_concretizes_key_point_2_dynamically():
    assets = generate_fallback_assets("本のメモ", "否定しない言い換え事典")
    prompts = json.loads(assets.image_prompts)
    scene_10 = prompts[9]

    assert scene_10["scene"] == 10
    assert scene_10["fixed_role"] == "重要ポイント②の具体化"
    assert scene_10["point_2_label"]
    assert scene_10["scene_10_core_message"]
    assert scene_10["example_label"]
    assert scene_10["application_label"]
    assert scene_10["result_label"]
    assert scene_10["visual_structure"] in {"before_after", "step_demo", "example_scene", "comparison", "action_map", "framework_demo"}
    assert len(scene_10["exact_text_elements"]) <= 3
    assert "Use only the following Japanese text elements exactly as written" in scene_10["final_prompt"]
    assert "Do not create a generic cause-and-effect flowchart unless the current script actually requires it" in scene_10["final_prompt"]
    assert "avoid generic split-screen flowcharts" in scene_10["final_prompt"]
    assert "avoid generic business people" in scene_10["final_prompt"]
    assert "avoid repeating the Scene 09 composition" in scene_10["final_prompt"]
    assert "Watercolor style split-screen showing cause and effect flowchart alongside business people" not in scene_10["final_prompt"]


def test_scene_12_fallback_prompt_uses_comment_cta_experience_label():
    assets = generate_fallback_assets("本のメモ", "否定しない言い換え事典")
    prompts = json.loads(assets.image_prompts)
    scene_12 = prompts[11]

    assert scene_12["scene"] == 12
    assert scene_12["fixed_role"] == "コメントCTA"
    assert scene_12["comment_question"]
    assert scene_12["experience_label"]
    assert scene_12["cta_label"] == "コメントで教えてください"
    assert scene_12["visual_structure"] in {"comment_card", "speech_bubbles", "viewer_participation", "notebook_comment"}
    assert scene_12["exact_text_elements"] == ["あなたの経験は？", scene_12["experience_label"], "コメントで教えてください"]
    assert "Current comment question:" in scene_12["final_prompt"]
    assert "Experience label:" in scene_12["final_prompt"]
    assert "Use only the following Japanese text elements exactly as written" in scene_12["final_prompt"]
    assert "Avoid English text" in scene_12["final_prompt"]
    assert "avoid keyword-comment prompts" in scene_12["final_prompt"]
    assert "avoid repeating the Scene 08 subscription CTA composition" in scene_12["final_prompt"]
    assert "Similar experience?" not in scene_12["final_prompt"]
    assert "Subscribe" not in scene_12["final_prompt"]


def test_scene_16_fallback_prompt_guides_remaining_value_without_sales_language():
    assets = generate_fallback_assets("本のメモ", "否定しない言い換え事典")
    prompts = json.loads(assets.image_prompts)
    scene_16 = prompts[15]

    assert scene_16["scene"] == 16
    assert scene_16["fixed_role"] == "本書の残りの価値案内"
    assert scene_16["remaining_value_label"]
    assert scene_16["read_invitation_label"] == "本書を手に取る"
    assert scene_16["visual_mode"] in {
        "generic_book",
        "real_cover_composite",
        "reading_nook",
        "open_book",
        "desk_still_life",
    }
    assert 1 <= len(scene_16["exact_text_elements"]) <= 3
    assert "Use only the following Japanese text elements exactly as written" in scene_16["final_prompt"]
    assert "not a sales advertisement" in scene_16["final_prompt"]
    assert "Avoid clutter, avoid sales-like design, avoid purchase links" in scene_16["final_prompt"]
    assert "Amazon" not in scene_16["final_prompt"]
    assert "楽天" not in scene_16["final_prompt"]
    assert "概要欄リンク" not in scene_16["final_prompt"]


def test_scene_16_uses_real_cover_composite_when_cover_exists(tmp_path: Path):
    from bookbase_automation.assets import AssetCheck

    check = AssetCheck(3, "scene_03_current_book_cover", "今回紹介する本のブックカバー", "OK", "input/20260619_book_cover.webp", "input/YYYYMMDD_book_cover.* から動的に取得")
    assets = generate_fallback_assets("本のメモ", "否定しない言い換え事典", [check])
    scene_16 = json.loads(assets.image_prompts)[15]

    assert scene_16["visual_mode"] == "real_cover_composite"
    assert scene_16["book_cover_path"] == "input/20260619_book_cover.webp"
    assert scene_16["post_process"]["composite_real_book_cover"] is True
    assert "Do not draw or recreate the book cover" in scene_16["final_prompt"]
    assert "smaller and more subtle than in Scene 03" in scene_16["final_prompt"]

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
    targets = build_image_targets(tmp_path / "output", assets.image_prompts, selection)
    target_16 = next(target for target in targets if target.scene == 16)

    assert target_16.references == (cover,)
    assert "real_cover_composite" in target_16.prompt
