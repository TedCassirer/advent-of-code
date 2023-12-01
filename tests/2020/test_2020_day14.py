from aoc2020 import day14 as aoc


def testPart1():
    data = """
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
    """.strip()
    assert aoc.part1(data) == 165


def testPart2():
    data = """
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
    """.strip()
    assert aoc.part2(data) == 208
