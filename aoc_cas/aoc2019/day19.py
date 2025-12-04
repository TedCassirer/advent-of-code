from .IntCodeComputer import IntCodeComputerVM, generator_of


def read_file(data):
    return [int(n) for n in data.split(",")]


def scanCoord(y, x, program):
    tractorBeam = IntCodeComputerVM(program)
    tractorBeam.input_provided_from(generator_of(x, y))
    output = next(tractorBeam.run())
    if output is None:
        raise RuntimeError("Intcode program produced no output")
    return output


def part_a(data):
    X, Y = 50, 50
    program = read_file(data)
    return sum(scanCoord(y, x, program) for y in range(Y) for x in range(X))


def part_b(data):
    size = 100 - 1
    x, y = 0, 0

    program = read_file(data)

    topRight = scanCoord(y, x + size, program)
    bottomLeft = scanCoord(y + size, x, program)

    while not (topRight and bottomLeft):
        while not topRight:
            y += 1
            topRight = scanCoord(y, x + size, program)
        bottomLeft = scanCoord(y + size, x, program)
        while not bottomLeft:
            x += 1
            bottomLeft = scanCoord(y + size, x, program)
        topRight = scanCoord(y, x + size, program)
    assert scanCoord(y, x, program)
    assert scanCoord(y + size, x + size, program)

    return x * 10000 + y
