def getDirs(data):
    parts = data.split(", ")
    y, x = 1, 0
    for part in parts:
        d, n = part[0], int(part[1:])
        if d == "R":
            y, x = -x, y
        else:
            y, x = x, -y
        yield n * y, n * x


def getCoords(y, x, dy, dx):
    for yy in range(y, y + dy, 1 if dy > 0 else -1):
        yield (yy, x)
    for xx in range(x, x + dx, 1 if dx > 0 else -1):
        yield (y, xx)


def part_a(data):
    y, x = 0, 0
    for dy, dx in getDirs(data):
        y += dy
        x += dx
    return abs(y) + abs(x)


def part_b(data):
    y, x = 0, 0
    visited = set()
    for dy, dx in getDirs(data):
        for coord in getCoords(y, x, dy, dx):
            if coord in visited:
                return sum(map(abs, coord))
            visited.add(coord)
        y += dy
        x += dx


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2016, day=1)
    print(part_a(data))
    print(part_b(data))
