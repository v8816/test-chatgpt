from pathlib import Path
from contextlib import contextmanager
import os
import json
from hypothesis import given, strategies as st
import io
from contextlib import redirect_stdout

import pytest

from pydice import cli


@contextmanager
def inside_dir(path: Path):
    old = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(old)


def test_cli_plain(capsys):
    cli.main(["1d6"])
    out = capsys.readouterr().out.strip()
    assert out.isdigit()


def test_cli_json(tmp_path: Path, capsys):
    with inside_dir(tmp_path):
        cli.main(["2d4+1", "--json", "--hist", "5"])
        out = capsys.readouterr().out
        data = json.loads(out)
        assert "total" in data
        assert Path("hist.png").exists()


def test_cli_hist_only(tmp_path: Path):
    with inside_dir(tmp_path):
        cli.main(["1d6", "--hist", "3"])
        assert Path("hist.png").exists()


def test_cli_large_roll(capsys):
    cli.main(["10d1+0"])
    out = capsys.readouterr().out.strip()
    assert out == "10"


@given(
    st.integers(min_value=1, max_value=3),
    st.integers(min_value=1, max_value=6),
    st.integers(min_value=-2, max_value=2),
)
def test_cli_random(count, sides, mod):
    """Property-based test for various notations."""

    notation = f"{count}d{sides}{mod:+d}" if mod else f"{count}d{sides}"
    with io.StringIO() as buf, redirect_stdout(buf):
        cli.main([notation])
        out = buf.getvalue().strip()
    assert out.lstrip("-").isdigit()
