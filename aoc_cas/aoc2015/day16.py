actualString = """
    children: 3
    cats: 7
    samoyeds: 2
    pomeranians: 3
    akitas: 0
    vizslas: 0
    goldfish: 5
    trees: 3
    cars: 2
    perfumes: 1
""".strip()


def parse(line):
    line = line.replace(",", "").replace(":", "")
    words = line.split(" ")
    nr = int(words[1])
    words = words[2:]
    items = {k: int(v) for k, v in zip(words[::2], words[1::2])}
    return (nr, items)


def part1(data):
    actual = dict()
    for line in actualString.splitlines():
        k, v = line.strip().split(": ")
        actual[k] = int(v)
    for nr, items in map(parse, data.splitlines()):
        if all(actual[k] == v for k, v in items.items()):
            return nr


def part2(data):
    actual = dict()
    for line in actualString.splitlines():
        k, v = line.strip().split(": ")
        v = int(v)
        if k in {"cats", "trees"}:
            actual[k] = v.__lt__
        elif k in {"pomeranians", "goldfish"}:
            actual[k] = v.__gt__
        else:
            actual[k] = v.__eq__
    for nr, items in map(parse, data.splitlines()):
        if all(actual[k](v) for k, v in items.items()):
            return nr


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2015, day=16)
    print(part1(data))
    print(part2(data))
