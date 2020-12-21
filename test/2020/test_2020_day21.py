from aoc_cas.aoc2020 import day21 as aoc

data = """
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
""".strip()


def testPart1():
    assert aoc.part1(data) == 5


def testPart2():
    assert aoc.part2(data) == "mxmxvkd,sqjhc,fvjkl"
