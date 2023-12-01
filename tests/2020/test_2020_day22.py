from aoc2020 import day22 as aoc

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


def testPart1():
    assert aoc.part1(data) == 306


def testPart2():
    assert aoc.part2(data) == 291
