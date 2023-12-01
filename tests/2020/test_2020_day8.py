from aoc2020 import day8 as aoc


testProgram = """
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
""".strip()


def testPart1():
    assert aoc.part1(testProgram) == 5


def testPart2():
    assert aoc.part2(testProgram) == 8
