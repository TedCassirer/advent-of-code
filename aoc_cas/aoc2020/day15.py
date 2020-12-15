from itertools import islice


def memoryGame(startingNumbers):
    seen = {}
    turn = 0
    for nextNumber in startingNumbers:
        yield nextNumber
        turn += 1
        seen[nextNumber] = turn
    previousNumber = nextNumber
    while True:
        nextNumber = turn - seen.get(previousNumber, turn)
        yield nextNumber
        seen[previousNumber] = turn
        previousNumber = nextNumber
        turn += 1


def part1(data):
    numbers = [int(n) for n in data.split(",")]
    muhNumbers = memoryGame(numbers)
    return next(islice(muhNumbers, 2019, None))


def part2(data):
    numbers = [int(n) for n in data.split(",")]
    muhNumbers = memoryGame(numbers)
    return next(islice(muhNumbers, 29999999, None))
