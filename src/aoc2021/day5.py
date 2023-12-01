from collections import Counter


def getLines(data, includeDiagonals=False):
    out = []
    for line in data.splitlines():
        p1, p2 = line.split(" -> ")
        n1, n2 = map(int, p1.split(","))
        n3, n4 = map(int, p2.split(","))
        group = set()
        if n1 == n3:
            n2, n4 = sorted([n2, n4])
            for n in range(n2, n4 + 1):
                group.add((n1, n))
        elif n2 == n4:
            n1, n3 = sorted([n1, n3])
            for n in range(n1, n3 + 1):
                group.add((n, n2))
        elif includeDiagonals:
            d1 = 1 if n1 < n3 else -1
            d2 = 1 if n2 < n4 else -1
            while (n3, n4) not in group:
                group.add((n1, n2))
                n1 += d1
                n2 += d2
        out.append(group)
    return out


def part1(data):
    lines = getLines(data)
    pointCount = Counter()
    for points in lines:
        pointCount.update(Counter(points))
    return sum(c >= 2 for p, c in pointCount.items())


def part2(data):
    lines = getLines(data, includeDiagonals=True)
    pointCount = Counter()
    for points in lines:
        pointCount.update(Counter(points))
    return sum(c >= 2 for p, c in pointCount.items())


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2021, day=5)

    print(part1(data))
    print(part2(data))
