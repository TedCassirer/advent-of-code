def part_a(data):
    numbers = [int(n) for n in data.splitlines()]
    return sum(n2 > n1 for n1, n2 in zip(numbers, numbers[1:]))


def part_b(data):
    numbers = [int(n) for n in data.splitlines()]
    return sum(n2 > n1 for n1, n2 in zip(numbers, numbers[3:]))


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2021, day=1)

    print(part_a(data))
    print(part_b(data))
