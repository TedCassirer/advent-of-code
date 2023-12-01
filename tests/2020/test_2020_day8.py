from aoc_cas.aoc2020 import day8 as aoc


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


def testPartA():
    assert aoc.part_a(testProgram) == 5


def testPartB():
    assert aoc.part_b(testProgram) == 8
