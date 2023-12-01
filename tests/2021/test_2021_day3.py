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


def testPartA():
    assert aoc.part_a(testData) == 198


def testPartB():
    assert aoc.part_b(testData) == 230
