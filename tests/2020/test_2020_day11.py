from aoc_cas.aoc2020 import day11 as aoc


data = """
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
""".strip()


def testPartA():
    assert aoc.part_a(data) == 37


def testPartB():
    assert aoc.part_b(data) == 26
