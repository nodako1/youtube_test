from bookbase_automation.assets import AssetCheck
from bookbase_automation.generator import generate_fallback_assets


def test_thumbnail_outputs_include_three_patterns_and_cover_reference():
    checks = [
        AssetCheck(
            scene=3,
            key="scene_03_current_book_cover",
            purpose="今回紹介する本のブックカバー",
            status="OK",
            path="assets/scene_03_current_book_cover.png",
            note="使用画像：assets/scene_03_current_book_cover.png",
        )
    ]

    assets = generate_fallback_assets("本のメモ", "テスト本", checks)

    assert "thumbnail_A_loss_aversion.png" in assets.thumbnail_ideas
    assert "thumbnail_B_benefit.png" in assets.thumbnail_ideas
    assert "thumbnail_C_curiosity.png" in assets.thumbnail_ideas
    assert "Pattern A：" in assets.thumbnail_comments
    assert "脅し・損失回避型" in assets.thumbnail_comments
    assert "誘惑・ベネフィット型" in assets.thumbnail_comments
    assert "逆張り・好奇心型" in assets.thumbnail_comments
    assert "assets/scene_03_current_book_cover.png" in assets.thumbnail_comments


def test_thumbnail_outputs_mark_needs_review_without_cover():
    checks = [
        AssetCheck(
            scene=3,
            key="scene_03_current_book_cover",
            purpose="今回紹介する本のブックカバー",
            status="MISSING",
            path=None,
            note="scene_03ではブックカバーなしで架空の表紙を作らず、needs_reviewにしてください。",
        )
    ]

    assets = generate_fallback_assets("本のメモ", "テスト本", checks)

    assert "needs_review：True" in assets.thumbnail_comments
    assert "架空のブックカバーは作らない" in assets.thumbnail_comments
