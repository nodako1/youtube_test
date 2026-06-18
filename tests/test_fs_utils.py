from datetime import date
from pathlib import Path

from bookbase_automation.fs_utils import output_folder_name, slugify


def test_slugify_keeps_japanese_title():
    assert slugify("新版 思考の整理学!!") == "新版_思考の整理学"


def test_output_folder_name_uses_date_prefix():
    assert output_folder_name(Path("20260618_新版思考の整理学.txt")) == "2026-06-18_新版思考の整理学"


def test_output_folder_name_uses_today_without_prefix():
    assert output_folder_name(Path("book.txt"), today=date(2026, 6, 18)) == "2026-06-18_book"
