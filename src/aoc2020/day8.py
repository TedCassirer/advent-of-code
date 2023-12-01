SUCCESS = 0
ERROR = 1


def getProgram(data):
    program = []
    for line in data.splitlines():
        op, v = line.split(" ")
        program.append((op, int(v)))
    return program


def executeProgram(program):
    i, acc = 0, 0
    executed = [False] * len(program)
    while i != len(program) and not executed[i]:
        executed[i] = True
        op, val = program[i]
        if op == "jmp":
            i += val
        elif op == "acc":
            acc += val
            i += 1
        else:
            i += 1

    returnCode = SUCCESS if i == len(program) else ERROR
    return acc, returnCode


def part1(data):
    program = getProgram(data)
    acc, returnCode = executeProgram(program)
    assert returnCode == ERROR
    return acc


def part2(data):
    program = getProgram(data)

    def patchProgram(program):
        for i, operation in enumerate(program):
            if operation[0] == "nop":
                yield program[:i] + [("jmp", operation[1])] + program[i + 1 :]
            elif operation[0] == "jmp":
                yield program[:i] + [("nop", operation[1])] + program[i + 1 :]

    for prog in patchProgram(program):
        acc, returnCode = executeProgram(prog)
        if returnCode == SUCCESS:
            break

    assert returnCode == SUCCESS
    return acc
