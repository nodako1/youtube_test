from __future__ import annotations

import traceback
from pathlib import Path

from .assets import build_asset_report, check_input_assets
from .config import AppConfig
from .fs_utils import move_file, move_path, output_folder_name, slugify
from .generator import AIResponseJSONParseError, generate_ai_assets, generate_fallback_assets
from .image_generation import build_image_quality_report, build_image_targets, generate_images, render_failed_images, render_prompts_markdown
from .input_assets import build_flat_input_report, derive_book_slug, read_rtfd_zip_text, select_flat_inputs, status_for
from .metadata import build_metadata_quality_report
from .quality import build_quality_report
from .rules import load_rules


def discover_inputs(input_dir: Path) -> list[Path]:
    txt_inputs = [path for path in input_dir.glob("*.txt") if path.is_file()]
    folder_inputs = [path / "source.txt" for path in input_dir.iterdir() if path.is_dir() and (path / "source.txt").is_file()]
    return sorted(txt_inputs + folder_inputs)


def _append_related_video_context(source_text: str, input_root: Path) -> str:
    related_video = input_root / "scene_19_related_video.txt"
    if not related_video.exists():
        return source_text
    return (
        source_text.rstrip()
        + "\n\n# scene_19_related_video.txt\n"
        + related_video.read_text(encoding="utf-8").strip()
        + "\n"
    )


def _research_status(markdown: str) -> str:
    return "OK" if "自動取得ステータス：OK" in markdown or "ステータス：OK" in markdown else "NEEDS_REVIEW"


def _build_research_quality_report(research_scene_11: str, research_scene_15: str) -> str:
    status_11 = _research_status(research_scene_11)
    status_15 = _research_status(research_scene_15)
    return "\n".join(
        [
            "",
            "## 【自動取得情報チェック】",
            "",
            f"- scene_11_story_person：{status_11}",
            f"- scene_11_story_person_source：{status_11}",
            f"- scene_15_quote_person：{status_15}",
            f"- scene_15_quote_source：{status_15}",
            "- scene_11：人物画像未取得の場合は、シルエットまたは象徴表現で代替。",
            "- scene_15：名言人物画像未取得の場合は、名言カードまたは静物構図で代替。",
        ]
    ) + "\n"


def process_one(input_path: Path, config: AppConfig) -> Path:
    if input_path.name == "source.txt" and input_path.parent.parent == config.input_dir:
        processing_root = move_path(input_path.parent, config.processing_dir)
        processing_path = processing_root / "source.txt"
        input_root = processing_root
        output_name_source = processing_root
    else:
        processing_path = move_file(input_path, config.processing_dir)
        input_root = processing_path.parent
        output_name_source = processing_path
    book_name = slugify(output_name_source.stem)
    is_folder_input = processing_path.name == "source.txt" and processing_path.parent.parent == config.processing_dir
    asset_checks = check_input_assets(input_root, include_source_check=is_folder_input)
    out_dir = config.output_dir / output_folder_name(output_name_source)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "images").mkdir(exist_ok=True)
    (out_dir / "thumbnails").mkdir(exist_ok=True)

    try:
        source_text = processing_path.read_text(encoding="utf-8")
        generation_input = _append_related_video_context(source_text, input_root)
        rules_text = load_rules(config.rules_dir)
        if config.use_ai:
            assets = generate_ai_assets(
                generation_input,
                book_name,
                rules_text,
                model=config.model,
                asset_checks=asset_checks,
                raw_response_path=out_dir / "debug" / "raw_ai_response.txt",
                error_dir=config.error_dir / output_folder_name(processing_path),
            )
        elif config.allow_fallback:
            assets = generate_fallback_assets(generation_input, book_name, asset_checks)
        else:
            raise RuntimeError("AI生成が無効です。本番実行では--use-aiを指定してください。動作確認のみ--allow-fallbackを使用できます。")

        (out_dir / "00_input.txt").write_text(source_text, encoding="utf-8")
        (out_dir / "01_script.md").write_text(assets.script, encoding="utf-8")
        (out_dir / "02_titles.md").write_text(assets.titles, encoding="utf-8")
        (out_dir / "03_description.md").write_text(assets.description, encoding="utf-8")
        (out_dir / "metadata.md").write_text(assets.metadata, encoding="utf-8")
        (out_dir / "04_thumbnail_ideas.md").write_text(assets.thumbnail_ideas, encoding="utf-8")
        (out_dir / "06_thumbnail_comments.md").write_text(assets.thumbnail_comments, encoding="utf-8")
        (out_dir / "05_image_prompts.json").write_text(assets.image_prompts, encoding="utf-8")
        research_dir = out_dir / "research"
        research_dir.mkdir(exist_ok=True)
        (research_dir / "scene_11_story_person.md").write_text(assets.research_scene_11, encoding="utf-8")
        (research_dir / "scene_15_quote_person.md").write_text(assets.research_scene_15, encoding="utf-8")
        report = build_quality_report(assets.script, assets.titles, assets.image_prompts, assets.description)
        report += build_metadata_quality_report(assets.metadata)
        report += build_asset_report(asset_checks)
        report += _build_research_quality_report(assets.research_scene_11, assets.research_scene_15)
        (out_dir / "quality_report.md").write_text(report, encoding="utf-8")
        if processing_path.name == "source.txt" and processing_path.parent.parent == config.processing_dir:
            move_path(processing_path.parent, config.archive_dir)
        else:
            move_file(processing_path, config.archive_dir)
        return out_dir
    except Exception as exc:
        err_dir = config.error_dir / output_folder_name(processing_path)
        err_dir.mkdir(parents=True, exist_ok=True)
        if not isinstance(exc, AIResponseJSONParseError):
            (err_dir / "error_report.md").write_text(
                "# エラーレポート\n\n"
                f"対象ファイル: {processing_path.name}\n\n"
                f"エラー内容: {exc}\n\n"
                "## 詳細\n\n"
                f"```\n{traceback.format_exc()}\n```\n",
                encoding="utf-8",
            )
        if processing_path.name == "source.txt" and processing_path.parent.parent == config.processing_dir:
            move_path(processing_path.parent, err_dir)
        else:
            move_file(processing_path, err_dir)
        raise



