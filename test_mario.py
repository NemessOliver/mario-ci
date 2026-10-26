# Tests for mario.py. Run them with:  python -m pytest -q
# pytest finds every function that starts with test_ and runs it.

from mario import build_pyramid, get_height


def test_height_1_is_one_hash():
    assert build_pyramid(1) == "#"


def test_height_3_matches_by_hand():
    # >> expected value written out BY HAND, not copied from the function's own output
    expected = "  #\n" \
               " ##\n" \
               "###"
    assert build_pyramid(3) == expected


def test_number_of_rows_equals_height():
    for height in range(1, 9):
        rows = build_pyramid(height).split("\n")
        assert len(rows) == height


def test_every_row_is_right_aligned():
    # >> right-aligned = every row is exactly `height` characters long
    # >> and ends with a hash
    height = 8
    for row in build_pyramid(height).split("\n"):
        assert len(row) == height
        assert row.endswith("#")


def test_bottom_row_is_all_hashes():
    rows = build_pyramid(5).split("\n")
    assert rows[-1] == "#####"


def test_height_0_gives_empty_pyramid():
    # >> edge case: no rows at all
    assert build_pyramid(0) == ""


def test_get_height_asks_again_after_bad_input(monkeypatch):
    # >> monkeypatch swaps the real input() for a fake one that "types" these answers in order
    answers = iter(["abc", "0", "9", "4"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(answers))
    # >> "abc" (not a number), 0 and 9 (outside 1-8) must be rejected, so we end up at 4
    assert get_height() == 4
