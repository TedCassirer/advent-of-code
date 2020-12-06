from aoc_cas.aoc2020 import day6 as aoc


def testPart1():
    data = """
abc

a
b
c

ab
ac

a
a
a
a

b
""".strip()
    assert aoc.part1(data) == 11


def testPart2():
    data = """
abc

a
b
c

ab
ac

a
a
a
a

b
""".strip()
    assert aoc.part2(data) == 6
