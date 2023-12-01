import aoc_cas.aoc2021.day14 as aoc

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


def testPartA():
    assert aoc.part_a(testData) == 1588


def testPartB():
    assert aoc.part_b(testData) == 2188189693529