def _has_flat_today_input(config: AppConfig) -> bool:
    selection = select_flat_inputs(config.input_dir)
    return bool(selection.used_files)


def _write_flat_outputs(out_dir: Path, source_text: str, assets) -> None:
    (out_dir / "script.md").write_text(assets.script, encoding="utf-8")
    (out_dir / "metadata.md").write_text(assets.metadata, encoding="utf-8")
    (out_dir / "legacy_titles.md").write_text(assets.titles, encoding="utf-8")
    (out_dir / "legacy_description.md").write_text(assets.description, encoding="utf-8")
    (out_dir / "legacy_thumbnail_ideas.md").write_text(assets.thumbnail_ideas, encoding="utf-8")
    (out_dir / "00_input.txt").write_text(source_text, encoding="utf-8")
    research_dir = out_dir / "research"
    research_dir.mkdir(exist_ok=True)
    (research_dir / "scene_11_story_person.md").write_text(assets.research_scene_11, encoding="utf-8")
    (research_dir / "scene_15_quote_person.md").write_text(assets.research_scene_15, encoding="utf-8")


def process_flat_inputs(config: AppConfig) -> Path:
    selection = select_flat_inputs(config.input_dir)
    source_path = selection.current_source
    book_slug = derive_book_slug(source_path) if source_path else "input_error"
    out_dir = config.output_dir / f"{selection.run_date.isoformat()}_{book_slug}"
    try:
        if status_for(selection.current_sources) != "OK":
            raise RuntimeError("今日の日付の .rtfd.zip が1件必要です。")
        assert source_path is not None
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "images").mkdir(exist_ok=True)
        (out_dir / "thumbnails").mkdir(exist_ok=True)
        source_text = read_rtfd_zip_text(source_path)
        if selection.related_source:
            source_text += "\n\n# scene_19_related_source\n" + read_rtfd_zip_text(selection.related_source)
        rules_text = load_rules(config.rules_dir)
        if config.use_ai:
            assets = generate_ai_assets(
                source_text,
                book_slug,
                rules_text,
                model=config.model,
                asset_checks=[],
                raw_response_path=out_dir / "debug" / "raw_ai_response.txt",
                error_dir=config.error_dir / f"{selection.run_date.isoformat()}_{book_slug}",
            )
        elif config.allow_fallback:
            assets = generate_fallback_assets(source_text, book_slug, [])
        else:
            raise RuntimeError("AI生成が無効です。本番実行では--use-aiを指定してください。動作確認のみ--allow-fallbackを使用できます。")
        targets = build_image_targets(out_dir, assets.image_prompts, selection, scene03_only=config.image_scene03_only)
        (out_dir / "image_prompts.md").write_text(render_prompts_markdown(targets), encoding="utf-8")
        image_report = build_image_quality_report([], scene03_only=config.image_scene03_only)
        failed = "# failed_images.md\n\n画像生成は未実行です。--generate-images を指定するとOpenAI APIで生成します。\n"
        if config.generate_images:
            results = generate_images(targets, model=config.image_model)
            failed = render_failed_images(results)
            image_report = build_image_quality_report(results, scene03_only=config.image_scene03_only)
        (out_dir / "failed_images.md").write_text(failed, encoding="utf-8")
        _write_flat_outputs(out_dir, source_text, assets)
        report = build_quality_report(assets.script, assets.titles, assets.image_prompts, assets.description)
        report += build_metadata_quality_report(assets.metadata)
        report += build_flat_input_report(selection)
        report += image_report
        report += _build_research_quality_report(assets.research_scene_11, assets.research_scene_15)
        (out_dir / "quality_report.md").write_text(report, encoding="utf-8")
        for used_file in selection.used_files:
            if used_file.exists():
                move_file(used_file, config.archive_dir)
        return out_dir
    except Exception as exc:
        err_dir = config.error_dir / f"{selection.run_date.isoformat()}_{book_slug}"
        err_dir.mkdir(parents=True, exist_ok=True)
        if not isinstance(exc, AIResponseJSONParseError):
            (err_dir / "error_report.md").write_text(
                "# エラーレポート\n\n"
                f"対象ファイル: {source_path.name if source_path else '未確定'}\n\n"
                f"エラー内容: {exc}\n\n"
                "## 詳細\n\n"
                f"```\n{traceback.format_exc()}\n```\n",
                encoding="utf-8",
            )
        for used_file in selection.used_files:
            if used_file.exists():
                move_file(used_file, err_dir)
        raise


def run(config: AppConfig) -> list[Path]:
    config.ensure_directories()
    if _has_flat_today_input(config):
        return [process_flat_inputs(config)]
    outputs: list[Path] = []
    for input_path in discover_inputs(config.input_dir)[: config.max_files_per_run]:
        outputs.append(process_one(input_path, config))
    return outputs
