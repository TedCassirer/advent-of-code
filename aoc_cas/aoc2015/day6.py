import re

regex = re.compile(r"(.+) (\d{1,3},\d{1,3}) through (\d{1,3},\d{1,3})")


def parseLine(line):
    match = regex.match(line)
    if not match:
        raise ValueError(f"Could not parse instruction: {line}")
    action, start, end = match.groups()
    y1, x1 = map(int, start.split(","))
    y2, x2 = map(int, end.split(","))
    lights = ((y, x) for y in range(y1, y2 + 1) for x in range(x1, x2 + 1))
    return action, lights


def part_a(data):
    lights = [[0] * 1000 for _ in range(1000)]
    for action, affectedLights in map(parseLine, data.splitlines()):
        if action == "turn on":
            op = lambda _: 1
        elif action == "turn off":
            op = lambda _: 0
        else:
            op = lambda n: n ^ 1

        for y, x in affectedLights:
            lights[y][x] = op(lights[y][x])
    return sum((sum(row) for row in lights))


def part_b(data):
    lights = [[0] * 1000 for _ in range(1000)]
    for action, affectedLights in map(parseLine, data.splitlines()):
        if action == "turn on":
            op = lambda n: n + 1
        elif action == "turn off":
            op = lambda n: max(0, n - 1)
        else:
            op = lambda n: n + 2

        for y, x in affectedLights:
            lights[y][x] = op(lights[y][x])
    return sum((sum(row) for row in lights))


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2015, day=6)
    print(part_a(data))
    print(part_b(data))
