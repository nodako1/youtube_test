from __future__ import annotations

import re
import zipfile
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ALLOWED_ASSET_EXTENSIONS = [".webp", ".png", ".jpg", ".jpeg"]
_DATE_PREFIX = re.compile(r"^(?P<date>\d{8})_(?P<rest>.+)$")


@dataclass(frozen=True)
class AssetCheck:
    scene: int | None
    key: str
    purpose: str
    status: str
    path: str | None
    note: str
    required: bool = True


@dataclass(frozen=True)
class InputBundle:
    today_key: str
    output_slug: str
    current_manuscripts: tuple[Path, ...]
    current_covers: tuple[Path, ...]
    current_authors: tuple[Path, ...]
    related_manuscripts: tuple[Path, ...]
    related_covers: tuple[Path, ...]
    unknown_files: tuple[Path, ...] = ()

    @property
    def all_candidate_files(self) -> tuple[Path, ...]:
        return (
            self.current_manuscripts
            + self.current_covers
            + self.current_authors
            + self.related_manuscripts
            + self.related_covers
        )

    @property
    def has_candidates(self) -> bool:
        return bool(self.all_candidate_files)


def today_key_jst() -> str:
    return datetime.now(ZoneInfo("Asia/Tokyo")).strftime("%Y%m%d")


def _date_prefix(path: Path) -> str | None:
    match = _DATE_PREFIX.match(path.name)
    if not match:
        return None
    return match.group("date")


def _without_rtfd_zip(name: str) -> str:
    return name[: -len(".rtfd.zip")] if name.endswith(".rtfd.zip") else Path(name).stem


def _title_from_manuscript(path: Path) -> str:
    base = _without_rtfd_zip(path.name)
    match = _DATE_PREFIX.match(base)
    if not match:
        return base
    return match.group("rest")


def _is_image(path: Path) -> bool:
    return path.suffix.lower() in ALLOWED_ASSET_EXTENSIONS


def _is_rtfd_zip(path: Path) -> bool:
    return path.name.endswith(".rtfd.zip")


def _is_book_cover(path: Path) -> bool:
    prefix = _date_prefix(path)
    return bool(prefix and _is_image(path) and path.stem == f"{prefix}_book_cover")


def _is_author(path: Path) -> bool:
    prefix = _date_prefix(path)
    return bool(prefix and _is_image(path) and path.stem == f"{prefix}_author")


def _is_manuscript(path: Path) -> bool:
    if not _is_rtfd_zip(path):
        return False
    lowered = path.name.lower()
    return "book_cover" not in lowered and "author" not in lowered and _date_prefix(path) is not None


def find_asset(assets_dir: Path, key: str) -> Path | None:
    for extension in ALLOWED_ASSET_EXTENSIONS:
        candidate = assets_dir / f"{key}{extension}"
        if candidate.exists() and candidate.is_file():
            return candidate
    return None


def discover_input_bundle(input_dir: Path, *, today_key: str | None = None) -> InputBundle:
    today_key = today_key or today_key_jst()
    files = sorted(path for path in input_dir.iterdir() if path.is_file()) if input_dir.exists() else []
    current_manuscripts: list[Path] = []
    current_covers: list[Path] = []
    current_authors: list[Path] = []
    related_manuscripts: list[Path] = []
    related_covers: list[Path] = []
    unknown_files: list[Path] = []

    for path in files:
        date_key = _date_prefix(path)
        if date_key is None:
            unknown_files.append(path)
            continue
        if date_key == today_key:
            if _is_manuscript(path):
                current_manuscripts.append(path)
            elif _is_book_cover(path):
                current_covers.append(path)
            elif _is_author(path):
                current_authors.append(path)
            else:
                unknown_files.append(path)
        elif date_key < today_key:
            if _is_manuscript(path):
                related_manuscripts.append(path)
            elif _is_book_cover(path):
                related_covers.append(path)
            else:
                unknown_files.append(path)
        else:
            unknown_files.append(path)

    output_slug = _title_from_manuscript(current_manuscripts[0]) if current_manuscripts else f"{today_key}_needs_review"
    return InputBundle(
        today_key=today_key,
        output_slug=output_slug,
        current_manuscripts=tuple(current_manuscripts),
        current_covers=tuple(current_covers),
        current_authors=tuple(current_authors),
        related_manuscripts=tuple(related_manuscripts),
        related_covers=tuple(related_covers),
        unknown_files=tuple(unknown_files),
    )


def _status_for(paths: tuple[Path, ...], *, required: bool) -> str:
    if len(paths) == 1:
        return "OK"
    if len(paths) > 1:
        return "DUPLICATED"
    return "MISSING" if required else "OPTIONAL"


