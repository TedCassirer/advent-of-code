import aoc_cas.aoc2021.day3 as aoc

testData = """
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
""".strip()


def testPart1():
    assert aoc.part1(testData) == 198


def testPart2():
    assert aoc.part2(testData) == 230
