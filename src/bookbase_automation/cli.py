from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path

from .config import AppConfig
from .processor import run


def _parse_target_date(value: str):
    try:
        return datetime.strptime(value, "%Y%m%d").date()
    except ValueError as exc:
        raise argparse.ArgumentTypeError("--target-date must be in YYYYMMDD format") from exc


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Book Base YouTube production helper automation")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Project root directory")
    parser.add_argument("--max-files", type=int, default=1, help="Maximum .txt files to process per run")
    parser.add_argument("--use-ai", action="store_true", help="Use OpenAI API for production generation")
    parser.add_argument("--allow-fallback", action="store_true", help="Allow deterministic fallback generation for local smoke tests only")
    parser.add_argument("--model", default="gpt-4.1-mini", help="OpenAI model for --use-ai")
    parser.add_argument("--verify-images", action="store_true", help="Verify generated scene PNG existence and 16:9 aspect ratio")
    parser.add_argument("--generate-images", action="store_true", help="Generate PNG image files with the OpenAI Images API")
    parser.add_argument("--generate-assets-only", action="store_true", help="Generate and save script, metadata, and image prompts without calling the Images API")
    parser.add_argument("--generate-images-only", action="store_true", help="Generate images from an existing output directory without regenerating text assets")
    parser.add_argument("--output-dir", type=Path, help="Existing output/{date}_{book_slug} directory for --generate-images-only")
    parser.add_argument("--image-scenes", default="1-20", help="Scenes to generate or dry-run, e.g. 1-20, 17,18,19,20, or 19")
    parser.add_argument("--force-images", action="store_true", help="Regenerate and overwrite existing scene images")
    parser.add_argument("--resume-images", action="store_true", help="Skip existing valid images that are marked OK in image_progress.json")
    parser.add_argument("--dry-run-images", action="store_true", help="Print final image prompts without calling the OpenAI Images API")
    parser.add_argument("--image-scene03-only", action="store_true", help="Only generate output images/scene_03.png for API smoke testing")
    parser.add_argument("--image-model", default="gpt-image-2", help="OpenAI image model for image generation/editing")
    parser.add_argument("--target-date", type=_parse_target_date, help="Target input date in YYYYMMDD format (defaults to today in Asia/Tokyo)")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.verify_images:
        from .image_generation import validate_png_16_9
        failed = False
        for path in sorted((args.root / "output").glob("*/images/scene_*.png")):
            exists_ok, image_size, ratio_ok, error = validate_png_16_9(path)
            size_text = f"{image_size[0]}x{image_size[1]}" if image_size else "unknown"
            print(f"{path}: exists={exists_ok} size={size_text} 16:9={ratio_ok}{f' error={error}' if error else ''}")
            failed = failed or not exists_ok or not ratio_ok
        return 1 if failed else 0

    config = AppConfig.from_root(
        args.root,
        max_files_per_run=args.max_files,
        use_ai=args.use_ai,
        allow_fallback=args.allow_fallback,
        model=args.model,
        generate_images=args.generate_images,
        generate_assets_only=args.generate_assets_only,
        generate_images_only=args.generate_images_only,
        image_scene03_only=args.image_scene03_only,
        image_model=args.image_model,
        image_scenes=args.image_scenes,
        force_images=args.force_images,
        dry_run_images=args.dry_run_images,
        resume_images=args.resume_images,
        images_output_dir=args.output_dir,
        target_date=args.target_date,
    )
    outputs = run(config)
    if not outputs:
        print("inputに.txtファイルがないため、処理はありませんでした。")
        return 0
    for output in outputs:
        print(f"生成完了: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
