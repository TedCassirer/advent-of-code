import json


def nums(x, ignore_red=False):
    if type(x) is dict:
        if ignore_red and "red" in x.values():
            return
        for a in x:
            yield from nums(x[a], ignore_red)
    elif type(x) is list:
        for a in x:
            yield from nums(a, ignore_red)
    elif type(x) is int:
        yield x


def part1(data):
    return sum(nums(json.loads(data)))


def part2(data):
    return sum(nums(json.loads(data), True))


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2015, day=12)

    print(part1(data))
    print(part2(data))
