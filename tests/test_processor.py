from pathlib import Path

from bookbase_automation.config import AppConfig
from bookbase_automation.processor import run


def _write_rtfd(path: Path, text: str) -> None:
    from zipfile import ZipFile

    with ZipFile(path, "w") as archive:
        archive.writestr("TXT.rtf", text)


def test_run_does_nothing_without_input(tmp_path: Path):
    config = AppConfig.from_root(tmp_path, allow_fallback=True)
    config.ensure_directories()

    assert run(config) == []


def test_run_requires_ai_or_explicit_fallback_for_flat_input(tmp_path: Path):
    from datetime import date

    config = AppConfig.from_root(tmp_path)
    config.ensure_directories()
    today = date.today().strftime("%Y%m%d")
    current = config.input_dir / f"{today}_テスト本.rtfd.zip"
    _write_rtfd(current, "本文")

    try:
        run(config)
    except RuntimeError as exc:
        assert "--use-ai" in str(exc)
    else:
        raise AssertionError("AIなし本番実行が許可されています")
    assert (config.error_dir / f"{today}_テスト本" / "error_report.md").exists()


def test_run_processes_flat_rtfd_inputs_and_writes_scene03_prompt(tmp_path: Path):
    from datetime import date

    config = AppConfig.from_root(tmp_path, allow_fallback=True, image_scene03_only=True)
    config.ensure_directories()
    today = date.today().strftime("%Y%m%d")
    current = config.input_dir / f"{today}_否定しない言い換え事典.rtfd.zip"
    related = config.input_dir / "20260616_雑談する人はなぜかうまくいく.rtfd.zip"
    _write_rtfd(current, "否定しない言い換えの読書メモです。")
    _write_rtfd(related, "雑談に関する過去動画メモです。")
    (config.input_dir / f"{today}_book_cover.webp").write_bytes(b"fake cover")
    (config.input_dir / f"{today}_author.jpg").write_bytes(b"fake author")
    (config.input_dir / "20260616_book_cover.webp").write_bytes(b"fake related cover")

    outputs = run(config)

    out_dir = outputs[0]
    assert (out_dir / "script.md").exists()
    assert (out_dir / "image_prompts.md").exists()
    assert (out_dir / "failed_images.md").read_text(encoding="utf-8").startswith("# failed_images.md")
    report = (out_dir / "quality_report.md").read_text(encoding="utf-8")
    prompts = (out_dir / "image_prompts.md").read_text(encoding="utf-8")
    assert "【inputファイル判定】" in report
    assert "今回の原稿材料：OK" in report
    assert "今回のブックカバー：OK" in report
    assert "scene_03：NEEDS_REVIEW" in report
    assert "scene_03.png" in prompts
    assert "book_cover" in prompts
    assert out_dir.name.startswith(today)
    assert not list(config.input_dir.iterdir())
    archived_files = list((config.archive_dir / out_dir.name).iterdir())
    assert {path.name for path in archived_files} >= {current.name, related.name, f"{today}_book_cover.webp"}


def test_flat_image_generation_without_api_key_moves_inputs_to_error(tmp_path: Path, monkeypatch):
    from datetime import date

    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    config = AppConfig.from_root(tmp_path, allow_fallback=True, generate_images=True, image_scene03_only=True)
    config.ensure_directories()
    today = date.today().strftime("%Y%m%d")
    current = config.input_dir / f"{today}_テスト本.rtfd.zip"
    _write_rtfd(current, "テスト本文です。")
    (config.input_dir / f"{today}_book_cover.webp").write_bytes(b"fake cover")

    try:
        run(config)
    except RuntimeError as exc:
        assert "OPENAI_API_KEY" in str(exc)
    else:
        raise AssertionError("OPENAI_API_KEYなしで画像生成が成功しています")

    error_dir = config.error_dir / f"{today}_テスト本"
    assert (error_dir / "error_report.md").exists()
    assert (error_dir / current.name).exists()
    assert not any(path.name.startswith(today) for path in config.input_dir.iterdir())
