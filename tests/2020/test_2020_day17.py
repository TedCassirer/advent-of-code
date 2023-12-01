from aoc_cas.aoc2020 import day17 as aoc


data = """
.#.
..#
###
""".strip()


def testPartA():
    assert aoc.part_a(data) == 112


def testPartB():
    assert aoc.part_b(data) == 848
