from dataclasses import dataclass
from typing import List


@dataclass
class Point:
    X: float
    Y: float


@dataclass
class RouteDTO:
    email: str
    departure: str
    arrival: str
    pass_points: List[Point]
    objects: List[Point]


@dataclass
class MarkDTO:
    email: str
    mark_name: str
    end_point: Point


@dataclass
class UserDTO:
    email: str
    password: str
