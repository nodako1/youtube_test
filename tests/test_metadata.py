from bookbase_automation.generator import generate_fallback_assets
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
