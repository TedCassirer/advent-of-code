from functools import lru_cache


def part1(data):
    adapters = sorted(map(int, data.splitlines()))
    adapters = [0] + adapters + [adapters[-1] + 3]
    diffs = [(n2 - n1) for n1, n2 in zip(adapters, adapters[1:])]
    oneDiffs, threeDiffs = diffs.count(1), diffs.count(3)
    return oneDiffs * threeDiffs


def part2(data):
    adapters = tuple(sorted(map(int, data.splitlines())))

    @lru_cache
    def inner(currJolt, startIndex):
        if len(adapters) == startIndex:
            return 1
        return sum(
            inner(adapters[i], i + 1)
            for i in range(startIndex, startIndex + 3)
            if i < len(adapters) and adapters[i] <= currJolt + 3
        )

    return inner(0, 0)
