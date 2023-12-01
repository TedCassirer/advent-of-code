import aoc2020.day2 as aoc

testData = """
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""


def testPart1():
    assert aoc.part1(testData) == 2


def testPart2():
    assert aoc.part2(testData) == 1
