from .IntCodeComputer import IntCodeComputerVM


def read_file(data):
    return [int(n) for n in data.split(",")]


def part1(data):
    program = read_file(data)
    vm = IntCodeComputerVM(program, 1)
    list(vm.run())
    return vm.out


def part2(data):
    program = read_file(data)
    vm = IntCodeComputerVM(program, 2)
    list(vm.run())
    return vm.out
