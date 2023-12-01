from aoc_cas.aoc2020 import day13 as aoc


data = """
939
7,13,x,x,59,x,31,19
""".strip()


def testPartA():
    assert aoc.part_a(data) == 5 * 59


def testPartB():
    assert aoc.part_b("\n17,x,13,19") == 3417
    assert aoc.part_b("\n67,7,59,61") == 754018
    assert aoc.part_b("\n67,x,7,59,61") == 779210
    assert aoc.part_b("\n67,7,x,59,61") == 1261476
    assert aoc.part_b("\n1789,37,47,1889") == 1202161486
    assert aoc.part_b("\n7,13,x,x,59,x,31,19") == 1068781
