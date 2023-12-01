import aoc_cas.aoc2022.day4 as aoc

testData = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
""".strip()


def testPartA():
    assert aoc.part_a(testData) == 2


def testPartB():
    assert aoc.part_b(testData) == 4
