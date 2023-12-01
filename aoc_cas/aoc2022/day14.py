def buildGrid(data):
    walls = set()

    for path in data.splitlines():
        points = []
        for p in path.split(" -> "):
            point = tuple(map(int, p.split(",")))
            points.append(point)
        for (x1, y1), (x2, y2) in zip(points, points[1:]):
            if x1 == x2:
                y1, y2 = sorted((y1, y2))
                for y in range(y1, y2 + 1):
                    walls.add((y, x1))
            else:
                x1, x2 = sorted((x1, x2))
                for x in range(x1, x2 + 1):
                    walls.add((y1, x))

    minY = min(walls)[0]
    maxY = max(walls)[0]
    minX = min(p[1] for p in walls) - maxY
    maxX = max(p[1] for p in walls) + maxY

    grid = [["."] * (maxX - minX) for _ in range(maxY + 3)]
    for y, x in walls:
        grid[y][x - minX] = "#"
    return grid, minY, minX, maxY, maxX


def dropSand(grid, row, col, floor=-1):
    ground = row
    while ground != floor and grid[ground][col] == ".":
        ground += 1
        if ground == len(grid):
            # Fell to the abyss
            return 0, True
    sand = 0
    while ground > row:
        if ground == floor:
            grid[ground - 1][col] = "o"
            sand += 1
            ground -= 1
        elif grid[ground][col - 1] == ".":
            newSand, abyss = dropSand(grid, ground, col - 1, floor)
            sand += newSand
            if abyss:
                return sand, True
        elif grid[ground][col + 1] == ".":
            newSand, abyss = dropSand(grid, ground, col + 1, floor)
            sand += newSand
            if abyss:
                return sand, True
        else:
            grid[ground - 1][col] = "o"
            ground -= 1
            sand += 1
    return sand, False


def part_a(data):
    grid, minY, minX, maxY, maxX = buildGrid(data)
    sand, _ = dropSand(grid, 0, 500 - minX)
    return sand


def part_b(data):
    grid, minY, minX, maxY, maxX = buildGrid(data)

    floorLevel = maxY + 2
    sand, _ = dropSand(grid, 0, 500 - minX, floor=floorLevel)
    return sand


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2022, day=14)

    print(part_a(data))
    print(part_b(data))
