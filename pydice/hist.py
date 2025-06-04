from __future__ import annotations

"""Histogram utilities."""

from typing import Iterable

import matplotlib.pyplot as plt


def create_histogram(results: Iterable[int], path: str) -> None:
    """Save a histogram of *results* to *path*."""

    plt.figure()
    plt.hist(list(results), bins="auto")
    plt.xlabel("Result")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
