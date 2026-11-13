"""Shared chart primitives for Lumen Chart Kit."""

from dataclasses import dataclass
from typing import Sequence


@dataclass
class Point:
    x: float
    y: float


def scale(points: Sequence[Point], width: int, height: int) -> list[tuple[int, int]]:
    if not points:
        return []
    xs = [p.x for p in points]
    ys = [p.y for p in points]
    x_span = (max(xs) - min(xs)) or 1
    y_span = (max(ys) - min(ys)) or 1
    return [
        (int((p.x - min(xs)) / x_span * width), height - int((p.y - min(ys)) / y_span * height))
        for p in points
    ]
