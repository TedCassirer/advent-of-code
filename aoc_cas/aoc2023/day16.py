import dataclasses

from aoc_cas.common import Direction, Coordinate, DIR_UP, DIR_RIGHT, DIR_LEFT, DIR_DOWN

reflections: dict[str, dict[Direction, tuple[Direction, ...]]] = {
    "/": {
        DIR_UP: (DIR_RIGHT,),
        DIR_LEFT: (DIR_DOWN,),
        DIR_DOWN: (DIR_LEFT,),
        DIR_RIGHT: (DIR_UP,),
    },
    "\\": {
        DIR_UP: (DIR_LEFT,),
        DIR_LEFT: (DIR_UP,),
        DIR_DOWN: (DIR_RIGHT,),
        DIR_RIGHT: (DIR_DOWN,),
    },
    "|": {
        DIR_UP: (DIR_UP,),
        DIR_LEFT: (DIR_UP, DIR_DOWN),
        DIR_DOWN: (DIR_DOWN,),
        DIR_RIGHT: (DIR_UP, DIR_DOWN),
    },
    "-": {
        DIR_UP: (DIR_LEFT, DIR_RIGHT),
        DIR_LEFT: (DIR_LEFT,),
        DIR_DOWN: (DIR_LEFT, DIR_RIGHT),
        DIR_RIGHT: (DIR_RIGHT,),
    },
    ".": {
        DIR_UP: (DIR_UP,),
        DIR_LEFT: (DIR_LEFT,),
        DIR_DOWN: (DIR_DOWN,),
        DIR_RIGHT: (DIR_RIGHT,),
    },
}


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

    return calculate_energized_tiles(board, Coordinate.create(0, 0), DIR_RIGHT)


def part_b(data: str) -> int:
    board = data.splitlines()
    M, N = len(board), len(board[0])
    top = max(calculate_energized_tiles(board, Coordinate.create(0, x), DIR_DOWN) for x in range(N))
    bottom = max(calculate_energized_tiles(board, Coordinate.create(M - 1, x), DIR_UP) for x in range(N))
    left = max(calculate_energized_tiles(board, Coordinate.create(y, 0), DIR_RIGHT) for y in range(M))
    right = max(calculate_energized_tiles(board, Coordinate.create(y, N - 1), DIR_LEFT) for y in range(M))

    return max((top, bottom, left, right))

    pass


if __name__ == "__main__":
    from aoc_cas.util import solve_with_example_data

    solve_with_example_data(year=2023, day=16)
