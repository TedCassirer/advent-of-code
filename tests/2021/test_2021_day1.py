import aoc_cas.aoc2021.day1 as aoc

testData = """
    199
    200
    208
    210
    200
    207
    240
    269
    260
    263
""".strip()


def testPartA():
    assert aoc.part_a(testData) == 7


def testPartB():
    assert aoc.part_b(testData) == 5
