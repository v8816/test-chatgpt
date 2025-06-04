import pytest

from pydice import parser
from pydice.parser import parse_notation
from hypothesis import given, strategies as st


@pytest.mark.parametrize(
    "notation,expected",
    [
        ("1d6", (1, 6, 0)),
        ("2d8+1", (2, 8, 1)),
        ("3d4-2", (3, 4, -2)),
        (" 10d20+5 ", (10, 20, 5)),
    ],
)
def test_parse_valid(notation, expected):
    assert parse_notation(notation) == expected


@pytest.mark.parametrize("notation", ["d6", "2d", "1d6+", "xd6", "1d-6", "1d6++1"])
def test_parse_invalid(notation):
    with pytest.raises(ValueError):
        parse_notation(notation)


def test_parse_zero_values():
    with pytest.raises(ValueError):
        parse_notation("0d6")
    with pytest.raises(ValueError):
        parse_notation("1d0")


@given(st.text(min_size=1, max_size=5).filter(lambda s: not parser.NOTATION_RE.fullmatch(s)))
def test_random_invalid(text):
    with pytest.raises(ValueError):
        parse_notation(text)


@given(
    st.integers(min_value=1, max_value=5),
    st.integers(min_value=1, max_value=20),
    st.integers(min_value=-5, max_value=5),
)
def test_roundtrip(count, sides, mod):
    notation = f"{count}d{sides}{mod:+d}" if mod else f"{count}d{sides}"
    assert parse_notation(notation) == (count, sides, mod)
