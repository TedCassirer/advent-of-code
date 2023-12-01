from collections import Counter
from itertools import product


def getBuddies(coord, size):
    for dy, dx in product((-1, 0, 1), repeat=2):
        if not (dy == 0 and dx == 0):
            y, x = (coord[0] + dy, coord[1] + dx)
            if 0 <= y < size[0] and 0 <= x < size[1]:
                yield y, x


def gameOfLight(activeLights, size):
    coordsWithActiveBuddies = Counter(buddy for coord in activeLights for buddy in getBuddies(coord, size))
    newActiveLights = set()
    for coord, activeBuddies in coordsWithActiveBuddies.items():
        if activeBuddies == 3 or (coord in activeLights and activeBuddies == 2):
            newActiveLights.add(coord)
    return newActiveLights


def createInitialState(data):
    activeLights = set()
    lines = data.splitlines()
    for x, line in enumerate(lines):
        for y, val in enumerate(line):
            if val == "#":
                activeLights.add((x, y))
    size = (len(lines), len(lines[0]))
    return size, activeLights


def part_a(data):
    size, curr = createInitialState(data)
    for _ in range(100):
        curr = gameOfLight(curr, size)
    return len(curr)


def part_b(data):
    size, curr = createInitialState(data)
    corners = {(0, 0), (size[0] - 1, 0), (0, size[0] - 1), (size[0] - 1, size[1] - 1)}
    for _ in range(100):
        curr.update(corners)
        curr = gameOfLight(curr, size)
    curr.update(corners)
    return len(curr)


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2015, day=18)

    print(part_a(data))
    print(part_b(data))
