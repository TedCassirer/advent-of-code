from .IntCodeComputer import IntCodeComputerVM, manual_input, read_program
from itertools import chain

animate = 0


def ascii_input():
    while True:
        yield from (ord(i) for i in input("Input: "))
        yield ord("\n")


def part1(data):
    program = read_program(data)
    vm = IntCodeComputerVM(program)
    s = []
    row = []
    for r in vm.run():
        char = chr(r)
        if char == "\n":
            s.append(row)
            row = []
        else:
            row.append(char)

    scaffold_coords = set()
    for y, row in enumerate(s):
        for x, char in enumerate(row):
            if char == "#":
                scaffold_coords.add((y, x))

    intersections = set()
    for y, x in scaffold_coords:
        if (
            (y - 1, x) in scaffold_coords
            and (y + 1, x) in scaffold_coords
            and (y, x - 1) in scaffold_coords
            and (y, x + 1) in scaffold_coords
        ):
            s[y][x] = "O"
            intersections.add((y, x))
    if animate:
        for row in s:
            print("".join(row))

    return sum(y * x for y, x in intersections)


def part2(data):
    """
    Manual solution

    Movements: R,8,L,10,R,8,R,12,R,8,L,8,L,12,R,8,L,10,R,8,L,12,L,10,L,8,R,8,L,10,R,8,R,12,R,8,L,8,L,12,L,12,L,10,L,8,L,12,L,10,L,8,R,8,L,10,R,8,R,12,R,8,L,8,L,12
    Main: A,B,A,C,A,B,C,C,A,B
    A: R,8,L,10,R,8
    B: R,12,R,8,L,8,L,12
    C: L,12,L,10,L,8
    """

    main = map(ord, "A,B,A,C,A,B,C,C,A,B")
    A = map(ord, "R,8,L,10,R,8")
    B = map(ord, "R,12,R,8,L,8,L,12")
    C = map(ord, "L,12,L,10,L,8")
    videoFeed = map(ord, "1")

    solutionInput = chain(main, A, B, C, videoFeed)
    program = read_program(data)
    program[0] = 2
    vm = IntCodeComputerVM(program)
    vm.input_provided_from(solutionInput)
    s = []
    row = []
    for r in vm.run():
        char = chr(r)
        if char == "\n":
            s.append(row)
            if animate:
                print("".join(row))
            row = []
        else:
            row.append(char)
    return vm.out
