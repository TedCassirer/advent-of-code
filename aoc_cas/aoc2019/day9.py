from .IntCodeComputer import IntCodeComputerVM


def read_file(data):
    return [int(n) for n in data.split(",")]


def part_a(data):
    program = read_file(data)
    vm = IntCodeComputerVM(program, 1)
    list(vm.run())
    return vm.out


def part_b(data):
    program = read_file(data)
    vm = IntCodeComputerVM(program, 2)
    list(vm.run())
    return vm.out
