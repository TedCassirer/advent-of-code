def step(grid):
    M, N = len(grid), len(grid[0])
    allFlashes = set()
    flashed = set()
    for y in range(M):
        for x in range(N):
            grid[y][x] += 1
            if grid[y][x] == 10:
                flashed.add((y, x))
    while flashed:
        allFlashes.update(flashed)
        nxt = set()
        for y, x in flashed:
            for iy in range(max(0, y - 1), min(M, y + 2)):
                for ix in range(max(0, x - 1), min(N, x + 2)):
                    if iy == y and ix == x:
                        continue
                    grid[iy][ix] += 1
                    if grid[iy][ix] == 10:
                        nxt.add((iy, ix))
        flashed = nxt

    for y, x in allFlashes:
        grid[y][x] = 0
    return len(allFlashes)


def part1(data):
    grid = [[int(n) for n in row] for row in data.splitlines()]
    flashes = 0
    for t in range(100):
        flashes += step(grid)
    return flashes


def part2(data):
    grid = [[int(n) for n in row] for row in data.splitlines()]
    tentacleBoys = len(grid) * len(grid[0])
    for t in range(1, 1 << 31):
        if step(grid) == tentacleBoys:
            return t


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2021, day=11)

    print(part1(data))
    print(part2(data))
