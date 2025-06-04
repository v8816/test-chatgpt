from __future__ import annotations

"""Utilities for parsing dice notation."""

import re

NOTATION_RE = re.compile(r"(\d+)d(\d+)([+-]\d+)?")


def parse_notation(notation: str) -> tuple[int, int, int]:
    """Parse dice notation ``XdY(+|-)Z``.

    Returns a tuple ``(count, sides, modifier)``.
    """

    match = NOTATION_RE.fullmatch(notation.strip())
    if not match:
        raise ValueError(f"Invalid notation: {notation}")
    count = int(match.group(1))
    sides = int(match.group(2))
    mod = int(match.group(3)) if match.group(3) else 0
    if count <= 0 or sides <= 0:
        raise ValueError("Count and sides must be positive")
    return count, sides, mod
