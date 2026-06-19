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


def test_run_processes_flat_rtfd_inputs_and_writes_scene03_prompt(tmp_path: Path):
    from datetime import date
    from zipfile import ZipFile

    target_date = date(2026, 6, 20)
    config = AppConfig.from_root(tmp_path, allow_fallback=True, image_scene03_only=True, target_date=target_date)
    config.ensure_directories()
    today = target_date.strftime("%Y%m%d")
    current = config.input_dir / f"{today}_否定しない言い換え事典.rtfd.zip"
    related = config.input_dir / "20260616_雑談する人はなぜかうまくいく.rtfd.zip"
    with ZipFile(current, "w") as archive:
        archive.writestr("TXT.rtf", "否定しない言い換えの読書メモです。")
    with ZipFile(related, "w") as archive:
        archive.writestr("TXT.rtf", "雑談に関する過去動画メモです。")
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
    assert "今回の原稿材料：OK" in report
    assert "今回のブックカバー：OK" in report
    assert "scene_03：NEEDS_REVIEW" in report
    assert "scene_03.png" in prompts
    assert "book_cover" in prompts
    assert not list(config.input_dir.iterdir())
    assert list(config.archive_dir.iterdir())


def test_flat_rtfd_target_date_override_and_error_details(tmp_path: Path):
    from datetime import date
    from zipfile import ZipFile

    config = AppConfig.from_root(tmp_path, allow_fallback=True, target_date=date(2026, 6, 20))
    config.ensure_directories()
    current = config.input_dir / "20260620_対象本.rtfd.zip"
    related = config.input_dir / "20260616_関連本.rtfd.zip"
    with ZipFile(current, "w") as archive:
        archive.writestr("TXT.rtf", "対象本の読書メモです。")
    with ZipFile(related, "w") as archive:
        archive.writestr("TXT.rtf", "関連本の読書メモです。")
    (config.input_dir / "20260620_book_cover.webp").write_bytes(b"fake cover")
    (config.input_dir / "20260616_book_cover.webp").write_bytes(b"fake related cover")

    outputs = run(config)

    assert outputs[0].name.startswith("2026-06-20_対象本")
    report = (outputs[0] / "quality_report.md").read_text(encoding="utf-8")
    assert "今日の日付キー：20260620" in report


def test_flat_rtfd_missing_target_date_error_lists_target_and_found_files(tmp_path: Path):
    from datetime import date
    from zipfile import ZipFile

    config = AppConfig.from_root(tmp_path, allow_fallback=True, target_date=date(2026, 6, 20))
    config.ensure_directories()
    related = config.input_dir / "20260616_関連本.rtfd.zip"
    future = config.input_dir / "20260621_未来本.rtfd.zip"
    with ZipFile(related, "w") as archive:
        archive.writestr("TXT.rtf", "関連本の読書メモです。")
    with ZipFile(future, "w") as archive:
        archive.writestr("TXT.rtf", "未来本の読書メモです。")

    try:
        run(config)
    except RuntimeError as exc:
        message = str(exc)
    else:
        raise AssertionError("対象日のrtfd.zip欠落が許可されています")

    assert "今日の日付の .rtfd.zip が1件必要です。" in message
    assert "target_date: 20260620" in message
    assert "found_rtfd_zip_files:" in message
    assert "- input/20260616_関連本.rtfd.zip" in message
    assert "- input/20260621_未来本.rtfd.zip" in message


def test_generate_assets_only_copies_reference_assets_and_does_not_generate_images(tmp_path: Path, monkeypatch):
    from datetime import date
    from zipfile import ZipFile

    def fail_generate_images(*args, **kwargs):
        raise AssertionError("image API should not be called")

    monkeypatch.setattr("bookbase_automation.processor.generate_images", fail_generate_images)
    config = AppConfig.from_root(tmp_path, allow_fallback=True, generate_assets_only=True, generate_images=True, target_date=date(2026, 6, 20))
    config.ensure_directories()
    with ZipFile(config.input_dir / "20260620_対象本.rtfd.zip", "w") as archive:
        archive.writestr("TXT.rtf", "対象本の読書メモです。")
    (config.input_dir / "20260620_book_cover.webp").write_bytes(b"fake cover")
    (config.input_dir / "20260620_author.jpg").write_bytes(b"fake author")
    (config.input_dir / "20260616_book_cover.webp").write_bytes(b"fake related cover")

    out_dir = run(config)[0]

    assert (out_dir / "script.md").exists()
    assert (out_dir / "05_image_prompts.json").exists()
    assert (out_dir / "assets" / "current_book_cover.webp").exists()
    assert (out_dir / "assets" / "author_reference.jpg").exists()
    assert (out_dir / "assets" / "related_book_cover.webp").exists()
    assert not list((out_dir / "images").glob("scene_*.png"))


def test_generate_images_only_uses_existing_prompts_without_ai_assets(tmp_path: Path, monkeypatch):
    import json

    def fail_ai(*args, **kwargs):
        raise AssertionError("generate_ai_assets should not be called")

    calls = []

    def fake_generate_images(targets, **kwargs):
        calls.extend(targets)
        return []

    monkeypatch.setattr("bookbase_automation.processor.generate_ai_assets", fail_ai)
    monkeypatch.setattr("bookbase_automation.processor.generate_images", fake_generate_images)
    out_dir = tmp_path / "output" / "2026-06-20_book"
    out_dir.mkdir(parents=True)
    (out_dir / "05_image_prompts.json").write_text(json.dumps([{"scene": 10, "prompt": "scene ten"}]), encoding="utf-8")
    config = AppConfig.from_root(tmp_path, generate_images_only=True, images_output_dir=out_dir, image_scenes="10", resume_images=True)

    assert run(config) == [out_dir]
    assert [target.key for target in calls] == ["scene_10"]
    assert calls[0].prompt.endswith("scene ten")
