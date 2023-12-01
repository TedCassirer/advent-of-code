def part_a(data):
    return data.count("(") - data.count(")")


def part_b(data):
    floor = 0
    for i, c in enumerate(data):
        floor += 1 if c == "(" else -1
        if floor == -1:
            return i + 1


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2015, day=1)

    print(part_a(data))
    print(part_b(data))
