from functools import reduce


def getGroups(numbers, target):
    if target == 0:
        yield tuple()
    if not numbers:
        return
    for i, n in enumerate(numbers):
        if n <= target:
            for group in getGroups(numbers[i + 1 :], target - n):
                yield (n,) + group


def canCreateGroups(numbers, target, N):
    if N == 1:
        return sum(numbers) == target
    numbers = sorted(numbers, key=lambda n: -n)
    for group in getGroups(numbers, target):
        remainingNumbers = set(numbers) - set(group)
        if canCreateGroups(remainingNumbers, target, N - 1):
            return True
    return False


def getNumbers(data):
    return [int(n) for n in data.splitlines()]


def getPacks(numbers, N):
    target = sum(numbers) // N
    group1Length = 1 << 32
    group1s = sorted(getGroups(numbers, target), key=len)

    candidates = []
    shortest = 1 << 32

    for group in group1s:
        remainingNumbers = sorted(set(numbers) - set(group), key=lambda n: -n)
        if canCreateGroups(remainingNumbers, target, N - 1):
            if len(group) > shortest:
                break
            candidates.append(group)
            shortest = len(group)

    return candidates


def part1(data):
    numbers = getNumbers(data)
    numbers = sorted(numbers, key=lambda n: -n)
    group1s = getPacks(numbers, 3)

    return min(reduce(lambda a, b: a * b, group) for group in group1s)


def part2(data):
    numbers = getNumbers(data)
    numbers = sorted(numbers, key=lambda n: -n)
    group1s = getPacks(numbers, 4)

    return min(reduce(lambda a, b: a * b, group) for group in group1s)


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2015, day=24)

    print(part1(data))
    print(part2(data))
