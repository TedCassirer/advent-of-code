import heapq


def extendGrid(grid):
    M, N = len(grid), len(grid[0])
    bigGrid = [[0] * N * 5 for _ in range(5 * M)]
    for y in range(5 * M):
        for x in range(5 * N):
            dy, iy = divmod(y, M)
            dx, ix = divmod(x, N)
            bigGrid[y][x] = (((grid[iy][ix] + dy + dx) - 1) % 9) + 1

    return bigGrid


def search(grid):
    queue = [(0, 0, 0)]
    M, N = len(grid), len(grid[0])
    seen = dict()
    while queue:
        cost, y, x = heapq.heappop(queue)
        if y == M - 1 and x == N - 1:
            return cost
        for ny, nx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
            if ny == -1 or ny == M or nx == -1 or nx == N:
                continue
            nCost = cost + grid[ny][nx]
            if seen.get((ny, nx), 1 << 31) > nCost:
                seen[(ny, nx)] = nCost
                heapq.heappush(queue, (cost + grid[ny][nx], ny, nx))


def part1(data):
    grid = [[*map(int, row)] for row in data.splitlines()]
    return search(grid)


def part2(data):
    grid = [[*map(int, row)] for row in data.splitlines()]
    return search(extendGrid(grid))


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2021, day=15)

    print(part1(data))
    print(part2(data))
