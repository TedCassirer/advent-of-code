import aoc_cas.aoc2021.day11 as aoc

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


def testPartA():
    assert aoc.part_a(testData) == 1656


def testPartB():
    assert aoc.part_b(testData) == 195
