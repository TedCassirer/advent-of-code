def buildGrid(data):
    grid = set()

    for path in data.splitlines():
        points = []
        for p in path.split(' -> '):
            point = tuple(map(int, p.split(',')))
            points.append(point)
        for (x1, y1), (x2, y2) in zip(points, points[1:]):
            if x1 == x2:
                y1, y2 = sorted((y1, y2))
                for y in range(y1, y2+1):
                    grid.add((y, x1))
            else:
                x1, x2 = sorted((x1, x2))
                for x in range(x1, x2+1):
                    grid.add((y1, x))
    
    return grid


def printGrid(grid):
    minY = min(grid)[0]
    maxY = max(grid)[0]
    minX = min(p[1] for p in grid)
    maxX = max(p[1] for p in grid)

    display = [["."]*(maxX-minX+3) for _ in range(maxY - minY+3)]
    for y, x in grid:
        display[y-minY+1][x-minX+1] = '#'

    for row in display:
        print(''.join(row))
    
    print()

def dropSand(grid, row, col, floor=-1):
    ground = min((p[0] for p in grid if p[1] == col and p[0] > row), default=floor)
    if ground == -1:
        return True
    while ground > row:
        if ground == floor:
            grid.add((ground-1, col))
            ground -= 1
        elif (ground, col-1) not in grid:
            if dropSand(grid, ground, col-1, floor):
                return True
        elif (ground, col+1) not in grid:
            if dropSand(grid, ground, col+1, floor):
                return True
        else:
            grid.add((ground-1, col))
            ground -= 1
    return False






def part1(data):
    grid = buildGrid(data)

    floors = len(grid)
    dropSand(grid, 0, 500)
    sand = len(grid) - floors
    return sand



def part2(data):
    grid = buildGrid(data)
    floorLevel = max(p[0] for p in grid) + 2
    floors = len(grid)
    dropSand(grid, 0, 500, floor=floorLevel)
    sand = len(grid) - floors
    return sand


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2022, day=14)

    print(part1(data))
    print(part2(data))
