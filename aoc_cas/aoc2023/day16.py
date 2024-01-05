import dataclasses
from enum import Enum
from functools import cache
from typing import Self, Sequence


class Direction(Enum):
    UP = (-1, 0)
    LEFT = (0, -1)
    DOWN = (1, 0)
    RIGHT = (0, 1)


@dataclasses.dataclass(frozen=True)
class Coordinate:
    y: int
    x: int

    @cache
    @staticmethod
    def create(y: int, x: int) -> "Coordinate":
        return Coordinate(y, x)

    def move(self, dir: Direction, k: int = 1) -> Self:
        return Coordinate.create(self.y + dir.value[0] * k, self.x + dir.value[1] * k)


reflections: dict[str, dict[Direction, tuple[Direction, ...]]] = {
    "/": {
        Direction.UP: (Direction.RIGHT,),
        Direction.LEFT: (Direction.DOWN,),
        Direction.DOWN: (Direction.LEFT,),
        Direction.RIGHT: (Direction.UP,),
    },
    "\\": {
        Direction.UP: (Direction.LEFT,),
        Direction.LEFT: (Direction.UP,),
        Direction.DOWN: (Direction.RIGHT,),
        Direction.RIGHT: (Direction.DOWN,),
    },
    "|": {
        Direction.UP: (Direction.UP,),
        Direction.LEFT: (Direction.UP, Direction.DOWN),
        Direction.DOWN: (Direction.DOWN,),
        Direction.RIGHT: (Direction.UP, Direction.DOWN),
    },
    "-": {
        Direction.UP: (Direction.LEFT, Direction.RIGHT),
        Direction.LEFT: (Direction.LEFT,),
        Direction.DOWN: (Direction.LEFT, Direction.RIGHT),
        Direction.RIGHT: (Direction.RIGHT,),
    },
    ".": {
        Direction.UP: (Direction.UP,),
        Direction.LEFT: (Direction.LEFT,),
        Direction.DOWN: (Direction.DOWN,),
        Direction.RIGHT: (Direction.RIGHT,),
    },
}


@dataclasses.dataclass(frozen=True)
class Light:
    pos: Coordinate
    dir: Direction


def calculate_energized_tiles(board: list[str], start_pos: Coordinate, start_dir: Direction) -> int:
    M, N = len(board), len(board[0])
    lights = {(start_pos, start_dir)}
    energized = {start_pos}
    seen = set()
    while lights:
        nxt = set()
        for coord, dir in lights:
            if coord.y < 0 or coord.y >= M or coord.x < 0 or coord.x >= N:
                continue
            energized.add(coord)
            tile = board[coord.y][coord.x]
            for reflection in reflections[tile][dir]:
                nxt.add((coord.move(reflection), reflection))
        lights = nxt - seen
        seen.update(nxt)
    return len(energized)


def part_a(data: str) -> int:
    board = data.splitlines()

    return calculate_energized_tiles(board, Coordinate.create(0, 0), Direction.RIGHT)


def part_b(data: str) -> int:
    board = data.splitlines()
    M, N = len(board), len(board[0])
    top = max(calculate_energized_tiles(board, Coordinate.create(0, x), Direction.DOWN) for x in range(N))
    bottom = max(calculate_energized_tiles(board, Coordinate.create(M - 1, x), Direction.UP) for x in range(N))
    left = max(calculate_energized_tiles(board, Coordinate.create(y, 0), Direction.RIGHT) for y in range(M))
    right = max(calculate_energized_tiles(board, Coordinate.create(y, N - 1), Direction.LEFT) for y in range(M))

    return max((top, bottom, left, right))

    pass


if __name__ == "__main__":
    from aoc_cas.util import solve_with_examples

    solve_with_examples(year=2023, day=16)
