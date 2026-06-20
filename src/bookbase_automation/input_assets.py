from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo
from zipfile import ZipFile, BadZipFile

from .fs_utils import slugify

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}
RTFD_ZIP_SUFFIX = ".rtfd.zip"
TOKYO_TIMEZONE = ZoneInfo("Asia/Tokyo")
BOOK_BASE_LOGO_FILENAME = "book_base_logo.png"


@dataclass(frozen=True)
class FlatInputSelection:
    run_date: date
    date_key: str
    current_sources: list[Path]
    current_book_covers: list[Path]
    current_authors: list[Path]
    related_sources: list[Path]
    related_book_covers: list[Path]

    @property
    def current_source(self) -> Path | None:
        return self.current_sources[0] if len(self.current_sources) == 1 else None

    @property
    def current_book_cover(self) -> Path | None:
        return self.current_book_covers[0] if len(self.current_book_covers) == 1 else None

    @property
    def current_author(self) -> Path | None:
        return self.current_authors[0] if len(self.current_authors) == 1 else None

    @property
    def related_source(self) -> Path | None:
        return self.related_sources[0] if len(self.related_sources) == 1 else None

    @property
    def related_book_cover(self) -> Path | None:
        return self.related_book_covers[0] if len(self.related_book_covers) == 1 else None

    @property
    def used_files(self) -> list[Path]:
        files: list[Path] = []
        for group in [
            self.current_sources,
            self.current_book_covers,
            self.current_authors,
            self.related_sources,
            self.related_book_covers,
        ]:
            files.extend(group)
        return sorted(set(files))


def _date_prefix(path: Path) -> str | None:
    name = path.name
    return name[:8] if len(name) >= 8 and name[:8].isdigit() else None


def _is_rtfd_zip(path: Path) -> bool:
    return path.name.lower().endswith(RTFD_ZIP_SUFFIX)


def _is_book_cover(path: Path) -> bool:
    return path.suffix.lower() in IMAGE_EXTENSIONS and "_book_cover" in path.stem.lower()


def _is_author(path: Path) -> bool:
    return path.suffix.lower() in IMAGE_EXTENSIONS and "_author" in path.stem.lower()


def is_book_base_logo_asset(path: Path) -> bool:
    return path.name.lower() == BOOK_BASE_LOGO_FILENAME


def today_in_tokyo() -> date:
    return datetime.now(TOKYO_TIMEZONE).date()


def select_flat_inputs(input_dir: Path, *, run_date: date | None = None) -> FlatInputSelection:
    run_date = run_date or today_in_tokyo()
    date_key = run_date.strftime("%Y%m%d")
    files = [path for path in input_dir.iterdir() if path.is_file() and not is_book_base_logo_asset(path)]
    current_sources: list[Path] = []
    current_book_covers: list[Path] = []
    current_authors: list[Path] = []
    related_sources: list[Path] = []
    related_book_covers: list[Path] = []
    for path in files:
        prefix = _date_prefix(path)
        if not prefix:
            continue
        is_today = prefix == date_key
        is_past = prefix < date_key
        if _is_rtfd_zip(path):
            if is_today:
                current_sources.append(path)
            elif is_past:
                related_sources.append(path)
        elif _is_book_cover(path):
            if is_today:
                current_book_covers.append(path)
            elif is_past:
                related_book_covers.append(path)
        elif is_today and _is_author(path):
            current_authors.append(path)
    return FlatInputSelection(
        run_date=run_date,
        date_key=date_key,
        current_sources=sorted(current_sources),
        current_book_covers=sorted(current_book_covers),
        current_authors=sorted(current_authors),
        related_sources=sorted(related_sources),
        related_book_covers=sorted(related_book_covers),
    )


def status_for(files: list[Path], *, required: bool = True) -> str:
    if len(files) == 1:
        return "OK"
    if len(files) > 1:
        return "DUPLICATED"
    return "MISSING" if required else "OPTIONAL"


def derive_book_slug(source: Path) -> str:
    name = source.name
    if name.lower().endswith(RTFD_ZIP_SUFFIX):
        stem = name[: -len(RTFD_ZIP_SUFFIX)]
    else:
        stem = source.stem
    if len(stem) >= 9 and stem[:8].isdigit() and stem[8] in {"_", "-"}:
        stem = stem[9:]
    return slugify(stem)


def read_rtfd_zip_text(path: Path) -> str:
    try:
        with ZipFile(path) as archive:
            text_parts: list[str] = []
            for member in sorted(archive.namelist()):
                lower = member.lower()
                if lower.endswith("/"):
                    continue
                if lower.endswith((".txt", ".rtf", ".md")) or "txt.rtf" in lower:
                    data = archive.read(member)
                    text_parts.append(data.decode("utf-8", errors="ignore"))
            if text_parts:
                return "\n\n".join(text_parts)
    except BadZipFile:
        return path.read_text(encoding="utf-8", errors="ignore")
    return f"{path.name} からテキストを抽出できませんでした。ファイル内容を確認してください。"


def format_rtfd_zip_search_error(selection: FlatInputSelection, found_files: list[Path]) -> str:
    lines = [
        "今日の日付の .rtfd.zip が1件必要です。",
        f"target_date: {selection.date_key}",
        "found_rtfd_zip_files:",
    ]
    if found_files:
        lines.extend(f"- {path.as_posix()}" for path in found_files)
    else:
        lines.append("- (none)")
    return "\n".join(lines)


def find_rtfd_zip_files(input_dir: Path) -> list[Path]:
    return sorted(path for path in input_dir.iterdir() if path.is_file() and not is_book_base_logo_asset(path) and _is_rtfd_zip(path))


def build_flat_input_report(selection: FlatInputSelection) -> str:
    lines = [
        "",
        "## 【入力ファイル判定】",
        "",
        f"- 実行日：{selection.run_date.isoformat()}",
        f"- 今日の日付キー：{selection.date_key}",
        f"- 今回の原稿材料：{status_for(selection.current_sources)}",
        f"- 今回のブックカバー：{status_for(selection.current_book_covers)}",
        f"- 今回の著者画像：{status_for(selection.current_authors, required=False)}",
        f"- scene_19用原稿材料：{status_for(selection.related_sources)}",
        f"- scene_19用ブックカバー：{status_for(selection.related_book_covers)}",
    ]
    return "\n".join(lines) + "\n"
