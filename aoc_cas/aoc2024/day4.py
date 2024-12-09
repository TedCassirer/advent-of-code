from aoc_cas.util import solve_with_input

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
NE = (-1, 1)
NW = (-1, -1)
SE = (1, 1)
SW = (1, -1)


def _count_xmas(grid: list[list[str]], y: int, x: int) -> int:
    M, N = len(grid), len(grid[0])
    word_to_find = "XMAS"
    word_count = 0
    for dy, dx in [UP, DOWN, LEFT, RIGHT, NE, NW, SE, SW]:
        for i, c in enumerate(word_to_find):
            yy, xx = y + dy * i, x + dx * i
            if not (0 <= yy < M and 0 <= xx < N) or grid[yy][xx] != c:
                break
        else:
            word_count += 1
    return word_count


def _parse_data(data: str) -> list[list[str]]:
    return [list(line) for line in data.splitlines()]


def part_a(data: str) -> int:
    grid = _parse_data(data)
    M, N = len(grid), len(grid[0])
    xmas_count = 0
    for y in range(M):
        for x in range(N):
            xmas_count += _count_xmas(grid, y, x)
    return xmas_count


def _is_mas_x(grid: list[list[str]], y: int, x: int) -> bool:
    M, N = len(grid), len(grid[0])
    if not (1 <= y < M - 1 and 1 <= x < N - 1):
        # OOB
        return False
    # Build a string of the current cell and its diagonal neighbors
    # 5.2
    # .1.
    # 4.3
    coords = ((y + dy, x + dx) for dy, dx in [(0, 0), NE, SE, SW, NW])
    x_string = "".join(grid[yy][xx] for yy, xx in coords)
    # Check if the string is is a MAS X
    return x_string in {"AMMSS", "ASSMM", "AMSSM", "ASMMS"}


def part_b(data: str) -> int:
    grid = _parse_data(data)
    M, N = len(grid), len(grid[0])
    return sum(_is_mas_x(grid, y, x) for y in range(M) for x in range(N))


if __name__ == "__main__":
    data = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
""".strip()
    solve_with_input(2024, 4, data, answer_a=18, answer_b=9)
