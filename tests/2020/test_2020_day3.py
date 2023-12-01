import aoc2020.day3 as aoc

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


def testPart1():
    assert aoc.part1(testData) == 7


def testPart2():
    assert aoc.part2(testData) == 336
