from functools import lru_cache


@lru_cache(None)
def fill(containers, eggnog):
    if eggnog == 0:
        return [[]]
    if not containers or containers[-1] > eggnog:
        return []
    out = []
    for solution in fill(containers[:-1], eggnog):
        out.append(solution)
    for solution in fill(containers[:-1], eggnog - containers[-1]):
        out.append([containers[-1]] + solution)
    return out


def part1(data):
    containers = tuple(sorted([int(c) for c in data.splitlines()])[::-1])
    solutions = fill(containers, 150)
    return len(solutions)


def part2(data):
    containers = tuple(sorted([int(c) for c in data.splitlines()])[::-1])
    solutions = fill(containers, 150)
    minContainers = min(map(len, solutions))
    return sum(len(s) == minContainers for s in solutions)


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2015, day=17)
    print(part1(data))
    print(part2(data))
