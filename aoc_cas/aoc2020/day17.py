from collections import Counter
from itertools import product


def getBuddies(coord):
    for diffVals in product((-1, 0, 1), repeat=len(coord)):
        if any(diffVals):
            yield tuple(c + dv for c, dv in zip(coord, diffVals))


def gameOfCube(activeCubes):
    coordsWithActiveBuddies = Counter(buddy for coord in activeCubes for buddy in getBuddies(coord))
    newActiveCubes = set()
    for coord, activeBuddies in coordsWithActiveBuddies.items():
        if activeBuddies == 3 or (coord in activeCubes and activeBuddies == 2):
            newActiveCubes.add(coord)
    return newActiveCubes


def createInitialState(data, dimensions):
    activeCubes = set()
    for x, line in enumerate(data.splitlines()):
        for y, val in enumerate(line):
            if val == "#":
                activeCubes.add((x, y) + (0,) * (dimensions - 2))
    return activeCubes


def part_a(data):
    activeCubes = createInitialState(data, 3)
    for i in range(6):
        activeCubes = gameOfCube(activeCubes)
    return len(activeCubes)


def part_b(data):
    activeCubes = createInitialState(data, 4)
    for i in range(6):
        activeCubes = gameOfCube(activeCubes)
    return len(activeCubes)
