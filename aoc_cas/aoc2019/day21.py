from aoc_cas.aoc2019.IntCodeComputer import IntCodeComputerVM, read_program


def instructions(*inputs):
    for i in inputs:
        yield from map(ord, i + "\n")


def gogoSpringyBoi(program, inputs):
    vm = IntCodeComputerVM(program)
    vm.input_provided_from(inputs)
    row = ""
    for r in vm.run():
        if r is None:
            continue
        if r > 0x110000:
            return r
        else:
            char = chr(r)
        row += char
        if char == "\n":
            print("".join(row))
            row = ""


def part_a(data):
    program = read_program(data)
    inputs = instructions(
        "OR A T",
        "AND B T",
        "AND C T",
        "NOT T J",
        "AND D J",
        "WALK",
    )
    return gogoSpringyBoi(program, inputs)


def part_b(data):
    program = read_program(data)
    inputs = instructions(
        # Only jump if there's a hole in the next 3 steps and D is ground
        "OR A T",
        "AND B T",
        "AND C T",
        "NOT T J",
        "AND D J",
        # Reset T to False
        "AND J T",
        # H | (E&I)
        "OR E T",
        "AND I T",
        "OR H T",
        "AND T J",
        "NOT A T",
        "OR T J",
        "RUN",
    )
    return gogoSpringyBoi(program, inputs)


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2019, day=21)
    print(part_a(data))
    print(part_b(data))
