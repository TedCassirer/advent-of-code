def part_a(data):
    for i in range(4, len(data)):
        if len(set(data[i - 4 : i])) == 4:
            return i
    raise ValueError(":(")


def part_b(data):
    for i in range(14, len(data)):
        if len(set(data[i - 14 : i])) == 14:
            return i
    raise ValueError(":(")


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2022, day=6)

    print(part_a(data))
    print(part_b(data))
