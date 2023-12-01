import aoc_cas.aoc2020.day2 as aoc

testData = """
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""


def testPartA():
    assert aoc.part_a(testData) == 2


def testPartB():
    assert aoc.part_b(testData) == 1
