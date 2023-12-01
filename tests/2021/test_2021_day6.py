import aoc_cas.aoc2021.day6 as aoc

testData = """
3,4,3,1,2
""".strip()


def testPartA():
    assert aoc.part_a(testData) == 5934


def testPartB():
    assert aoc.part_b(testData) == 26984457539
