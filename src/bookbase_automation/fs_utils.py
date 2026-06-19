from __future__ import annotations

import re
import shutil
from datetime import date
from pathlib import Path


_SAFE_CHARS = re.compile(r"[^0-9A-Za-zぁ-んァ-ン一-龥ー々〆〤\-_]+")
_DATE_PREFIX = re.compile(r"^(?P<date>\d{8})[_\-](?P<title>.+)$")


def slugify(value: str, *, fallback: str = "untitled") -> str:
    value = value.strip().replace(" ", "_").replace("　", "_")
    value = _SAFE_CHARS.sub("_", value)
    value = re.sub(r"_+", "_", value).strip("_")
    return value or fallback


def output_folder_name(input_path: Path, *, today: date | None = None) -> str:
    today = today or date.today()
    stem = input_path.stem
    match = _DATE_PREFIX.match(stem)
    if match:
        raw_date = match.group("date")
        title = slugify(match.group("title"))
        yyyy_mm_dd = f"{raw_date[:4]}-{raw_date[4:6]}-{raw_date[6:8]}"
        return f"{yyyy_mm_dd}_{title}"
    return f"{today.isoformat()}_{slugify(stem)}"


def unique_path(path: Path) -> Path:
    if not path.exists():
        return path
    counter = 2
    while True:
        candidate = path.with_name(f"{path.stem}_{counter}{path.suffix}")
        if not candidate.exists():
            return candidate
        counter += 1


def move_file(src: Path, dest_dir: Path) -> Path:
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = unique_path(dest_dir / src.name)
    shutil.move(str(src), str(dest))
    return dest


def move_path(src: Path, dest_dir: Path) -> Path:
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = unique_path(dest_dir / src.name)
    shutil.move(str(src), str(dest))
    return dest
