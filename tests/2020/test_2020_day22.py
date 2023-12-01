from aoc_cas.aoc2020 import day22 as aoc

data = """
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
""".strip()


def testPartA():
    assert aoc.part_a(data) == 306


def testPartB():
    assert aoc.part_b(data) == 291
