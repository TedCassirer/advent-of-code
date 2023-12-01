from .IntCodeComputer import IntCodeComputerVM


def part_a(data):
    program = [int(i) for i in data.split(",")]
    vm = IntCodeComputerVM(program, 1)
    return list(vm.run())[-1]


def part_b(data):
    program = [int(i) for i in data.split(",")]
    vm = IntCodeComputerVM(program, 5)
    return list(vm.run())[-1]
