from .IntCodeComputer import IntCodeComputerVM


def part1(data):
    program = [int(i) for i in data.split(",")]
    vm = IntCodeComputerVM(program, 1)
    return list(vm.run())[-1]


def part2(data):
    program = [int(i) for i in data.split(",")]
    vm = IntCodeComputerVM(program, 5)
    return list(vm.run())[-1]
