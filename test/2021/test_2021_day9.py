import aoc_cas.aoc2021.day9 as aoc

testData = """
2199943210
3987894921
9856789892
8767896789
9899965678
""".strip()


def testPart1():
    assert aoc.part1(testData) == 15


def testPart2():
    assert aoc.part2(testData) == 1134
