import aoc2022.day8 as aoc

testData = """
30373
25512
65332
33549
35390
""".strip()


def testPart1():
    assert aoc.part1(testData) == 21


def testPart2():
    assert aoc.part2(testData) == 8
