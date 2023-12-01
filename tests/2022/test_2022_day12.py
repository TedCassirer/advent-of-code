import aoc2022.day12 as aoc

testData = """
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
""".strip()


def testPart1():
    assert aoc.part1(testData) == 31


def testPart2():
    assert aoc.part2(testData) == 29
