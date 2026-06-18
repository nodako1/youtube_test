from __future__ import annotations

import traceback
from pathlib import Path

from .config import AppConfig
from .fs_utils import move_file, output_folder_name, slugify
from .generator import generate_ai_assets, generate_fallback_assets
from .quality import build_quality_report
from .rules import load_rules


def discover_inputs(input_dir: Path) -> list[Path]:
    return sorted(path for path in input_dir.glob("*.txt") if path.is_file())


def process_one(input_path: Path, config: AppConfig) -> Path:
    processing_path = move_file(input_path, config.processing_dir)
    book_name = slugify(processing_path.stem)
    out_dir = config.output_dir / output_folder_name(processing_path)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "images").mkdir(exist_ok=True)
    (out_dir / "thumbnails").mkdir(exist_ok=True)

    try:
        source_text = processing_path.read_text(encoding="utf-8")
        rules_text = load_rules(config.rules_dir)
        if config.use_ai:
            assets = generate_ai_assets(source_text, book_name, rules_text, model=config.model)
        elif config.allow_fallback:
            assets = generate_fallback_assets(source_text, book_name)
        else:
            raise RuntimeError("AI生成が無効です。本番実行では--use-aiを指定してください。動作確認のみ--allow-fallbackを使用できます。")

        (out_dir / "00_input.txt").write_text(source_text, encoding="utf-8")
        (out_dir / "01_script.md").write_text(assets.script, encoding="utf-8")
        (out_dir / "02_titles.md").write_text(assets.titles, encoding="utf-8")
        (out_dir / "03_description.md").write_text(assets.description, encoding="utf-8")
        (out_dir / "04_thumbnail_ideas.md").write_text(assets.thumbnail_ideas, encoding="utf-8")
        (out_dir / "05_image_prompts.json").write_text(assets.image_prompts, encoding="utf-8")
        report = build_quality_report(assets.script, assets.titles, assets.image_prompts, assets.description)
        (out_dir / "quality_report.md").write_text(report, encoding="utf-8")
        move_file(processing_path, config.archive_dir)
        return out_dir
    except Exception as exc:
        err_dir = config.error_dir / output_folder_name(processing_path)
        err_dir.mkdir(parents=True, exist_ok=True)
        (err_dir / "error_report.md").write_text(
            "# エラーレポート\n\n"
            f"対象ファイル: {processing_path.name}\n\n"
            f"エラー内容: {exc}\n\n"
            "## 詳細\n\n"
            f"```\n{traceback.format_exc()}\n```\n",
            encoding="utf-8",
        )
        move_file(processing_path, err_dir)
        raise


def run(config: AppConfig) -> list[Path]:
    config.ensure_directories()
    outputs: list[Path] = []
    for input_path in discover_inputs(config.input_dir)[: config.max_files_per_run]:
        outputs.append(process_one(input_path, config))
    return outputs
