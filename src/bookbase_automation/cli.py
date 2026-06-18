from __future__ import annotations

import argparse
from pathlib import Path

from .config import AppConfig
from .processor import run


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Book Base YouTube production helper automation")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Project root directory")
    parser.add_argument("--max-files", type=int, default=1, help="Maximum .txt files to process per run")
    parser.add_argument("--use-ai", action="store_true", help="Use OpenAI API for production generation")
    parser.add_argument("--allow-fallback", action="store_true", help="Allow deterministic fallback generation for local smoke tests only")
    parser.add_argument("--model", default="gpt-4.1-mini", help="OpenAI model for --use-ai")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    config = AppConfig.from_root(
        args.root,
        max_files_per_run=args.max_files,
        use_ai=args.use_ai,
        allow_fallback=args.allow_fallback,
        model=args.model,
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
