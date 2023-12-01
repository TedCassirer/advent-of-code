import aoc_cas.aoc2022.day2 as aoc

testData = """
A Y
B X
C Z
""".strip()


def testPartA():
    assert aoc.part_a(testData) == 15


def testPartB():
    assert aoc.part_b(testData) == 12
