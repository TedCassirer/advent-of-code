import aoc_cas.aoc2020.day1 as aoc

testData1 = """
    1721
    979
    366
    299
    675
    1456
"""


def testPart1():
    assert aoc.part1(testData1) == 514579


def testPart2():
    assert aoc.part2(testData1) == 241861950
