import aoc_cas.aoc2021.day15 as aoc

testData = """
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
""".strip()


def testPartA():
    assert aoc.part_a(testData) == 40


def testPartB():
    assert aoc.part_b(testData) == 315
