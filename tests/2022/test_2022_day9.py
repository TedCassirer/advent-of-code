import aoc_cas.aoc2022.day9 as aoc


def testPart1():
    testData = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
""".strip()
    assert aoc.part1(testData) == 13


def testPart2():
    testData = """
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20""".strip()
    assert aoc.part2(testData) == 36
