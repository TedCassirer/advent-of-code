def part_a(data):
    directions = (line.split(" ") for line in data.splitlines())
    depth, distance = 0, 0
    for direction, amount in directions:
        amount = int(amount)
        if direction == "up":
            depth -= amount
        elif direction == "down":
            depth += amount
        elif direction == "forward":
            distance += amount
        else:
            raise Exception("What the?")

    return depth * distance


def part_b(data):
    directions = (line.split(" ") for line in data.splitlines())
    aim, depth, distance = 0, 0, 0
    depth = 0
    distance = 0
    for direction, amount in directions:
        amount = int(amount)
        if direction == "up":
            aim -= amount
        elif direction == "down":
            aim += amount
        elif direction == "forward":
            distance += amount
            depth += aim * amount
        else:
            raise Exception("What the?")

    return depth * distance


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2021, day=2)

    print(part_a(data))
    print(part_b(data))
