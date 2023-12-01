def getPassWord(numpad, data, startCol, startRow):
    c, r = startCol, startRow
    pw = ""
    for line in data.splitlines():
        for i in line:
            if i == "R" and numpad[r][c + 1] != ".":
                c += 1
            elif i == "L" and numpad[r][c - 1] != ".":
                c -= 1
            elif i == "D" and numpad[r + 1][c] != ".":
                r += 1
            elif i == "U" and numpad[r - 1][c] != ".":
                r -= 1
        pw += numpad[r][c]
    return pw


def part_a(data):
    numpad = """
.....
.123.
.456.
.789.
.....
""".strip().splitlines()
    startCol, startRow = 2, 2
    return getPassWord(numpad, data, startCol, startRow)


def part_b(data):
    numpad = """
.......
...1...
..234..
.56789.
..ABC..
...D...
.......
""".strip().splitlines()
    startCol, startRow = 1, 3
    return getPassWord(numpad, data, startCol, startRow)


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2016, day=2)

    print(part_a(data))
    print(part_b(data))
