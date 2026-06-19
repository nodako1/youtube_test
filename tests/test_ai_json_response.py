import json
from pathlib import Path

from bookbase_automation.generator import _bookbase_assets_json_schema, _write_ai_json_parse_error_report, _write_raw_ai_response


def test_bookbase_assets_json_schema_requires_single_strict_object():
    schema = _bookbase_assets_json_schema()

    assert schema["type"] == "object"
    assert schema["additionalProperties"] is False
    assert "image_prompts" in schema["required"]
    image_prompts = schema["properties"]["image_prompts"]
    assert image_prompts["minItems"] == 20
    assert image_prompts["maxItems"] == 20
    assert image_prompts["items"]["additionalProperties"] is False
    assert "最終プロンプト" in image_prompts["items"]["required"]


def test_ai_response_debug_and_parse_error_files_are_written(tmp_path: Path):
    raw_text = json.dumps({"script": "本文"}, ensure_ascii=False) + "\n余計な説明"

    _write_raw_ai_response(tmp_path / "output" / "debug" / "raw_ai_response.txt", raw_text)
    _write_ai_json_parse_error_report(tmp_path / "error" / "2026-06-19_book", raw_text)

    assert (tmp_path / "output" / "debug" / "raw_ai_response.txt").read_text(encoding="utf-8") == raw_text
    assert (tmp_path / "error" / "2026-06-19_book" / "raw_ai_response.txt").read_text(encoding="utf-8") == raw_text
    report = (tmp_path / "error" / "2026-06-19_book" / "error_report.md").read_text(encoding="utf-8")
    assert "エラー種別：AI応答JSONパース失敗" in report
    assert "発生箇所：generator.py / generate_ai_assets / json.loads(text)" in report
