from itertools import islice


def memoryGame(startingNumbers, n):
    seen = [0] * n
    for turn, nextNumber in enumerate(startingNumbers):
        seen[nextNumber] = turn + 1
    previousNumber = nextNumber
    for turn in range(turn + 1, n):
        nextNumber = turn - (seen[previousNumber] or turn)
        seen[previousNumber] = turn
        previousNumber = nextNumber
    return nextNumber


def part1(data):
    numbers = [int(n) for n in data.split(",")]
    return memoryGame(numbers, 2020)


def part2(data):
    numbers = [int(n) for n in data.split(",")]
    return memoryGame(numbers, 30000000)
