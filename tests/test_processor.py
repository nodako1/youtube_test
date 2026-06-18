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
    assert (out_dir / "04_thumbnail_ideas.md").exists()
    assert (out_dir / "05_image_prompts.json").exists()
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
