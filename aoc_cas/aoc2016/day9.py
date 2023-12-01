import re


def decompressLength(string, recursive):
    expansion = re.search(r"\((\d+x\d+)\)", string)
    if expansion:
        start, end = expansion.span()
        a, b = map(int, string[start + 1 : end - 1].split("x"))
        p1 = string[:start]
        toRepeat = string[end : end + a]
        p3 = string[end + a :]
        if recursive:
            return len(p1) + decompressLength(toRepeat, recursive) * b + decompressLength(p3, recursive)
        else:
            return len(p1) + len(toRepeat) * b + decompressLength(p3, recursive)
    return len(string)


def part_a(data):
    return decompressLength(data, recursive=False)


def part_b(data):
    return decompressLength(data, recursive=True)


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2016, day=9)
    print(part_a(data))
    print(part_b(data))
