from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

ALLOWED_ASSET_EXTENSIONS = [".png", ".jpg", ".jpeg", ".webp"]

INPUT_FILE_SPECS = {
    "source": {
        "purpose": "本の内容・読書メモ・原稿作成の材料",
        "path": "source.txt",
        "required": True,
        "missing_note": "source.txt が見つかりません。動画ごとの入力フォルダに原稿作成用メモを置いてください。",
    },
    "scene_19_related_video": {
        "purpose": "scene_19で接続する過去動画・関連動画の情報",
        "path": "scene_19_related_video.txt",
        "required": True,
        "missing_note": "scene_19_related_video.txt が見つかりません。関連動画タイトル、関連本、今回の動画とのつながりを記入してください。",
    },
}

IMAGE_ASSET_SPECS = {
    3: {
        "key": "scene_03_current_book_cover",
        "purpose": "今回紹介する本のブックカバー。scene_03とサムネイルで使用",
        "required": True,
        "missing_note": "scene_03ではブックカバーなしで架空の表紙を作らず、needs_reviewにしてください。サムネイル生成もneeds_reviewです。",
    },
    4: {
        "key": "scene_04_author_reference",
        "purpose": "著者イラスト作成用の参考画像。任意だが推奨",
        "required": False,
        "missing_note": "scene_04では著者の顔を想像で描かず、人物シルエットまたは本と3ポイント中心の構図に変更してください。",
    },
    19: {
        "key": "scene_19_related_book_cover",
        "purpose": "scene_19で紹介する過去動画・関連動画側の本のブックカバー",
        "required": True,
        "missing_note": "scene_19では関連本のブックカバーを勝手に作らず、needs_reviewにしてください。",
    },
}

# Backward-compatible alias for older imports/tests.
REQUIRED_IMAGE_ASSETS = IMAGE_ASSET_SPECS


@dataclass(frozen=True)
class AssetCheck:
    scene: int | None
    key: str
    purpose: str
    status: str
    path: str | None
    note: str
    required: bool = True


def find_asset(assets_dir: Path, key: str) -> Path | None:
    for extension in ALLOWED_ASSET_EXTENSIONS:
        candidate = assets_dir / f"{key}{extension}"
        if candidate.exists() and candidate.is_file():
            return candidate
    return None


def _relative(path: Path, root: Path) -> str:
    return str(path.relative_to(root))


def _file_check(input_root: Path, key: str, spec: dict[str, object]) -> AssetCheck:
    relative = str(spec["path"])
    candidate = input_root / relative
    found = candidate if candidate.exists() and candidate.is_file() else None
    required = bool(spec["required"])
    status = "OK" if found else "MISSING"
    return AssetCheck(
        scene=None,
        key=key,
        purpose=str(spec["purpose"]),
        status=status,
        path=_relative(found, input_root) if found else None,
        note=f"使用ファイル：{_relative(found, input_root)}" if found else str(spec["missing_note"]),
        required=required,
    )


def check_input_assets(input_root: Path, *, include_source_check: bool = True) -> list[AssetCheck]:
    assets_dir = input_root / "assets"
    checks: list[AssetCheck] = []
    for key, spec in INPUT_FILE_SPECS.items():
        if key == "source" and not include_source_check:
            continue
        checks.append(_file_check(input_root, key, spec))
    for scene, spec in IMAGE_ASSET_SPECS.items():
        found = find_asset(assets_dir, str(spec["key"]))
        required = bool(spec["required"])
        status = "OK" if found else ("MISSING" if required else "OPTIONAL")
        checks.append(
            AssetCheck(
                scene=scene,
                key=str(spec["key"]),
                purpose=str(spec["purpose"]),
                status=status,
                path=_relative(found, input_root) if found else None,
                note=f"使用画像：{_relative(found, input_root)}" if found else str(spec["missing_note"]),
                required=required,
            )
        )
    return checks


def asset_checks_by_scene(checks: list[AssetCheck]) -> dict[int, AssetCheck]:
    return {check.scene: check for check in checks if check.scene is not None}


def _line_for(check: AssetCheck) -> str:
    suffix = f"（{check.path}）" if check.path else ""
    return f"- {check.key}：{check.status}{suffix}"


def build_asset_report(checks: list[AssetCheck]) -> str:
    lines = ["", "## 【入力ファイルチェック】", ""]
    for key in ["source", "scene_19_related_video", "scene_03_current_book_cover", "scene_04_author_reference", "scene_19_related_book_cover"]:
        check = next((item for item in checks if item.key == key), None)
        if check:
            lines.append(_line_for(check))
    cover = next((check for check in checks if check.key == "scene_03_current_book_cover"), None)
    if cover:
        lines.extend(["", "## 【サムネイル入力画像チェック】", "", _line_for(cover)])
    missing = [check for check in checks if check.status == "MISSING"]
    optional = [check for check in checks if check.status == "OPTIONAL"]
    if missing or optional:
        lines.extend(["", "## 不足・任意ファイル", ""])
        for check in missing + optional:
            lines.append(f"- {check.key} が見つかりません。{check.note}")
    return "\n".join(lines) + "\n"
