import aoc2021.day11 as aoc

testData = """
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
""".strip()


def testPart1():
    assert aoc.part1(testData) == 1656


def testPart2():
    assert aoc.part2(testData) == 195
