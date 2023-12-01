import numpy as np
from itertools import cycle, islice


def phasePattern(phase, length):
    pattern = [0] * phase + [1] * phase + [0] * phase + [-1] * phase
    pattern = cycle(pattern)
    return list(islice(pattern, 1, length + 1))


def fftMatrix(N):
    matrix = np.array([phasePattern(n, N) for n in range(1, N + 1)])
    return matrix


def fft(numbers, times):
    matrix = fftMatrix(len(numbers))
    for _ in range(times):
        numbers = abs(np.matmul(matrix, numbers)) % 10
    return numbers


def fftOffset(numbers, offset, times):
    assert 2 * offset >= len(numbers)
    numbers = numbers[offset:]
    for _ in range(times):
        for i in range(len(numbers) - 2, -1, -1):
            numbers[i] += numbers[i + 1]
    return [n % 10 for n in numbers]


def part1(data):
    numbers = np.array([int(c) for c in data.strip()])
    numbers = fft(numbers, 100)
    return "".join(map(str, numbers[:8]))


def part2(data):
    numbers = [int(c) for c in data.strip()] * 10000
    offset = int(data[:7])
    numbers = fftOffset(numbers, offset, 100)
    return "".join(map(str, numbers[:8]))
