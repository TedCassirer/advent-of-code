def getRanges(data):
    r1, r2 = data.split(",")
    range1 = map(int, r1.split("-"))
    range2 = map(int, r2.split("-"))
    return tuple(range1), tuple(range2)


def overlaps(r1, r2):
    return (r2[0] <= r1[1] <= r2[1]) or (r1[0] <= r2[1] <= r1[1])


def contains(r1, r2):
    return (r1[0] <= r2[0] and r1[1] >= r2[1]) or (r1[0] >= r2[0] and r1[1] <= r2[1])


def part1(data):
    ranges = (getRanges(line) for line in data.splitlines())
    return sum(contains(range1, range2) for range1, range2 in ranges)


def part2(data):
    ranges = (getRanges(line) for line in data.splitlines())
    return sum(overlaps(range1, range2) for range1, range2 in ranges)


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2022, day=4)
    print(part1(data))
    print(part2(data))
