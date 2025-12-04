def parse_grid(input: str) -> list[list[bool]]:
    grid: list[list[bool]] = []
    for line in input.splitlines():
        row: list[bool] = []
        for char in line:
            if char == "@":
                row.append(True)
            else:
                row.append(False)
        grid.append(row)
    return grid


def count_active_neighbors(grid: list[list[bool]], row: int, col: int) -> int:
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
        new_row, new_col = row + dy, col + dx
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col]:
            count += 1
    return count


def part_a(input: str) -> int:
    grid = parse_grid(input)
    ans = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] and count_active_neighbors(grid, y, x) < 4:
                ans += 1
    return ans


def part_b(input: str) -> int:
    grid = parse_grid(input)
    ans = 0
    keep_going = True
    while keep_going:
        keep_going = False
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] and count_active_neighbors(grid, y, x) < 4:
                    ans += 1
                    grid[y][x] = False
                    keep_going = True
    return ans


if __name__ == "__main__":
    from aoc_cas.util import solve_with_example_input

    solve_with_example_input(year=2025, day=4)
