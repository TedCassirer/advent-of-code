import aoc2021.day14 as aoc

testData = """
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
""".strip()


def testPart1():
    assert aoc.part1(testData) == 1588


def testPart2():
    assert aoc.part2(testData) == 2188189693529
