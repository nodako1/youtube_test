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
    assert "scenes" in schema["required"]
    assert "script" not in schema["required"]
    assert schema["properties"]["scenes"]["minItems"] == 20
    assert schema["properties"]["scenes"]["maxItems"] == 20
    assert schema["properties"]["scenes"]["items"]["properties"]["body"]["minLength"] == 180
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
            "schedule": [
                {"time": "0:00", "topic": "本日のテーマ：導入"},
                {"time": "2:00", "topic": "ポイント①：要点1"},
                {"time": "4:00", "topic": "ポイント②：要点2"},
                {"time": "6:00", "topic": "ポイント③：要点3"},
                {"time": "8:00", "topic": "まとめ：締め"},
            ],
            "description": {"text": "説明文", "count": 3},
            "comment": ["1行目", "2行目", "3行目"],
            "metadata": {},
        }
    )

    assert rendered.startswith("# 投稿補助情報")
    assert "## タイトル案" in rendered
    assert "## タイムスケジュール" in rendered
    assert "0:00 本日のテーマ：導入" in rendered
    assert "8:00 まとめ：締め" in rendered
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
                {"scene_number": index, "body": f"本文{index}です。"}
                for index in range(1, 21)
            ]
        },
        "script",
    )

    assert "【シーン1】" in rendered
    assert "本文1です。" in rendered
    assert "\n\n【シーン2】\n" in rendered
    assert rendered.endswith("\n")


def test_structured_optional_markdown_fields_are_rendered():
    from bookbase_automation.generator import _ensure_markdown_text, render_image_prompts

    assert "要点" in _ensure_markdown_text({"text": "要点"}, "thumbnail_ideas")
    assert "- 注意: 確認" in _ensure_markdown_text({"注意": "確認"}, "thumbnail_comments")
    assert render_image_prompts({"prompts": [{"scene": 1, "prompt": "desk"}]}).startswith("{")


def test_render_script_from_scenes_enforces_bookbase_format():
    from bookbase_automation.generator import render_script_from_scenes, validate_bookbase_script

    scene_1 = "こんにちは！人生の土台作りをサポートするブックベースです！いきなりですが、人材関連サービスを提供する株式会社R＆Gの2026年の調査で、能力開発や人材育成に問題があると答えた事業所は何％だったと思いますか。A、39.9％。B、59.9％。C、79.9％。管理職だけでなく、後輩指導やチーム作業にも直結する数字です。自分の仕事の土台にも関わります。それでは正解を発表します。"
    scene_3 = "今回紹介するのは、著者さんの『テスト本』こちらの本になります。結論から言うと、仕事の判断を整理できることです。本書が教えてくれるのは、根性で乗り切る方法ではなく、状況の見方を変える技術です。会議や相談の場面でも、考える順番が整うだけで言葉の選び方が変わります。迷った時の確認点が増えるので、明日の一歩も選びやすくなります。仕事に活かしたい人にとって、とても学びのある一冊になっています。"
    scene_4 = "著者の著者さんは、本書のテーマに関わる知見を読者が使いやすい形で伝えてきた人物です。本書の重要ポイントは、最初に本質的な課題を見える形にすること、次に背景や仕組みを理解して判断を整えること、最後に小さな行動へ落として実践を始めることです。この三つは横並びではなく、順番に深掘りすることで明日の行動に変わります。仕事で迷う方は、この三つをつなげると、実践に移しやすいです。"
    scenes = [{"scene_number": 1, "body": scene_1}] + [{"scene_number": index, "body": scene_3 if index == 3 else scene_4 if index == 4 else "あ" * 180} for index in range(2, 21)]
    rendered = render_script_from_scenes(scenes)

    assert rendered.startswith("【シーン1】\n")
    assert "\n\n【シーン2】\n" in rendered
    assert rendered.endswith("\n")
    assert validate_bookbase_script(rendered) == []


def test_validate_bookbase_script_reports_short_and_joined_scene():
    from bookbase_automation.generator import validate_bookbase_script

    errors = validate_bookbase_script("【シーン1】短い本文【シーン2】短い本文")

    assert "シーン数：0個。20個ではありません" in errors
    assert "見出しと本文が同じ行になっています" in errors
