import aoc_cas.aoc2021.day7 as aoc

testData = """
16,1,2,0,4,2,7,1,2,14
""".strip()


def testPart1():
    assert aoc.part1(testData) == 37


def testPart2():
    assert aoc.part2(testData) == 168
