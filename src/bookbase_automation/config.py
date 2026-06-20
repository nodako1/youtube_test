from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path


BOOK_BASE_LOGO_PATH = "input/book_base_logo.png"
BOOK_BASE_LOGO_WIDTH = 180
BOOK_BASE_LOGO_LEFT_MARGIN = 28
BOOK_BASE_LOGO_BOTTOM_MARGIN = 24


@dataclass(frozen=True)
class AppConfig:
    root: Path
    input_dir: Path
    processing_dir: Path
    output_dir: Path
    archive_dir: Path
    error_dir: Path
    rules_dir: Path
    max_files_per_run: int = 1
    use_ai: bool = False
    allow_fallback: bool = False
    model: str = "gpt-4.1-mini"
    generate_images: bool = False
    generate_assets_only: bool = False
    generate_images_only: bool = False
    image_scene03_only: bool = False
    image_model: str = "gpt-image-2"
    image_scenes: str = "1-20"
    force_images: bool = False
    dry_run_images: bool = False
    resume_images: bool = False
    images_output_dir: Path | None = None
    target_date: date | None = None

    @classmethod
    def from_root(
        cls,
        root: Path,
        *,
        max_files_per_run: int = 1,
        use_ai: bool = False,
        allow_fallback: bool = False,
        model: str = "gpt-4.1-mini",
        generate_images: bool = False,
        generate_assets_only: bool = False,
        generate_images_only: bool = False,
        image_scene03_only: bool = False,
        image_model: str = "gpt-image-2",
        image_scenes: str = "1-20",
        force_images: bool = False,
        dry_run_images: bool = False,
        resume_images: bool = False,
        images_output_dir: Path | None = None,
        target_date: date | None = None,
    ) -> "AppConfig":
        root = root.resolve()
        return cls(
            root=root,
            input_dir=root / "input",
            processing_dir=root / "processing",
            output_dir=root / "output",
            archive_dir=root / "archive",
            error_dir=root / "error",
            rules_dir=root / "rules",
            max_files_per_run=max_files_per_run,
            use_ai=use_ai,
            allow_fallback=allow_fallback,
            model=model,
            generate_images=generate_images,
            generate_assets_only=generate_assets_only,
            generate_images_only=generate_images_only,
            image_scene03_only=image_scene03_only,
            image_model=image_model,
            image_scenes=image_scenes,
            force_images=force_images,
            dry_run_images=dry_run_images,
            resume_images=resume_images,
            images_output_dir=images_output_dir.resolve() if images_output_dir else None,
            target_date=target_date,
        )

    def ensure_directories(self) -> None:
        for directory in [
            self.input_dir,
            self.processing_dir,
            self.output_dir,
            self.archive_dir,
            self.error_dir,
            self.rules_dir,
        ]:
            directory.mkdir(parents=True, exist_ok=True)
