from collections import Counter


def mostCommonChar(string):
    count = Counter(string)
    return max(count.items(), key=lambda kv: kv[1])[0]


def leastCommonChar(string):
    count = Counter(string)
    return min(count.items(), key=lambda kv: kv[1])[0]


def byColumn(rows):
    yield from ("".join(column) for column in zip(*rows))


def part1(data):
    columns = byColumn(data.splitlines())
    return "".join(map(mostCommonChar, columns))


def part2(data):
    columns = byColumn(data.splitlines())
    return "".join(map(leastCommonChar, columns))


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2016, day=6)
    print(part1(data))
    print(part2(data))
