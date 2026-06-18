from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


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
    model: str = "gpt-4.1-mini"

    @classmethod
    def from_root(cls, root: Path, *, max_files_per_run: int = 1, use_ai: bool = False, model: str = "gpt-4.1-mini") -> "AppConfig":
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
            model=model,
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
