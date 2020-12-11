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


def testPart1():
    assert aoc.part1(data) == 37


def testPart2():
    assert aoc.part2(data) == 26
