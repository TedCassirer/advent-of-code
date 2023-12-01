def getGrid(data):
    return [[int(n) for n in row] for row in data.splitlines()]


def lowPoints(grid):
    M, N = len(grid), len(grid[0])
    for y, row in enumerate(grid):
        for x, n in enumerate(row):
            right = grid[y][x + 1] if x != N - 1 else 9
            up = grid[y - 1][x] if y != 0 else 9
            left = grid[y][x - 1] if x != 0 else 9
            down = grid[y + 1][x] if y != M - 1 else 9
            if n < min((right, up, left, down)):
                yield y, x


def bfs(grid, y, x):
    if grid[y][x] == 9:
        return []

    M, N = len(grid), len(grid[0])

    basin = set()
    stack = [(y, x)]
    while stack:
        y, x = stack.pop()
        if (y, x) in basin or y < 0 or y == M or x < 0 or x == N or grid[y][x] == 9:
            continue
        basin.add((y, x))
        stack.extend([(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)])
    return basin


def part_a(data):
    grid = getGrid(data)
    return sum(1 + grid[y][x] for y, x in lowPoints(grid))


def part_b(data):
    grid = getGrid(data)
    M, N = len(grid), len(grid[0])
    basins = []
    seen = set()
    for y in range(M):
        for x in range(N):
            if (y, x) in seen:
                continue
            basin = bfs(grid, y, x)
            basins.append(len(basin))
            seen.update(basin)
    b1, b2, b3 = sorted(basins, reverse=True)[:3]
    return b1 * b2 * b3


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2021, day=9)

    print(part_a(data))
    print(part_b(data))
