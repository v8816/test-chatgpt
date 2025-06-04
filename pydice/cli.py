from __future__ import annotations

"""Command line interface for PyDice.

See the project documentation for usage examples.
"""

import argparse
import json
import random
from typing import Sequence

from .hist import create_histogram
from .parser import parse_notation
from .types import RollResult


def roll_once(count: int, sides: int, mod: int) -> RollResult:
    """Roll ``count`` dice with ``sides`` sides and apply ``mod``."""

    rolls = [random.randint(1, sides) for _ in range(count)]
    total = sum(rolls) + mod
    return {"total": total, "rolls": rolls, "modifier": mod}


def build_parser() -> argparse.ArgumentParser:
    """Return an argument parser for the CLI."""

    parser = argparse.ArgumentParser(prog="pydice", description="Roll dice")
    parser.add_argument("notation", help="Dice notation XdY(+|-)Z")
    parser.add_argument("--hist", type=int, metavar="N", help="generate histogram of N rolls")
    parser.add_argument("--json", action="store_true", help="output result as JSON")
    return parser


def main(argv: Sequence[str] | None = None) -> None:
    """Entry point for the CLI."""

    parser = build_parser()
    args = parser.parse_args(argv)
    count, sides, mod = parse_notation(args.notation)
    if args.hist:
        results = [sum(random.randint(1, sides) for _ in range(count)) + mod for _ in range(args.hist)]
        create_histogram(results, "hist.png")
    result = roll_once(count, sides, mod)
    if args.json:
        print(json.dumps(result))
    else:
        print(result["total"])


if __name__ == "__main__":  # pragma: no cover
    main()
