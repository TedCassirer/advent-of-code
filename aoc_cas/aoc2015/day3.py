def part_a(data):
    visited = {(0, 0)}
    x, y = 0, 0
    for c in data:
        if c == "v":
            y += 1
        elif c == "^":
            y -= 1
        elif c == ">":
            x += 1
        else:
            x -= 1
        visited.add((y, x))
    return len(visited)


def part_b(data):
    visited = {(0, 0)}
    x, y = 0, 0
    for c in data[::2]:
        if c == "v":
            y += 1
        elif c == "^":
            y -= 1
        elif c == ">":
            x += 1
        else:
            x -= 1
        visited.add((y, x))
    x, y = 0, 0
    for c in data[1::2]:
        if c == "v":
            y += 1
        elif c == "^":
            y -= 1
        elif c == ">":
            x += 1
        else:
            x -= 1
        visited.add((y, x))
    return len(visited)


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2015, day=3)

    print(part_a(data))
    print(part_b(data))
