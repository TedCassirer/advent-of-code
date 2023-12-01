def increment(start):
    current = list(start)
    while True:
        i = -1
        while current[i] == "z":
            current[i] = "a"
            i -= 1
        current[i] = chr(ord(current[i]) + 1)
        yield current


def increasing(current):
    current = [ord(c) for c in current]
    for c1, c2, c3 in zip(current, current[1:], current[2:]):
        if c3 == c2 + 1 and c3 == c1 + 2:
            return True
    return False


def twoPairs(string):
    pairs = {c1 for c1, c2 in zip(string, string[1:]) if c1 == c2}
    return len(pairs) >= 2


def banned(string):
    return "i" not in string and "o" not in string and "l" not in string


def part_a(data):
    for s in increment(data):
        if banned(s) and twoPairs(s) and increasing(s):
            return "".join(s)


def part_b(data):
    return part_a(part_a(data))


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2015, day=11)

    print(part_a(data))
    print(part_b(data))
