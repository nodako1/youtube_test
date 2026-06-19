from __future__ import annotations

import json
import shutil
import traceback
from pathlib import Path

from .assets import AssetCheck, build_asset_report, check_input_assets
from .config import AppConfig
from .fs_utils import move_file, move_path, output_folder_name, slugify
from .generator import AIResponseJSONParseError, AIResponseValidationError, generate_ai_assets, generate_fallback_assets
from .image_generation import build_image_quality_report, build_image_targets, generate_images, parse_image_scenes, render_failed_images, render_prompts_markdown
from .input_assets import FlatInputSelection, build_flat_input_report, derive_book_slug, find_rtfd_zip_files, format_rtfd_zip_search_error, read_rtfd_zip_text, select_flat_inputs, status_for
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
        (out_dir / "image_context.json").write_text(assets.image_context, encoding="utf-8")
        research_dir = out_dir / "research"
        research_dir.mkdir(exist_ok=True)
        (research_dir / "scene_11_story_person.md").write_text(assets.research_scene_11, encoding="utf-8")
        (research_dir / "scene_15_quote_person.md").write_text(assets.research_scene_15, encoding="utf-8")
        report = build_quality_report(assets.script, assets.titles, assets.image_prompts, assets.description, source_text)
        report += build_metadata_quality_report(assets.metadata)
        report += build_asset_report(asset_checks)
        report += _build_research_quality_report(assets.research_scene_11, assets.research_scene_15)
        report += assets.api_communication_report
        (out_dir / "quality_report.md").write_text(report, encoding="utf-8")
        if processing_path.name == "source.txt" and processing_path.parent.parent == config.processing_dir:
            move_path(processing_path.parent, config.archive_dir)
        else:
            move_file(processing_path, config.archive_dir)
        return out_dir
    except Exception as exc:
        err_dir = config.error_dir / output_folder_name(processing_path)
        err_dir.mkdir(parents=True, exist_ok=True)
        if not isinstance(exc, (AIResponseJSONParseError, AIResponseValidationError)):
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




def _copy_flat_reference_assets(selection: FlatInputSelection, out_dir: Path) -> FlatInputSelection:
    assets_dir = out_dir / "assets"
    assets_dir.mkdir(exist_ok=True)

    def copy_one(path: Path | None, name: str) -> list[Path]:
        if path is None:
            return []
        dest = assets_dir / f"{name}{path.suffix.lower()}"
        shutil.copy2(path, dest)
        return [dest]

    return FlatInputSelection(
        selection.run_date,
        selection.date_key,
        selection.current_sources,
        copy_one(selection.current_book_cover, "current_book_cover"),
        copy_one(selection.current_author, "author_reference"),
        selection.related_sources,
        copy_one(selection.related_book_cover, "related_book_cover"),
    )


def _selection_from_output_assets(out_dir: Path) -> FlatInputSelection:
    assets_dir = out_dir / "assets"
    def first(pattern: str) -> list[Path]:
        return sorted(assets_dir.glob(pattern))[:1]
    return FlatInputSelection(
        run_date=__import__("datetime").date.today(),
        date_key="",
        current_sources=[],
        current_book_covers=first("current_book_cover.*"),
        current_authors=first("author_reference.*"),
        related_sources=[],
        related_book_covers=first("related_book_cover.*"),
    )


def generate_images_for_output(out_dir: Path, config: AppConfig) -> Path:
    prompts_path = out_dir / "05_image_prompts.json"
    if not prompts_path.exists():
        raise RuntimeError(f"05_image_prompts.json が見つかりません: {out_dir}")
    selected_scenes = parse_image_scenes(config.image_scenes)
    selection = _selection_from_output_assets(out_dir)
    targets = build_image_targets(out_dir, prompts_path.read_text(encoding="utf-8"), selection, scene03_only=config.image_scene03_only, scenes=selected_scenes, include_thumbnails=False)
    if config.dry_run_images:
        print(render_prompts_markdown(targets))
        results = []
    else:
        results = generate_images(targets, model=config.image_model, force=config.force_images, resume=config.resume_images, progress_dir=out_dir)
    (out_dir / "image_prompts.md").write_text(render_prompts_markdown(targets), encoding="utf-8")
    (out_dir / "failed_images.md").write_text(render_failed_images(results) if results else "# failed_images.md\n\n画像生成はdry-runのため未実行です。\n", encoding="utf-8")
    image_report = build_image_quality_report(results, scene03_only=config.image_scene03_only, scenes=selected_scenes, model=config.image_model)
    report_path = out_dir / "quality_report.md"
    existing = report_path.read_text(encoding="utf-8") if report_path.exists() else "# quality_report.md\n"
    report_path.write_text(existing.rstrip() + "\n" + image_report, encoding="utf-8")
    return out_dir

def _has_flat_today_input(config: AppConfig) -> bool:
    selection = select_flat_inputs(config.input_dir, run_date=config.target_date)
    return bool(selection.used_files)


def _write_flat_outputs(out_dir: Path, source_text: str, assets) -> None:
    (out_dir / "script.md").write_text(assets.script, encoding="utf-8")
    (out_dir / "metadata.md").write_text(assets.metadata, encoding="utf-8")
    (out_dir / "legacy_titles.md").write_text(assets.titles, encoding="utf-8")
    (out_dir / "legacy_description.md").write_text(assets.description, encoding="utf-8")
    (out_dir / "legacy_thumbnail_ideas.md").write_text(assets.thumbnail_ideas, encoding="utf-8")
    (out_dir / "00_input.txt").write_text(source_text, encoding="utf-8")
    (out_dir / "image_context.json").write_text(assets.image_context, encoding="utf-8")
    (out_dir / "05_image_prompts.json").write_text(assets.image_prompts, encoding="utf-8")
    research_dir = out_dir / "research"
    research_dir.mkdir(exist_ok=True)
    (research_dir / "scene_11_story_person.md").write_text(assets.research_scene_11, encoding="utf-8")
    (research_dir / "scene_15_quote_person.md").write_text(assets.research_scene_15, encoding="utf-8")



