import aoc2021.day15 as aoc

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


def testPart1():
    assert aoc.part1(testData) == 40


def testPart2():
    assert aoc.part2(testData) == 315