def _path_text(paths: tuple[Path, ...]) -> str | None:
    if not paths:
        return None
    return ", ".join(path.name for path in paths)


def checks_for_bundle(bundle: InputBundle) -> list[AssetCheck]:
    return [
        AssetCheck(
            scene=None,
            key="current_manuscript",
            purpose="今回の動画の原稿材料",
            status=_status_for(bundle.current_manuscripts, required=True),
            path=_path_text(bundle.current_manuscripts),
            note="今日の日付の .rtfd.zip を1つだけ配置してください。",
            required=True,
        ),
        AssetCheck(
            scene=3,
            key="scene_03_current_book_cover",
            purpose="今回紹介する本のブックカバー。scene_03とサムネイルで使用",
            status=_status_for(bundle.current_covers, required=True),
            path=_path_text(bundle.current_covers),
            note="今日の日付の book_cover 画像を1つだけ配置してください。架空の表紙は作りません。",
            required=True,
        ),
        AssetCheck(
            scene=4,
            key="scene_04_author_reference",
            purpose="著者イラスト作成用の参考画像。任意だが推奨",
            status=_status_for(bundle.current_authors, required=False),
            path=_path_text(bundle.current_authors),
            note="著者画像がない場合は、著者の顔を想像で描かず人物シルエット、本、3ポイント中心の構図にします。",
            required=False,
        ),
        AssetCheck(
            scene=None,
            key="scene_19_related_manuscript",
            purpose="scene_19で紹介する過去動画・関連動画の内容",
            status=_status_for(bundle.related_manuscripts, required=True),
            path=_path_text(bundle.related_manuscripts),
            note="今日より前の日付の .rtfd.zip を1つだけ配置してください。",
            required=True,
        ),
        AssetCheck(
            scene=19,
            key="scene_19_related_book_cover",
            purpose="scene_19で紹介する過去動画・関連動画側の本のブックカバー",
            status=_status_for(bundle.related_covers, required=True),
            path=_path_text(bundle.related_covers),
            note="今日より前の日付の book_cover 画像を1つだけ配置してください。架空の過去本カバーは作りません。",
            required=True,
        ),
    ]


def _strip_rtf_markup(text: str) -> str:
    text = re.sub(r"\\'[0-9a-fA-F]{2}", "", text)
    text = re.sub(r"\\[a-zA-Z]+-?\d* ?", "", text)
    text = text.replace("{", " ").replace("}", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def read_rtfd_zip_text(path: Path) -> str:
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        text_names = [name for name in names if name.lower().endswith((".txt", ".rtf"))]
        if not text_names:
            raise RuntimeError(f"{path.name} に .rtf または .txt が含まれていません。")
        parts: list[str] = []
        for name in sorted(text_names):
            raw = archive.read(name)
            decoded = raw.decode("utf-8", errors="ignore")
            parts.append(_strip_rtf_markup(decoded) if name.lower().endswith(".rtf") else decoded.strip())
    return "\n\n".join(part for part in parts if part).strip()


def asset_checks_by_scene(checks: list[AssetCheck]) -> dict[int, AssetCheck]:
    return {check.scene: check for check in checks if check.scene is not None}


def _line_for(check: AssetCheck) -> str:
    suffix = f"（{check.path}）" if check.path else ""
    return f"- {check.key}：{check.status}{suffix}"


def build_asset_report(checks: list[AssetCheck], *, today_key: str | None = None) -> str:
    lines = ["", "## 【inputファイル判定】", ""]
    if today_key:
        lines.extend([f"- 実行日：{today_key}", f"- 今日の日付キー：{today_key}", ""])
    for check in checks:
        lines.append(_line_for(check))
    cover = next((check for check in checks if check.key == "scene_03_current_book_cover"), None)
    if cover:
        lines.extend(["", "## 【サムネイル入力画像チェック】", "", _line_for(cover)])
    problems = [check for check in checks if check.status in {"MISSING", "DUPLICATED", "OPTIONAL"}]
    if problems:
        lines.extend(["", "## 不足・重複・任意ファイル", ""])
        for check in problems:
            lines.append(f"- {check.key}：{check.status}。{check.note}")
    return "\n".join(lines) + "\n"


def validate_bundle(bundle: InputBundle) -> list[str]:
    errors: list[str] = []
    for check in checks_for_bundle(bundle):
        if check.required and check.status != "OK":
            errors.append(f"{check.key}: {check.status}（{check.note}）")
        if check.status == "DUPLICATED":
            errors.append(f"{check.key}: DUPLICATED（候補: {check.path}）")
    return errors
