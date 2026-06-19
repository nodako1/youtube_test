from pathlib import Path
from zipfile import ZipFile

from bookbase_automation.assets import (
    build_asset_report,
    checks_for_bundle,
    discover_input_bundle,
    find_asset,
    read_rtfd_zip_text,
    validate_bundle,
)


def _write_rtfd_zip(path: Path, text: str) -> None:
    with ZipFile(path, "w") as archive:
        archive.writestr("TXT.rtf", r"{\rtf1 " + text + "}")


def test_find_asset_uses_extension_priority(tmp_path: Path):
    assets = tmp_path / "assets"
    assets.mkdir()
    (assets / "scene_03_current_book_cover.webp").write_text("webp", encoding="utf-8")
    (assets / "scene_03_current_book_cover.jpg").write_text("jpg", encoding="utf-8")

    assert find_asset(assets, "scene_03_current_book_cover") == assets / "scene_03_current_book_cover.webp"


def test_discover_input_bundle_classifies_input_root_files(tmp_path: Path):
    input_dir = tmp_path / "input"
    input_dir.mkdir()
    _write_rtfd_zip(input_dir / "20260619_否定しない言い換え事典.rtfd.zip", "今回の本")
    (input_dir / "20260619_book_cover.webp").write_text("cover", encoding="utf-8")
    (input_dir / "20260619_author.jpg").write_text("author", encoding="utf-8")
    _write_rtfd_zip(input_dir / "20260616_雑談する人はなぜかうまくいく.rtfd.zip", "過去動画")
    (input_dir / "20260616_book_cover.webp").write_text("related", encoding="utf-8")

    bundle = discover_input_bundle(input_dir, today_key="20260619")
    checks = checks_for_bundle(bundle)
    report = build_asset_report(checks, today_key=bundle.today_key)

    assert bundle.output_slug == "否定しない言い換え事典"
    assert checks[0].status == "OK"
    assert all(check.status == "OK" for check in checks)
    assert "【inputファイル判定】" in report
    assert "20260619_book_cover.webp" in report
    assert validate_bundle(bundle) == []


def test_discover_input_bundle_detects_duplicates(tmp_path: Path):
    input_dir = tmp_path / "input"
    input_dir.mkdir()
    _write_rtfd_zip(input_dir / "20260619_本A.rtfd.zip", "A")
    _write_rtfd_zip(input_dir / "20260619_本B.rtfd.zip", "B")
    (input_dir / "20260619_book_cover.webp").write_text("cover", encoding="utf-8")
    _write_rtfd_zip(input_dir / "20260616_過去本.rtfd.zip", "past")
    (input_dir / "20260616_book_cover.webp").write_text("related", encoding="utf-8")

    bundle = discover_input_bundle(input_dir, today_key="20260619")
    checks = checks_for_bundle(bundle)

    assert checks[0].status == "DUPLICATED"
    assert validate_bundle(bundle)


def test_read_rtfd_zip_text_extracts_rtf_text(tmp_path: Path):
    path = tmp_path / "20260619_本.rtfd.zip"
    _write_rtfd_zip(path, "これは本文です。")

    assert "これは本文です。" in read_rtfd_zip_text(path)
