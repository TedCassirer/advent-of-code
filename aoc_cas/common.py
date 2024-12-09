import dataclasses
from functools import cache
import typing as t

T = t.TypeVar("T")


@dataclasses.dataclass(frozen=True)
class Direction:
    __slots__ = "dy", "dx"
    dy: int
    dx: int

    @cache
    @staticmethod
    def create(dy: int, dx: int) -> "Direction":
        return Direction(dy, dx)

    def turn_right(self) -> t.Self:
        return Direction.create(dx=-self.dy, dy=self.dx)

    def turn_left(self) -> t.Self:
        return Direction.create(dx=self.dy, dy=-self.dx)

    def __lt__(self, other: t.Self) -> bool:
        if self.dy == other.dy:
            return self.dx < other.dx
        return self.dy < other.dy


DIR_DOWN = Direction.create(1, 0)
DIR_UP = Direction.create(-1, 0)
DIR_LEFT = Direction.create(0, -1)
DIR_RIGHT = Direction.create(0, 1)


@dataclasses.dataclass(frozen=True)
class Vector:
    __slots__ = "y", "x"
    y: int
    x: int

    def __abs__(self) -> int:
        return abs((self.y**2 + self.x**2) ** 0.5)

    def __mul__(self, k: int) -> t.Self:
        return Vector(self.y * k, self.x * k)


@dataclasses.dataclass(frozen=True)
class Coordinate:
    __slots__ = "y", "x"
    y: int
    x: int

    @cache
    @staticmethod
    def create(y: int, x: int) -> "Coordinate":
        return Coordinate(y, x)

    def move(self, dir: Direction, k: int = 1) -> t.Self:
        return Coordinate.create(self.y + dir.dy * k, self.x + dir.dx * k)

    def md(self, other: t.Self) -> int:
        return abs(other.x - self.x) + abs(other.y - self.y)

    def __add__(self, v: Vector) -> t.Self:
        return Coordinate.create(self.y + v.y, self.x + v.x)

    def __sub__(self, other: t.Self) -> Vector:
        return Vector(self.y - other.y, self.x - other.x)

    def __lt__(self, other: t.Self) -> bool:
        if self.y == other.y:
            return self.x < other.x
        return self.y < other.y


class Grid(t.Generic[T]):
    def __init__(self, rows: t.MutableSequence[t.MutableSequence[T]]):
        self._grid = rows
        self.M = len(rows)
        self.N = len(rows[0])

    @property
    def dimensions(self) -> tuple[int, int]:
        return self.M, self.N

    def in_bounds(self, coord: Coordinate) -> bool:
        return 0 <= coord.y < self.M and 0 <= coord.x < self.N

    def get(self, i: Coordinate, default: T | None = None) -> T | None:
        if self.in_bounds(i):
            return self._grid[i.y][i.x]
        return default

    def rows(self) -> t.Sequence[t.Sequence[T]]:
        return list(self._grid)

    def find(self, val: T) -> Coordinate | None:
        for y, row in enumerate(self._grid):
            for x, v in enumerate(row):
                if v == val:
                    return Coordinate.create(y, x)
        return None

    def items(self) -> t.Iterable[t.Tuple[Coordinate, T]]:
        for y, row in enumerate(self._grid):
            for x, val in enumerate(row):
                yield Coordinate.create(y, x), val

    def __getitem__(self, c: Coordinate) -> T:
        return self._grid[c.y][c.x]

    def __setitem__(self, c: Coordinate, value: T) -> None:
        self._grid[c.y][c.x] = value

    def __len__(self) -> int:
        return self.M * self.N
