import json
from pathlib import Path

from bookbase_automation.generator import (
    _bookbase_assets_json_schema,
    _write_ai_json_parse_error_report,
    _write_ai_json_validation_error_report,
    _write_raw_ai_response,
    render_description,
    render_metadata,
    render_titles,
)


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


def test_render_titles_accepts_structured_patterns():
    rendered = render_titles(
        {
            "pattern_a": "【損する前に】テスト本【今すぐ確認】",
            "pattern_b": "【仕事が軽い】テスト本【明日変わる】",
            "pattern_c": "【努力しない】テスト本【逆転の発想】",
        }
    )

    assert rendered.startswith("## タイトル案")
    assert "Pattern A：脅し・損失回避型" in rendered
    assert "【損する前に】テスト本【今すぐ確認】" in rendered
    assert rendered.endswith("\n")


def test_render_description_accepts_structured_description():
    rendered = render_description({"text": "テスト本の要点を仕事に活かす説明です。", "count": 22})

    assert rendered.startswith("## 50文字説明")
    assert "文字数：22文字" in rendered


def test_render_metadata_combines_structured_json_sections():
    rendered = render_metadata(
        {
            "titles": {"pattern_a": "A案", "pattern_b": "B案", "pattern_c": "C案"},
            "schedule": [{"time": "0:00", "topic": "導入"}],
            "description": {"text": "説明文", "count": 3},
            "comment": ["1行目", "2行目", "3行目"],
            "metadata": {},
        }
    )

    assert rendered.startswith("# 投稿補助情報")
    assert "## タイトル案" in rendered
    assert "## タイムスケジュール" in rendered
    assert "0:00 導入" in rendered
    assert "## 50文字説明" in rendered
    assert "## コメント" in rendered


def test_ai_response_validation_error_report_is_written(tmp_path: Path):
    _write_ai_json_validation_error_report(tmp_path, "Unexpected titles type: list", {"titles": []})

    report = (tmp_path / "error_report.md").read_text(encoding="utf-8")
    assert "エラー種別：AI応答JSON型検証失敗" in report
    assert "Unexpected titles type: list" in report
    assert (tmp_path / "parsed_ai_response.json").exists()


def test_ensure_markdown_text_accepts_structured_script_dict():
    from bookbase_automation.generator import _ensure_markdown_text

    rendered = _ensure_markdown_text(
        {
            "scenes": [
                {"scene": 1, "text": "導入です。"},
                {"scene": 2, "text": "結論です。"},
            ]
        },
        "script",
    )

    assert "【シーン1】" in rendered
    assert "導入です。" in rendered
    assert rendered.endswith("\n")


def test_structured_optional_markdown_fields_are_rendered():
    from bookbase_automation.generator import _ensure_markdown_text, render_image_prompts

    assert "要点" in _ensure_markdown_text({"text": "要点"}, "thumbnail_ideas")
    assert "- 注意: 確認" in _ensure_markdown_text({"注意": "確認"}, "thumbnail_comments")
    assert render_image_prompts({"prompts": [{"scene": 1, "prompt": "desk"}]}).startswith("{")
