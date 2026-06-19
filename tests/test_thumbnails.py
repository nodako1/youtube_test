from bookbase_automation.generator import generate_fallback_assets


def test_thumbnail_outputs_include_three_patterns_and_current_cover_reference():
    assets = generate_fallback_assets("本のメモ", "テスト本")

    assert "thumbnail_A_loss_aversion.png" in assets.thumbnail_ideas
    assert "thumbnail_B_benefit.png" in assets.thumbnail_ideas
    assert "thumbnail_C_curiosity.png" in assets.thumbnail_ideas
    assert "Pattern A：" in assets.thumbnail_comments
    assert "脅し・損失回避型" in assets.thumbnail_comments
    assert "誘惑・ベネフィット型" in assets.thumbnail_comments
    assert "逆張り・好奇心型" in assets.thumbnail_comments
    assert "今日の日付_book_cover画像" in assets.thumbnail_comments
