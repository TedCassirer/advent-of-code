from aoc_cas.aoc2020 import day6 as aoc


def testPartA():
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
    assert aoc.part_a(data) == 11


def testPartB():
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
    assert aoc.part_b(data) == 6
