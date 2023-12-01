import aoc_cas.aoc2022.day3 as aoc

testData = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
""".strip()


def testPartA():
    assert aoc.part_a(testData) == 157


def testPartB():
    assert aoc.part_b(testData) == 70
