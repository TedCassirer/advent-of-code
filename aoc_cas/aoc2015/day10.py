def countGame(number):
    streak = 1
    out = ""
    for n1, n2 in zip(number, number[1:]):
        if n1 == n2:
            streak += 1
        else:
            out += f"{streak}{n1}"
            streak = 1
    return f"{out}{streak}{n2}"


def part_a(data):
    number = data
    for _ in range(40):
        number = countGame(number)
    return len(number)


def part_b(data):
    number = data
    for _ in range(50):
        number = countGame(number)
    return len(number)


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2015, day=10)
    print(part_a(data))
    print(part_b(data))
