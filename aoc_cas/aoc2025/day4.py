def parse_grid(input: str) -> set[tuple[int, int]]:
    grid: set[tuple[int, int]] = set()

    for y, line in enumerate(input.splitlines()):
        for x, char in enumerate(line):
            if char == "@":
                grid.add((y, x))
    return grid


def count_active_neighbors(grid: set[tuple[int, int]], row: int, col: int) -> int:
    directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]
    count = 0
    for dy, dx in directions:
        coord = row + dy, col + dx
        count += coord in grid
    return count


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
    while True:
        for row, col in grid:
            if count_active_neighbors(grid, row, col) < 4:
                ans += 1
                break
        else:
            return ans
        grid.remove((row, col))


if __name__ == "__main__":
    from aoc_cas.util import solve_with_example_input

    solve_with_example_input(year=2025, day=4, answers_a=[13])
