from aoc_cas.aoc2020 import day23 as aoc
import pytest

data = "389125467"


def testPartA():
    assert aoc.part_a(data) == 67384529


@pytest.mark.skip(reason="Too slow to run every time")
def testPartB():
    assert aoc.part_b(data) == 149245887792
