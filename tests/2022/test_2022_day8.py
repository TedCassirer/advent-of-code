import aoc_cas.aoc2022.day8 as aoc

testData = """
30373
25512
65332
33549
35390
""".strip()


def testPartA():
    assert aoc.part_a(testData) == 21


def testPartB():
    assert aoc.part_b(testData) == 8
