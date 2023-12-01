def decode(string):
    chars = (c for c in string[1:-1])
    out = ""
    for c1 in chars:
        if c1 != "\\":
            out += c1
        else:
            c2 = next(chars)
            if c2 == "x":
                c3, c4 = next(chars), next(chars)
                out += chr(int(c3 + c4, 16))
            else:
                out += c2
    return out


def escape(string):
    out = ""
    for c in string:
        if c in {"\\", '"'}:
            out += "\\"
        out += c
    return '"' + out + '"'


def part_a(data):
    out = 0
    for line in data.splitlines():
        cleanString = decode(line)
        out += len(line) - len(cleanString)
    return out


def part_b(data):
    out = 0
    for line in data.splitlines():
        escapedString = escape(line)
        out += len(escapedString) - len(line)
    return out


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2015, day=8)
    print(part_a(data))
    print(part_b(data))
