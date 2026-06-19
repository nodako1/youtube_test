from bookbase_automation.generator import (
    generate_fallback_assets,
    render_comment,
    render_metadata,
    render_schedule,
)
from bookbase_automation.metadata import build_metadata_quality_report


def test_metadata_output_contains_required_sections():
    assets = generate_fallback_assets("本のメモ", "テスト本")

    assert assets.metadata.startswith("# 投稿補助情報")
    assert "## タイトル案" in assets.metadata
    assert "Pattern A：脅し・損失回避型" in assets.metadata
    assert "Pattern B：誘惑・ベネフィット型" in assets.metadata
    assert "Pattern C：逆張り・好奇心型" in assets.metadata
    assert "0:00 本日のテーマ：" in assets.metadata
    assert "8:00 まとめ：" in assets.metadata
    assert "## 50文字説明" in assets.metadata
    assert "文字数：" in assets.metadata
    assert "## コメント" in assets.metadata


def test_metadata_quality_report_passes_generated_metadata():
    assets = generate_fallback_assets("本のメモ", "テスト本")

    report = build_metadata_quality_report(assets.metadata)

    assert "タイトル前後の【】：OK" in report
    assert "タイムスケジュール5項目：OK" in report
    assert "タイムスケジュール時間固定：OK" in report
    assert "50文字説明 50〜60文字：OK" in report
    assert "コメント3行構成：OK" in report
    assert "コメント3行目固定文：OK" in report


def _structured_schedule():
    return [
        {"time": "0:00", "topic": "本日のテーマ：否定しない言い換えの効果"},
        {"time": "2:00", "topic": "ポイント①：否定を避ける心理学的効果"},
        {"time": "4:00", "topic": "ポイント②：受け取り方を変える言い換え技法"},
        {"time": "6:00", "topic": "ポイント③：具体的フレーズの活用法"},
        {"time": "8:00", "topic": "まとめ：実践して良好なコミュニケーションへ"},
    ]


def _structured_comment():
    return [
        "今回は、否定しない言い換えについて紹介しました。",
        "あなたも日常や仕事で相手の意見を否定せず伝えようとした経験はありませんか？",
        "キーワードをコメントしてください。",
    ]


def test_render_schedule_outputs_exactly_five_newline_separated_lines():
    rendered = render_schedule(_structured_schedule())
    body_lines = rendered.split("\n\n", 1)[1].strip().splitlines()

    assert len(body_lines) == 5
    assert body_lines == [
        "0:00 本日のテーマ：否定しない言い換えの効果",
        "2:00 ポイント①：否定を避ける心理学的効果",
        "4:00 ポイント②：受け取り方を変える言い換え技法",
        "6:00 ポイント③：具体的フレーズの活用法",
        "8:00 まとめ：実践して良好なコミュニケーションへ",
    ]
    assert "効果 2:00" not in rendered


def test_render_comment_outputs_three_lines_and_fixed_third_line():
    rendered = render_comment(_structured_comment())
    body_lines = rendered.split("\n\n", 1)[1].strip().splitlines()

    assert len(body_lines) == 3
    assert body_lines[2] == "もし似たような経験があれば、ぜひコメント欄で教えてください。"
    assert "紹介しました。 あなたも" not in rendered


def test_render_metadata_has_blank_lines_between_sections():
    rendered = render_metadata(
        {
            "titles": {
                "pattern_a": "【A】タイトル【A】",
                "pattern_b": "【B】タイトル【B】",
                "pattern_c": "【C】タイトル【C】",
            },
            "schedule": _structured_schedule(),
            "description": {"text": "説明文", "count": 3},
            "comment": _structured_comment(),
            "metadata": {},
        }
    )

    assert "# 投稿補助情報\n\n## タイトル案" in rendered
    assert "## タイムスケジュール\n\n0:00" in rendered
    assert "8:00 まとめ：実践して良好なコミュニケーションへ\n\n## 50文字説明" in rendered
    assert "文字数：3文字\n\n## コメント\n\n今回は" in rendered
    assert "\n2:00 ポイント①" in rendered
    assert "紹介しました。\nあなたも" in rendered


def test_metadata_quality_report_includes_metadata_format_check():
    metadata = render_metadata(
        {
            "titles": {
                "pattern_a": "【A】タイトル【A】",
                "pattern_b": "【B】タイトル【B】",
                "pattern_c": "【C】タイトル【C】",
            },
            "schedule": _structured_schedule(),
            "description": {
                "text": "この本の要点を仕事と日常で使える視点に絞り、明日から実践できる行動まで解説します。",
                "count": 46,
            },
            "comment": _structured_comment(),
            "metadata": {},
        }
    )

    report = build_metadata_quality_report(metadata)

    assert "【metadata出力整形チェック】" in report
    assert "タイムスケジュール5行出力：OK" in report
    assert "タイムスケジュール1行連結なし：OK" in report
    assert "コメント3行出力：OK" in report
    assert "コメント1行連結なし：OK" in report
    assert "コメント3行目固定文：OK" in report
