def part1(data):
    out = 0
    for line in data.splitlines():
        a, b, c = map(int, line.split("x"))
        sides = (a * b, a * c, b * c)
        out += sum(sides) * 2 + min(sides)
    return out


def part2(data):
    out = 0
    for line in data.splitlines():
        s1, s2, s3 = sorted([int(c) for c in line.split("x")])
        out += 2 * (s1 + s2) + s1 * s2 * s3
    return out


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2015, day=2)

    print(part1(data))
    print(part2(data))
