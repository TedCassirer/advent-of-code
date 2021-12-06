import aoc_cas.aoc2021.day5 as aoc

testData = """
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
""".strip()


def testPart1():
    assert aoc.part1(testData) == 5


def testPart2():
    assert aoc.part2(testData) == 12
