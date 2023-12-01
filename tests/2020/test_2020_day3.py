import aoc_cas.aoc2020.day3 as aoc

testData = """
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
""".strip()


def testPartA():
    assert aoc.part_a(testData) == 7


def testPartB():
    assert aoc.part_b(testData) == 336
