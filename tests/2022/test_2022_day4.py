import aoc2022.day4 as aoc

testData = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
""".strip()


def testPart1():
    assert aoc.part1(testData) == 2


def testPart2():
    assert aoc.part2(testData) == 4
