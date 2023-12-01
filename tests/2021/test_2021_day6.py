import aoc2021.day6 as aoc

testData = """
3,4,3,1,2
""".strip()


def testPart1():
    assert aoc.part1(testData) == 5934


def testPart2():
    assert aoc.part2(testData) == 26984457539
