import re


def isAbba(string):
    for i in range(len(string) - 3):
        p1 = string[i : i + 2]
        p2 = string[i + 2 : i + 4]
        if p1 == p2[::-1] and p1 != p2:
            return True
    return False


def getAbas(string):
    for c1, c2, c3 in zip(string, string[1:], string[2:]):
        if c1 == c3 and c1 != c2:
            yield c1 + c2 + c3


def getParts(line):
    outside = re.findall(r"\](\w+)\[", "]" + line + "[")
    inside = re.findall(r"\[(\w+)\]", line)
    return outside, inside


def part_a(data):
    tlsCount = 0
    for line in data.splitlines():
        outside, inside = getParts(line)
        if any(isAbba(p) for p in outside) and all(not isAbba(p) for p in inside):
            tlsCount += 1
    return tlsCount


def part_b(data):
    sslCount = 0
    for line in data.splitlines():
        outside, inside = getParts(line)
        abasInside = set(aba for abas in map(getAbas, inside) for aba in abas)
        abasOutside = set(aba for abas in map(getAbas, outside) for aba in abas)
        babsOutside = set(aba[1] + aba[0] + aba[1] for aba in abasOutside)
        if abasInside & babsOutside:
            sslCount += 1
    return sslCount


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2016, day=7)
    print(part_a(data))
    print(part_b(data))
