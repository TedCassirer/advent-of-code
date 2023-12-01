import aoc_cas.aoc2021.day7 as aoc

testData = """
16,1,2,0,4,2,7,1,2,14
""".strip()


def testPartA():
    assert aoc.part_a(testData) == 37


def testPartB():
    assert aoc.part_b(testData) == 168
