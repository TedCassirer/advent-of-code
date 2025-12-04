import re

REGEX = re.compile(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)")


def parseSensorsAndBeacons(data):
    for line in data.splitlines():
        match = REGEX.search(line)
        if not match:
            raise ValueError(f"Unable to parse sensor line: {line}")
        sx, sy, bx, by = map(int, match.groups())
        yield (sy, sx), (by, bx)


def manhattanDistance(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])


def part_a(data, row=2000000):
    noBeacon = set()
    onRow = set()
    for sensor, beacon in parseSensorsAndBeacons(data):
        dist = manhattanDistance(sensor, beacon)
        distToRow = abs(sensor[0] - row)
        if distToRow > dist:
            continue
        width = dist - distToRow
        noBeacon.update(range(sensor[1] - width, sensor[1] + width + 1))
        if sensor[0] == row:
            onRow.add(sensor[1])
        if beacon[0] == row:
            onRow.add(beacon[1])
    return len(noBeacon) - len(onRow)


def part_b(data, searchSpace=4000000):
    rows = [[(-1, -1), (searchSpace + 1, searchSpace + 1)] for _ in range(searchSpace + 1)]
    for sensor, beacon in parseSensorsAndBeacons(data):
        dist = manhattanDistance(sensor, beacon)
        top = max(0, sensor[0] - dist)
        bottom = min(searchSpace, sensor[0] + dist)
        for row in range(top, bottom + 1):
            width = dist - abs(row - sensor[0])
            left = max(0, sensor[1] - width)
            right = min(searchSpace + 1, sensor[1] + width)
            rows[row].append((left, right))

    for y, row in enumerate(rows):
        row.sort()
        x = 0
        for left_bound, right_bound in row:
            if right_bound <= x:
                continue
            if x + 1 < left_bound:
                return (x + 1) * 4000000 + y
            x = max(x, right_bound)


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2022, day=15)

    print(part_a(data))
    print(part_b(data))
