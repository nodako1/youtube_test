import base64
import os
import sys
import types
from pathlib import Path

import pytest
from PIL import Image

from bookbase_automation.image_generation import (
    ImageTarget,
    build_image_targets,
    generate_images,
    parse_image_scenes,
    validate_png_16_9,
)
from bookbase_automation.input_assets import FlatInputSelection
from datetime import date


def _png_b64(size=(1536, 864)):
    path = Path(os.environ.get("PYTEST_TMPDIR", "/tmp")) / "mock_image.png"
    Image.new("RGB", size, (240, 235, 225)).save(path)
    return base64.b64encode(path.read_bytes()).decode("ascii")


class MockImages:
    def __init__(self):
        self.calls = []

    def generate(self, **kwargs):
        self.calls.append(kwargs)
        item = types.SimpleNamespace(b64_json=_png_b64())
        return types.SimpleNamespace(data=[item])

    def edit(self, **kwargs):
        return self.generate(**kwargs)


class MockOpenAI:
    images = MockImages()

    def __init__(self, api_key, timeout=None, max_retries=None):
        self.api_key = api_key
        self.timeout = timeout
        self.max_retries = max_retries


class MockAPIConnectionError(Exception):
    pass


class MockAPITimeoutError(Exception):
    pass


class MockRateLimitError(Exception):
    pass


class MockAPIStatusError(Exception):
    def __init__(self, message, status_code=500):
        super().__init__(message)
        self.status_code = status_code


def install_mock_openai(monkeypatch):
    MockOpenAI.images = MockImages()
    module = types.SimpleNamespace(
        OpenAI=MockOpenAI,
        APIConnectionError=MockAPIConnectionError,
        APITimeoutError=MockAPITimeoutError,
        RateLimitError=MockRateLimitError,
        APIStatusError=MockAPIStatusError,
    )
    monkeypatch.setitem(sys.modules, "openai", module)
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    return MockOpenAI.images


def target(tmp_path, scene=1):
    return ImageTarget(f"scene_{scene:02d}", f"scene_{scene:02d}.png", tmp_path, "minimal concise Japanese text only", (), scene)


def test_parse_image_scenes_selects_only_requested_scenes():
    assert parse_image_scenes("17,18,19,20") == [17, 18, 19, 20]
    assert parse_image_scenes("1-3,5") == [1, 2, 3, 5]


def test_build_image_targets_limits_to_image_scenes(tmp_path):
    selection = FlatInputSelection(date(2026, 6, 19), "20260619", [], [], [], [], [])
    targets = build_image_targets(tmp_path, "[]", selection, scenes=[19], include_thumbnails=False)
    assert [t.key for t in targets] == ["scene_19"]


def test_generate_images_calls_api_and_saves_png(monkeypatch, tmp_path):
    images = install_mock_openai(monkeypatch)
    results = generate_images([target(tmp_path)], force=False)
    output = tmp_path / "scene_01.png"
    assert output.exists()
    assert results[0].status == "OK"
    assert images.calls[0]["model"] == "gpt-image-2"
    assert images.calls[0]["size"] == "1536x864"
    assert images.calls[0]["quality"] == "high"
    assert images.calls[0]["output_format"] == "png"


def test_generate_images_skips_existing_without_force(monkeypatch, tmp_path):
    images = install_mock_openai(monkeypatch)
    output = tmp_path / "scene_01.png"
    Image.new("RGB", (1536, 864)).save(output)
    before = output.read_bytes()
    results = generate_images([target(tmp_path)], force=False)
    assert results[0].status == "SKIPPED"
    assert output.read_bytes() == before
    assert images.calls == []


def test_generate_images_regenerates_existing_with_force(monkeypatch, tmp_path):
    images = install_mock_openai(monkeypatch)
    output = tmp_path / "scene_01.png"
    output.write_bytes(b"old")
    results = generate_images([target(tmp_path)], force=True)
    assert results[0].status == "OK"
    assert images.calls
    assert output.read_bytes() != b"old"


def test_generate_images_requires_openai_api_key(monkeypatch, tmp_path):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    with pytest.raises(RuntimeError, match="OPENAI_API_KEY"):
        generate_images([target(tmp_path)])


def test_validate_png_16_9_accepts_exact_ratio(tmp_path):
    ok = tmp_path / "ok.png"
    ng = tmp_path / "ng.png"
    Image.new("RGB", (1920, 1080)).save(ok)
    Image.new("RGB", (1000, 1000)).save(ng)
    assert validate_png_16_9(ok)[2] is True
    assert validate_png_16_9(ng)[2] is False


def test_cli_options_keep_image_generation_and_dry_run_explicit():
    from bookbase_automation.cli import build_parser

    parser = build_parser()
    no_images = parser.parse_args(["--root", ".", "--use-ai"])
    dry_run = parser.parse_args(["--root", ".", "--use-ai", "--dry-run-images", "--image-scenes", "17,18"])
    generate = parser.parse_args(["--root", ".", "--use-ai", "--generate-images", "--image-scenes", "1-20"])

    assert no_images.generate_images is False
    assert dry_run.dry_run_images is True
    assert dry_run.generate_images is False
    assert dry_run.image_scenes == "17,18"
    assert generate.generate_images is True
