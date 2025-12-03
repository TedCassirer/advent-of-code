FLOOR = "."
EMPTY = "L"
OCCUPIED = "#"


def tick(grid, rule, seatsToConnected):
    _Y, _X = len(grid), len(grid[0])
    newGrid = [row.copy() for row in grid]
    totalSeatOccupied = 0
    for coord, connected in seatsToConnected.items():
        nearbyOccupied = sum(grid[y][x] == OCCUPIED for y, x in connected)
        currentlyOccupied = grid[coord[0]][coord[1]] == OCCUPIED
        updatedSeat = rule(currentlyOccupied, nearbyOccupied)
        newGrid[coord[0]][coord[1]] = updatedSeat
        totalSeatOccupied += updatedSeat == OCCUPIED

    return newGrid, totalSeatOccupied


def part_a(data):
    grid = [list(row) for row in data.splitlines()]
    Y, X = len(grid), len(grid[0])

    def nearbySeats(y, x):
        nearby = set()
        for iy in range(max(0, y - 1), min(Y, y + 2)):
            for ix in range(max(0, x - 1), min(X, x + 2)):
                if ix == x and iy == y:
                    continue
                if grid[iy][ix] != FLOOR:
                    nearby.add((iy, ix))
        return nearby

    def rule(occupied, nearbyOccupied):
        if occupied:
            return EMPTY if nearbyOccupied >= 4 else OCCUPIED
        else:
            return EMPTY if nearbyOccupied > 0 else OCCUPIED

    coords = ((y, x) for y in range(Y) for x in range(X))
    connectedSeats = {c: nearbySeats(*c) for c in coords if grid[c[0]][c[1]] != FLOOR}

    seen = set()
    occupiedSeats = 0
    while occupiedSeats not in seen:
        seen.add(occupiedSeats)
        grid, occupiedSeats = tick(grid, rule, connectedSeats)

    return occupiedSeats


def part_b(data):
    grid = [list(row) for row in data.splitlines()]
    Y, X = len(grid), len(grid[0])

    def nearbySeats(y, x):
        nearby = set()
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                iy = y + dy
                ix = x + dx
                while 0 <= iy < Y and 0 <= ix < X:
                    if grid[iy][ix] == FLOOR:
                        iy += dy
                        ix += dx
                        continue
                    else:
                        nearby.add((iy, ix))
                        break
        return nearby

    def rule(occupied, nearbyOccupied):
        if occupied:
            return EMPTY if nearbyOccupied >= 5 else OCCUPIED
        else:
            return EMPTY if nearbyOccupied > 0 else OCCUPIED

    coords = ((y, x) for y in range(Y) for x in range(X))
    connectedSeats = {c: nearbySeats(*c) for c in coords if grid[c[0]][c[1]] != FLOOR}

    seen = set()
    occupiedSeats = 0
    while occupiedSeats not in seen:
        seen.add(occupiedSeats)
        grid, occupiedSeats = tick(grid, rule, connectedSeats)

    return occupiedSeats
