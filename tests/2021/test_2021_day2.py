import aoc2021.day2 as aoc

testData = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
""".strip()


def testPart1():
    assert aoc.part1(testData) == 150


def testPart2():
    assert aoc.part2(testData) == 900
