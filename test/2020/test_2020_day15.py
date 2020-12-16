from aoc_cas.aoc2020 import day15 as aoc
import pytest


def testPart1():
    data = [("0,3,6", 436), ("1,3,2", 1), ("2,1,3", 10), ("1,2,3", 27), ("2,3,1", 78), ("3,2,1", 438), ("3,1,2", 1836)]
    for d, e in data:
        assert aoc.part1(d) == e


@pytest.mark.skip(reason="Too slow to run every time")
def testPart2():
    data = [
        ("0,3,6", 175594),
        ("1,3,2", 2578),
        ("2,1,3", 3544142),
        ("1,2,3", 261214),
        ("2,3,1", 6895259),
        ("3,2,1", 18),
        ("3,1,2", 362),
    ]
    for d, e in data:
        assert aoc.part2(d) == e
