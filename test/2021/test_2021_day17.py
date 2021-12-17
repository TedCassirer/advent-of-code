import aoc_cas.aoc2021.day17 as aoc


def testPart1():
    assert aoc.part1("target area: x=20..30, y=-10..-5") == 45


def testPart2():
    assert aoc.part2("target area: x=20..30, y=-10..-5") == 112
