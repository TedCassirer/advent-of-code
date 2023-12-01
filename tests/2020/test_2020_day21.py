from aoc_cas.aoc2020 import day21 as aoc

data = """
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
""".strip()


def testPartA():
    assert aoc.part_a(data) == 5


def testPartB():
    assert aoc.part_b(data) == "mxmxvkd,sqjhc,fvjkl"
