import aoc_cas.aoc2022.day14 as aoc

testData = """
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
""".strip()


def testPartA():
    assert aoc.part_a(testData) == 24


def testPartB():
    assert aoc.part_b(testData) == 93


if __name__ == "__main__":
    testPartA()
    testPartB()
