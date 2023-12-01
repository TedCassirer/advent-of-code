from .IntCodeComputer import IntCodeComputerVM, generator_of
from itertools import permutations


def read_file(data):
    return [int(n) for n in data.split(",")]


def part_a(data):
    program = read_file(data)
    phase_setting_sequences = permutations((0, 1, 2, 3, 4))
    highest_output = 0
    for phase_settings in phase_setting_sequences:
        vms = [IntCodeComputerVM(program) for _ in range(len(phase_settings))]
        for phase, vm in zip(phase_settings, vms):
            vm.input_provided_from(iter([phase]))
        prev_signal = 0
        for vm in vms:
            vm.input_provided_from(iter([prev_signal]))
            prev_signal = next(vm.run())
        highest_output = max(highest_output, prev_signal)

    return highest_output


def part_b(data):
    program = read_file(data)
    phase_setting_sequences = permutations((5, 6, 7, 8, 9))
    highest_output = 0
    for phase_settings in phase_setting_sequences:
        vms = [IntCodeComputerVM(program) for _ in range(len(phase_settings))]
        for phase, vm in zip(phase_settings, vms):
            vm.input_provided_from(iter([phase]))
        prev_signal = 0
        iters = [vm.run() for vm in vms]
        while True:
            try:
                for vm, runner in zip(vms, iters):
                    vm.input_provided_from([prev_signal])
                    prev_signal = next(runner)
            except StopIteration:
                break
        output = prev_signal
        highest_output = max(highest_output, output)
    return highest_output
