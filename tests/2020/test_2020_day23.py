from aoc_cas.aoc2020 import day23 as aoc
import pytest

data = "389125467"


def testPart1():
    assert aoc.part1(data) == 67384529


@pytest.mark.skip(reason="Too slow to run every time")
def testPart2():
    assert aoc.part2(data) == 149245887792
