import aoc_cas.aoc2021.day9 as aoc

testData = """
2199943210
3987894921
9856789892
8767896789
9899965678
""".strip()


def testPartA():
    assert aoc.part_a(testData) == 15


def testPartB():
    assert aoc.part_b(testData) == 1134
