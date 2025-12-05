from typing import Iterator

Coordinate = tuple[int, int]


def parse_grid(input: str) -> set[Coordinate]:
    grid: set[Coordinate] = set()

    for y, line in enumerate(input.splitlines()):
        for x, char in enumerate(line):
            if char == "@":
                grid.add((y, x))
    return grid


def count_active_neighbors(grid: set[Coordinate], row: int, col: int) -> int:
    count = 0
    for coord in neighbors(row, col):
        count += coord in grid
    return count


def neighbors(row: int, col: int) -> Iterator[Coordinate]:
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if dy != 0 or dx != 0:
                yield row + dy, col + dx


def part_a(input: str) -> int:
    grid = parse_grid(input)
    ans = 0
    for row, col in grid:
        if count_active_neighbors(grid, row, col) < 4:
            ans += 1
    return ans


def part_b(input: str) -> int:
    grid = parse_grid(input)
    ans = 0
    to_check = set(grid)
    while to_check:
        coord = to_check.pop()
        if count_active_neighbors(grid, *coord) < 4:
            ans += 1
            grid.remove(coord)
            to_check.update(c for c in neighbors(*coord) if c in grid)
    return ans


if __name__ == "__main__":
    from aoc_cas.util import solve_with_example_input

    solve_with_example_input(year=2025, day=4, answers_a=[13])
