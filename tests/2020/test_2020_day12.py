from aoc_cas.aoc2020 import day12 as aoc


data = """
F10
N3
F7
R90
F11
""".strip()


def testPartA():
    assert aoc.part_a(data) == 25


def testPartB():
    assert aoc.part_b(data) == 286
