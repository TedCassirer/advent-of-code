from aoc_cas.aoc2020 import day12 as aoc


data = """
F10
N3
F7
R90
F11
""".strip()


def testPart1():
    assert aoc.part1(data) == 25


def testPart2():
    assert aoc.part2(data) == 286
