import aoc_cas.aoc2021.day2 as aoc

testData = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
""".strip()


def testPartA():
    assert aoc.part_a(testData) == 150


def testPartB():
    assert aoc.part_b(testData) == 900
