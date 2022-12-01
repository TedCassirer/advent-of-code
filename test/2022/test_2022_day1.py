import aoc_cas.aoc2022.day1 as aoc

testData = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
""".strip()


def testPart1():
    assert aoc.part1(testData) == 24000


def testPart2():
    assert aoc.part2(testData) == 45000