def _flat_asset_checks(selection) -> list[AssetCheck]:
    return [
        AssetCheck(3, "scene_03_current_book_cover", "今回紹介する本のブックカバー", status_for(selection.current_book_covers), str(selection.current_book_cover) if selection.current_book_cover else None, "input/YYYYMMDD_book_cover.* から動的に取得"),
        AssetCheck(4, "scene_04_author_reference", "著者イラスト作成用の参考画像", status_for(selection.current_authors, required=False), str(selection.current_author) if selection.current_author else None, "input/YYYYMMDD_author.* から動的に取得。なければ顔を想像しない", required=False),
        AssetCheck(19, "scene_19_related_book_cover", "関連動画側の本のブックカバー", status_for(selection.related_book_covers), str(selection.related_book_cover) if selection.related_book_cover else None, "過去日付のbook_coverから動的に取得"),
    ]

def process_flat_inputs(config: AppConfig) -> Path:
    selection = select_flat_inputs(config.input_dir, run_date=config.target_date)
    source_path = selection.current_source
    book_slug = derive_book_slug(source_path) if source_path else "input_error"
    out_dir = config.output_dir / f"{selection.run_date.isoformat()}_{book_slug}"
    try:
        if status_for(selection.current_sources) != "OK":
            found_rtfd_zip_files = []
            for path in find_rtfd_zip_files(config.input_dir):
                try:
                    found_rtfd_zip_files.append(path.relative_to(config.root))
                except ValueError:
                    found_rtfd_zip_files.append(path)
            raise RuntimeError(format_rtfd_zip_search_error(selection, found_rtfd_zip_files))
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
                asset_checks=_flat_asset_checks(selection),
                raw_response_path=out_dir / "debug" / "raw_ai_response.txt",
                error_dir=config.error_dir / f"{selection.run_date.isoformat()}_{book_slug}",
            )
        elif config.allow_fallback:
            assets = generate_fallback_assets(source_text, book_slug, _flat_asset_checks(selection))
        else:
            raise RuntimeError("AI生成が無効です。本番実行では--use-aiを指定してください。動作確認のみ--allow-fallbackを使用できます。")
        stable_selection = _copy_flat_reference_assets(selection, out_dir)
        selected_scenes = parse_image_scenes(config.image_scenes)
        targets = build_image_targets(out_dir, assets.image_prompts, stable_selection, scene03_only=config.image_scene03_only, scenes=selected_scenes, include_thumbnails=False)
        (out_dir / "image_prompts.md").write_text(render_prompts_markdown(targets), encoding="utf-8")
        image_report = build_image_quality_report([], scene03_only=config.image_scene03_only, scenes=selected_scenes, model=config.image_model)
        failed = "# failed_images.md\n\n画像生成は未実行です。--generate-images を指定するとOpenAI APIで生成します。\n"
        if config.dry_run_images:
            print(render_prompts_markdown(targets))
            failed = "# failed_images.md\n\n画像生成はdry-runのため未実行です。\n"
        elif config.generate_images and not config.generate_assets_only:
            results = generate_images(targets, model=config.image_model, force=config.force_images, resume=config.resume_images, progress_dir=out_dir)
            failed = render_failed_images(results)
            image_report = build_image_quality_report(results, scene03_only=config.image_scene03_only, scenes=selected_scenes, model=config.image_model)
            failed_scenes = [result.key for result in results if result.status not in {"OK", "SKIPPED"}]
            if failed_scenes:
                print(f"画像生成に失敗または要確認のsceneがあります: {', '.join(failed_scenes)}")
        (out_dir / "failed_images.md").write_text(failed, encoding="utf-8")
        _write_flat_outputs(out_dir, source_text, assets)
        report = build_quality_report(assets.script, assets.titles, assets.image_prompts, assets.description, source_text)
        report += build_metadata_quality_report(assets.metadata)
        report += build_flat_input_report(selection)
        report += image_report
        report += _build_research_quality_report(assets.research_scene_11, assets.research_scene_15)
        report += assets.api_communication_report
        (out_dir / "quality_report.md").write_text(report, encoding="utf-8")
        for used_file in selection.used_files:
            if used_file.exists():
                move_file(used_file, config.archive_dir)
        return out_dir
    except Exception as exc:
        err_dir = config.error_dir / f"{selection.run_date.isoformat()}_{book_slug}"
        err_dir.mkdir(parents=True, exist_ok=True)
        if not isinstance(exc, (AIResponseJSONParseError, AIResponseValidationError)):
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
    if config.generate_images_only:
        if config.images_output_dir is None:
            raise RuntimeError("--generate-images-only には --output-dir が必要です。")
        return [generate_images_for_output(config.images_output_dir, config)]
    if _has_flat_today_input(config):
        return [process_flat_inputs(config)]
    outputs: list[Path] = []
    for input_path in discover_inputs(config.input_dir)[: config.max_files_per_run]:
        outputs.append(process_one(input_path, config))
    return outputs
