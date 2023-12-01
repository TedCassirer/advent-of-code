from aoc2020 import day17 as aoc


data = """
.#.
..#
###
""".strip()


def testPart1():
    assert aoc.part1(data) == 112


def testPart2():
    assert aoc.part2(data) == 848
