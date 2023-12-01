import aoc_cas.aoc2021.day17 as aoc


def testPartA():
    assert aoc.part_a("target area: x=20..30, y=-10..-5") == 45


def testPartB():
    assert aoc.part_b("target area: x=20..30, y=-10..-5") == 112
