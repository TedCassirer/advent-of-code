def commonItem(*groups):
    return (set.intersection(*map(set, groups))).pop()


def priority(item):
    if item.islower():
        return ord(item) - ord("a") + 1
    else:
        return ord(item) - ord("A") + 27


def part1(data):
    commonItems = (commonItem(line[: len(line) // 2], line[len(line) // 2 :]) for line in data.splitlines())
    priorities = (priority(item) for item in commonItems)
    return sum(priorities)


def part2(data):
    lines = data.splitlines()
    _sum = 0
    for i in range(0, len(lines), 3):
        badge = commonItem(*lines[i : i + 3])
        _sum += priority(badge)
    return _sum


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2022, day=3)

    print(part1(data))
    print(part2(data))
