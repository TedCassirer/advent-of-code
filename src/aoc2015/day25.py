def getValue(column, row):
    val = 20151125
    c, r = 1, 1
    loops = 0
    while c < column:
        loops += c + r
        c += 1
    while r < row:
        loops += c + r - 1
        r += 1
    for _ in range(loops):
        val = (val * 252533) % 33554393
    return val


def part1(data):
    left, right = data.split(", column")
    row = int(left.split(" ")[-1])
    col = int(right[:-1])
    val = getValue(col, row)
    return val


def part2(data):
    pass


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2015, day=25)

    print(part1(data))
    print(part2(data))
