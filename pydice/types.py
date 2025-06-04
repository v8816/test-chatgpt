from __future__ import annotations

from typing import List, TypedDict


class RollResult(TypedDict):
    total: int
    rolls: List[int]
    modifier: int
