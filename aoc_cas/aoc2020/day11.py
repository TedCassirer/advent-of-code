FLOOR = "."
EMPTY = "L"
OCCUPIED = "#"


def getNearbySeats(y, x, Y, X, grid, floorOk=True):
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue
            iy = y + dy
            ix = x + dx
            while 0 <= iy < Y and 0 <= ix < X:
                if grid[iy][ix] == FLOOR:
                    if floorOk:
                        yield iy, ix
                        break
                    iy += dy
                    ix += dx
                    continue
                else:
                    yield iy, ix
                    break


def tick(grid, floorOk=True):
    Y, X = len(grid), len(grid[0])
    newGrid = []
    occupiedSeats = 0
    for y, row in enumerate(grid):
        newRow = []
        for x, tile in enumerate(row):
            if tile == FLOOR:
                newRow.append(tile)
                continue
            nearbySeats = [grid[iy][ix] for iy, ix in getNearbySeats(y, x, Y, X, grid, floorOk)]
            # print(nearbySeats)
            occupied = nearbySeats.count(OCCUPIED)
            if tile == EMPTY:
                tile = OCCUPIED if occupied == 0 else EMPTY
            elif tile == OCCUPIED:
                tile = EMPTY if occupied >= (5 - floorOk) else OCCUPIED
            else:
                tile = FLOOR
            occupiedSeats += tile == OCCUPIED
            newRow.append(tile)
        newGrid.append("".join(newRow))
    return newGrid, occupiedSeats


def part1(data):
    grid = data.splitlines()

    seen = set()
    occupiedSeats = 0

    while occupiedSeats not in seen:
        seen.add(occupiedSeats)
        grid, occupiedSeats = tick(grid)

    return occupiedSeats


def part2(data):
    grid = data.splitlines()

    seen = set()
    occupiedSeats = 0

    while occupiedSeats not in seen:
        seen.add(occupiedSeats)
        # print(occupiedSeats)
        # print(*grid, sep='\n')
        # print('\n---------\n')
        grid, occupiedSeats = tick(grid, floorOk=False)

    return occupiedSeats
