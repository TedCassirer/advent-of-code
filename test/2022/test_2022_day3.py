import aoc_cas.aoc2022.day3 as aoc

testData = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw

""".strip()


def testPart1():
    assert aoc.part1(testData) == 157


def testPart2():
    assert aoc.part2(testData) == 70
