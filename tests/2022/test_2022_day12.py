import aoc_cas.aoc2022.day12 as aoc

testData = """
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
""".strip()


def testPartA():
    assert aoc.part_a(testData) == 31


def testPartB():
    assert aoc.part_b(testData) == 29
