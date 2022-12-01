def part1(data):
    carrying = [[int(g) for g in group.splitlines()] for group in data.split("\n\n")]
    return max(map(sum, carrying))


def part2(data):
    carrying = [[int(g) for g in group.splitlines()] for group in data.split("\n\n")]
    carrySorted = sorted(map(sum, carrying))
    return sum(carrySorted[-3:])


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2022, day=1)

    print(part1(data))
    print(part2(data))
