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
    def inner(currJolt, adapters):
        if not adapters:
            return 1
        return sum(inner(j, adapters[i + 1 :]) for i, j in enumerate(adapters) if j <= currJolt + 3)

    return inner(0, adapters)
