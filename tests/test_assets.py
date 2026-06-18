from pathlib import Path

from bookbase_automation.assets import build_asset_report, check_input_assets, find_asset


def test_find_asset_uses_extension_priority(tmp_path: Path):
    assets = tmp_path / "assets"
    assets.mkdir()
    (assets / "scene_03_current_book_cover.webp").write_text("webp", encoding="utf-8")
    (assets / "scene_03_current_book_cover.jpg").write_text("jpg", encoding="utf-8")

    assert find_asset(assets, "scene_03_current_book_cover") == assets / "scene_03_current_book_cover.jpg"


def test_check_input_assets_uses_latest_required_and_optional_files(tmp_path: Path):
    assets = tmp_path / "assets"
    assets.mkdir()
    (tmp_path / "source.txt").write_text("memo", encoding="utf-8")
    (tmp_path / "scene_19_related_video.txt").write_text("関連動画タイトル：テスト", encoding="utf-8")
    (assets / "scene_03_current_book_cover.png").write_text("png", encoding="utf-8")

    checks = check_input_assets(tmp_path)
    report = build_asset_report(checks)

    by_key = {check.key: check for check in checks}
    assert by_key["source"].status == "OK"
    assert by_key["scene_19_related_video"].status == "OK"
    assert by_key["scene_03_current_book_cover"].path == "assets/scene_03_current_book_cover.png"
    assert by_key["scene_04_author_reference"].status == "OPTIONAL"
    assert by_key["scene_19_related_book_cover"].status == "MISSING"
    assert "scene_11_story_person_reference" not in report
    assert "scene_15_quote_person_reference" not in report
    assert "scene_19_related_book_cover：MISSING" in report
