from __future__ import annotations

import shutil
import traceback
from pathlib import Path

from .assets import (
    InputBundle,
    build_asset_report,
    checks_for_bundle,
    discover_input_bundle,
    read_rtfd_zip_text,
    validate_bundle,
)
from .config import AppConfig
from .fs_utils import output_folder_name, slugify, unique_path
from .generator import generate_ai_assets, generate_fallback_assets
from .metadata import build_metadata_quality_report
from .quality import build_quality_report
from .rules import load_rules


def discover_inputs(input_dir: Path) -> list[InputBundle]:
    bundle = discover_input_bundle(input_dir)
    return [bundle] if bundle.has_candidates else []


def _move_files(files: tuple[Path, ...], dest_dir: Path) -> tuple[Path, ...]:
    dest_dir.mkdir(parents=True, exist_ok=True)
    moved: list[Path] = []
    for src in files:
        dest = unique_path(dest_dir / src.name)
        shutil.move(str(src), str(dest))
        moved.append(dest)
    return tuple(moved)


def _bundle_with_moved_files(bundle: InputBundle, moved_root: Path, moved_files: tuple[Path, ...]) -> InputBundle:
    by_name = {path.name: path for path in moved_files}

    def moved(paths: tuple[Path, ...]) -> tuple[Path, ...]:
        return tuple(by_name[path.name] for path in paths if path.name in by_name)

    return InputBundle(
        today_key=bundle.today_key,
        output_slug=bundle.output_slug,
        current_manuscripts=moved(bundle.current_manuscripts),
        current_covers=moved(bundle.current_covers),
        current_authors=moved(bundle.current_authors),
        related_manuscripts=moved(bundle.related_manuscripts),
        related_covers=moved(bundle.related_covers),
        unknown_files=(),
    )


def _read_generation_input(bundle: InputBundle) -> tuple[str, str]:
    current = bundle.current_manuscripts[0]
    related = bundle.related_manuscripts[0]
    current_text = read_rtfd_zip_text(current)
    related_text = read_rtfd_zip_text(related)
    generation_input = (
        current_text.rstrip()
        + "\n\n# scene_19_related_material\n"
        + related_text.strip()
        + "\n"
    )
    return current_text, generation_input


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


def _archive_or_error_dir(base: Path, bundle: InputBundle) -> Path:
    return base / output_folder_name(Path(f"{bundle.today_key}_{slugify(bundle.output_slug)}.txt"))


def process_one(bundle: InputBundle, config: AppConfig) -> Path:
    processing_root = unique_path(config.processing_dir / slugify(bundle.output_slug))
    moved_files = _move_files(bundle.all_candidate_files, processing_root)
    processing_bundle = _bundle_with_moved_files(bundle, processing_root, moved_files)
    asset_checks = checks_for_bundle(processing_bundle)
    out_dir = config.output_dir / output_folder_name(Path(f"{processing_bundle.today_key}_{slugify(processing_bundle.output_slug)}.txt"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "images").mkdir(exist_ok=True)
    (out_dir / "thumbnails").mkdir(exist_ok=True)

    try:
        validation_errors = validate_bundle(processing_bundle)
        if validation_errors:
            raise RuntimeError("inputファイル判定でneeds_reviewです: " + "; ".join(validation_errors))

        source_text, generation_input = _read_generation_input(processing_bundle)
        rules_text = load_rules(config.rules_dir)
        if config.use_ai:
            assets = generate_ai_assets(generation_input, slugify(processing_bundle.output_slug), rules_text, model=config.model, asset_checks=asset_checks)
        elif config.allow_fallback:
            assets = generate_fallback_assets(generation_input, slugify(processing_bundle.output_slug), asset_checks)
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
        report += build_asset_report(asset_checks, today_key=processing_bundle.today_key)
        report += _build_research_quality_report(assets.research_scene_11, assets.research_scene_15)
        (out_dir / "quality_report.md").write_text(report, encoding="utf-8")
        archive_dir = _archive_or_error_dir(config.archive_dir, processing_bundle)
        _move_files(tuple(processing_root.iterdir()), archive_dir)
        processing_root.rmdir()
        return out_dir
    except Exception as exc:
        err_dir = _archive_or_error_dir(config.error_dir, processing_bundle)
        err_dir.mkdir(parents=True, exist_ok=True)
        (err_dir / "error_report.md").write_text(
            "# エラーレポート\n\n"
            f"対象入力: {processing_bundle.output_slug}\n\n"
            f"エラー内容: {exc}\n\n"
            "## 詳細\n\n"
            f"```\n{traceback.format_exc()}\n```\n",
            encoding="utf-8",
        )
        (err_dir / "quality_report.md").write_text(build_asset_report(asset_checks, today_key=processing_bundle.today_key), encoding="utf-8")
        _move_files(tuple(processing_root.iterdir()), err_dir)
        processing_root.rmdir()
        raise


def run(config: AppConfig) -> list[Path]:
    config.ensure_directories()
    outputs: list[Path] = []
    for bundle in discover_inputs(config.input_dir)[: config.max_files_per_run]:
        outputs.append(process_one(bundle, config))
    return outputs
