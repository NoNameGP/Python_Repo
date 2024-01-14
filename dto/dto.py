from dataclasses import dataclass
from typing import List


@dataclass
class Point:
    X: float
    Y: float


@dataclass
class RouteDTO:
    email: str
    start_point: Point
    end_point: Point
    pass_points: List[Point]
    objects: List[Point]


@dataclass
class MarkDTO:
    email: str
    mark_name: str
    end_point: Point
