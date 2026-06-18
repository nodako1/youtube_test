from pathlib import Path

from bookbase_automation.config import AppConfig
from bookbase_automation.processor import run


def test_run_processes_one_input_file(tmp_path: Path):
    config = AppConfig.from_root(tmp_path, allow_fallback=True)
    config.ensure_directories()
    (config.input_dir / "20260618_テスト本.txt").write_text("仕事で使える本の要点です。判断、習慣、行動について説明します。", encoding="utf-8")

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
    assert not list(config.input_dir.glob("*.txt"))
    assert list(config.archive_dir.glob("*.txt"))


def test_run_does_nothing_without_input(tmp_path: Path):
    config = AppConfig.from_root(tmp_path, allow_fallback=True)
    config.ensure_directories()

    assert run(config) == []


def test_run_requires_ai_or_explicit_fallback(tmp_path: Path):
    config = AppConfig.from_root(tmp_path)
    config.ensure_directories()
    (config.input_dir / "20260618_テスト本.txt").write_text("本文", encoding="utf-8")

    try:
        run(config)
    except RuntimeError as exc:
        assert "--use-ai" in str(exc)
    else:
        raise AssertionError("AIなし本番実行が許可されています")
    assert list(config.error_dir.glob("2026-06-18_テスト本/*.txt"))


def test_run_processes_folder_input_with_latest_assets_and_related_video(tmp_path: Path):
    config = AppConfig.from_root(tmp_path, allow_fallback=True)
    config.ensure_directories()
    input_folder = config.input_dir / "20260618_test_book"
    assets = input_folder / "assets"
    assets.mkdir(parents=True)
    (input_folder / "source.txt").write_text("仕事で使える本の要点です。", encoding="utf-8")
    (input_folder / "scene_19_related_video.txt").write_text(
        "関連動画タイトル：お金はこれで増やせます\n今回の動画とのつながり：判断の整理がお金の不安対策とつながるため。",
        encoding="utf-8",
    )
    (assets / "scene_03_current_book_cover.jpg").write_text("image", encoding="utf-8")
    (assets / "scene_19_related_book_cover.png").write_text("image", encoding="utf-8")

    outputs = run(config)

    out_dir = outputs[0]
    report = (out_dir / "quality_report.md").read_text(encoding="utf-8")
    metadata = (out_dir / "metadata.md").read_text(encoding="utf-8")
    prompts = (out_dir / "05_image_prompts.json").read_text(encoding="utf-8")
    thumbnail_comments = (out_dir / "06_thumbnail_comments.md").read_text(encoding="utf-8")
    research_11 = (out_dir / "research" / "scene_11_story_person.md").read_text(encoding="utf-8")
    assert "投稿補助情報チェック" in report
    assert "自動取得情報チェック" in report
    assert "# 投稿補助情報" in metadata
    assert "source：OK" in report
    assert "scene_19_related_video：OK" in report
    assert "scene_03_current_book_cover：OK" in report
    assert "scene_04_author_reference：OPTIONAL" in report
    assert "scene_19_related_book_cover：OK" in report
    assert "scene_11_story_person_reference" not in report
    assert "scene_15_quote_person_reference" not in report
    assert "assets/scene_03_current_book_cover.jpg" in prompts
    assert "人物画像未取得の場合" in prompts
    assert "thumbnail_A_loss_aversion.png" in thumbnail_comments
    assert "NEEDS_REVIEW" in research_11
    assert not input_folder.exists()
    assert (config.archive_dir / "20260618_test_book" / "source.txt").exists()
