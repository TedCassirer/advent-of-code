def rotate(display, axis, index, amount):
    if axis == "row":
        display[index] = display[index][-amount:] + display[index][:-amount]
    else:
        column = [r[index] for r in display]
        column = column[-amount:] + column[:-amount]
        for r, colVal in zip(display, column):
            r[index] = colVal
    return display


def doThing(line, display):
    if line.startswith("rect"):
        _, dims = line.split(" ")
        cols, rows = map(int, dims.split("x"))
        for y in range(rows):
            for x in range(cols):
                display[y][x] = "#"
    else:
        M, N = len(display), len(display[0])
        _, axis, index, _, amount = line.split(" ")
        index = int(index.split("=")[-1])
        amount = int(amount)
        display = rotate(display, axis, index, amount)
    return display


def printDisplay(display):
    for r in display:
        print("".join(r))


def part1(data):
    display = [["."] * 50 for _ in range(6)]
    for line in data.splitlines():
        display = doThing(line, display)
    out = 0
    for r in display:
        out += sum(c == "#" for c in r)
    return out


def part2(data):
    display = [["."] * 50 for _ in range(6)]
    print()
    for line in data.splitlines():
        display = doThing(line, display)
    printDisplay(display)
    return "EFEYKFRFIJ"


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2016, day=8)
    print(part1(data))
    print(part2(data))
