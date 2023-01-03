import aoc_cas.aoc2022.day14 as aoc

testData = """
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
""".strip()


def testPart1():
    assert aoc.part1(testData) == 24


def testPart2():
    assert aoc.part2(testData) == 93


if __name__ == "__main__":
    # testPart1()
    testPart2()
