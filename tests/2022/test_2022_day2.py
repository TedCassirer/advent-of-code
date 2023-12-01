import aoc2022.day2 as aoc

testData = """
A Y
B X
C Z
""".strip()


def testPart1():
    assert aoc.part1(testData) == 15


def testPart2():
    assert aoc.part2(testData) == 12
