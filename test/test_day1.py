import aoc

testData1 = """
    1721
    979
    366
    299
    675
    1456
"""


def testPart1():
    assert aoc.part1(1, 2020, testData1) == 514579


def testPart2():
    assert aoc.part2(1, 2020, testData1) == 241861950
