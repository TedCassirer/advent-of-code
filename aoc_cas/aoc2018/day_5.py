from itertools import filterfalse
from utils import readData, timeIt


def reactPolymer(polymer):
    result = []
    for s in polymer:
        if result and s.swapcase() == result[-1]:
            result.pop()
        else:
            result.append(s)
    return result


@timeIt
def part_a():
    polymer = next(readData("2018/data/day_5"))
    return len(reactPolymer(polymer))


@timeIt
def part_b():
    polymer = next(readData("2018/data/day_5"))
    polymerPairs = {(p, p.upper()) for p in polymer if p.islower()}
    reducedForms = map(lambda pp: filterfalse(pp.__contains__, polymer), polymerPairs)
    reactedPolymers = map(reactPolymer, reducedForms)
    return min(map(len, reactedPolymers))


if __name__ == "__main__":
    print("Part A:", part_a())
    print("Part B:", part_b())
