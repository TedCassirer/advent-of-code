import dataclasses
from functools import cache
from typing import Self


@dataclasses.dataclass(frozen=True)
class Direction:
    __slots__ = "dy", "dx"
    dy: int
    dx: int

    @cache
    @staticmethod
    def create(dy: int, dx: int) -> "Direction":
        return Direction(dy, dx)

    def rotate(self, left: bool = True) -> Self:
        if left:
            return Direction.create(dx=self.dy, dy=-self.dx)
        else:
            return Direction.create(dx=-self.dy, dy=self.dx)

    def __lt__(self, other: Self) -> bool:
        if self.dy == other.dy:
            return self.dx < other.dx
        return self.dy < other.dy


DIR_DOWN = Direction.create(1, 0)
DIR_UP = Direction.create(-1, 0)
DIR_LEFT = Direction.create(0, -1)
DIR_RIGHT = Direction.create(0, 1)


@dataclasses.dataclass(frozen=True)
class Coordinate:
    __slots__ = "y", "x"
    y: int
    x: int

    @cache
    @staticmethod
    def create(y: int, x: int) -> "Coordinate":
        return Coordinate(y, x)

    def move(self, dir: Direction, k: int = 1) -> Self:
        return Coordinate.create(self.y + dir.dy * k, self.x + dir.dx * k)

    def md(self, other: Self) -> int:
        return abs(other.x - self.x) + abs(other.y - self.y)

    def __lt__(self, other: Self) -> bool:
        if self.y == other.y:
            return self.x < other.x
        return self.y < other.y
