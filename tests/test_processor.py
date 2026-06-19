from pathlib import Path
from zipfile import ZipFile

from bookbase_automation.assets import today_key_jst
from bookbase_automation.config import AppConfig
from bookbase_automation.processor import run


def _write_rtfd_zip(path: Path, text: str) -> None:
    with ZipFile(path, "w") as archive:
        archive.writestr("TXT.rtf", r"{\rtf1 " + text + "}")


def _seed_valid_flat_input(config: AppConfig, today_key: str) -> None:
    _write_rtfd_zip(config.input_dir / f"{today_key}_テスト本.rtfd.zip", "仕事で使える本の要点です。判断、習慣、行動について説明します。")
    (config.input_dir / f"{today_key}_book_cover.webp").write_text("cover", encoding="utf-8")
    (config.input_dir / f"{today_key}_author.jpg").write_text("author", encoding="utf-8")
    _write_rtfd_zip(config.input_dir / "20200101_過去本.rtfd.zip", "過去動画の内容です。今回の本と仕事の判断でつながります。")
    (config.input_dir / "20200101_book_cover.webp").write_text("related", encoding="utf-8")


def test_run_processes_input_root_files_and_archives_all_used_files(tmp_path: Path):
    config = AppConfig.from_root(tmp_path, allow_fallback=True)
    config.ensure_directories()
    today_key = today_key_jst()
    _seed_valid_flat_input(config, today_key)

    outputs = run(config)

    assert len(outputs) == 1
    out_dir = outputs[0]
    assert (out_dir / "01_script.md").exists()
    assert (out_dir / "02_titles.md").exists()
    assert (out_dir / "03_description.md").exists()
    assert (out_dir / "metadata.md").exists()
    assert (out_dir / "04_thumbnail_ideas.md").exists()
    assert (out_dir / "06_thumbnail_comments.md").exists()
    assert (out_dir / "05_image_prompts.json").exists()
    assert (out_dir / "research" / "scene_11_story_person.md").exists()
    assert (out_dir / "research" / "scene_15_quote_person.md").exists()
    assert (out_dir / "quality_report.md").exists()
    assert not list(config.input_dir.iterdir())
    assert len(list(config.archive_dir.glob("**/*"))) >= 5


def test_run_does_nothing_without_input(tmp_path: Path):
    config = AppConfig.from_root(tmp_path, allow_fallback=True)
    config.ensure_directories()

    assert run(config) == []


def test_run_requires_ai_or_explicit_fallback(tmp_path: Path):
    config = AppConfig.from_root(tmp_path)
    config.ensure_directories()
    today_key = today_key_jst()
    _seed_valid_flat_input(config, today_key)

    try:
        run(config)
    except RuntimeError as exc:
        assert "--use-ai" in str(exc)
    else:
        raise AssertionError("AIなし本番実行が許可されています")
    assert list(config.error_dir.glob("**/error_report.md"))


def test_run_writes_input_and_research_quality_checks(tmp_path: Path):
    config = AppConfig.from_root(tmp_path, allow_fallback=True)
    config.ensure_directories()
    today_key = today_key_jst()
    _seed_valid_flat_input(config, today_key)

    out_dir = run(config)[0]

    report = (out_dir / "quality_report.md").read_text(encoding="utf-8")
    metadata = (out_dir / "metadata.md").read_text(encoding="utf-8")
    prompts = (out_dir / "05_image_prompts.json").read_text(encoding="utf-8")
    thumbnail_comments = (out_dir / "06_thumbnail_comments.md").read_text(encoding="utf-8")
    research_11 = (out_dir / "research" / "scene_11_story_person.md").read_text(encoding="utf-8")
    assert "投稿補助情報チェック" in report
    assert "【inputファイル判定】" in report
    assert "自動取得情報チェック" in report
    assert "current_manuscript：OK" in report
    assert "scene_04_author_reference：OK" in report
    assert "scene_19_related_book_cover：OK" in report
    assert "# 投稿補助情報" in metadata
    assert f"{today_key}_book_cover.webp" in prompts
    assert "人物画像未取得の場合" in prompts
    assert "thumbnail_A_loss_aversion.png" in thumbnail_comments
    assert "NEEDS_REVIEW" in research_11
