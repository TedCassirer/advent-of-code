import aoc2021.day1 as aoc

testData = """
    199
    200
    208
    210
    200
    207
    240
    269
    260
    263
""".strip()


def testPart1():
    assert aoc.part1(testData) == 7


def testPart2():
    assert aoc.part2(testData) == 5
