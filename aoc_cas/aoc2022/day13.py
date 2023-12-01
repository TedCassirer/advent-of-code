from itertools import zip_longest
from functools import cmp_to_key


def compare(p1, p2):
    if p1 == None:
        return -1
    if p2 == None:
        return 1
    if isinstance(p1, int):
        if isinstance(p2, int):
            if p1 < p2:
                return -1
            if p1 == p2:
                return 0
            else:
                return 1
        else:
            return compare([p1], p2)
    else:
        if isinstance(p2, int):
            return compare(p1, [p2])
        else:
            for i1, i2 in zip_longest(p1, p2):
                if (compareRes := compare(i1, i2)) != 0:
                    return compareRes
            return 0


def parsePackets(packets):
    for packetPair in packets.split("\n\n"):
        p1, p2 = map(eval, packetPair.splitlines())
        yield p1, p2


def part_a(data):
    _sum = 0
    for i, (p1, p2) in enumerate(parsePackets(data)):
        if compare(p1, p2) <= 0:
            _sum += i + 1
    return _sum


def part_b(data):
    packets = [packet for packetPair in parsePackets(data) for packet in packetPair]
    dividerPacket1 = [[2]]
    dividerPacket2 = [[6]]
    packets.append(dividerPacket1)
    packets.append(dividerPacket2)

    packets.sort(key=cmp_to_key(compare))
    p1Index = packets.index(dividerPacket1) + 1
    p2Index = packets.index(dividerPacket2) + 1
    return p1Index * p2Index


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2022, day=13)

    print(part_a(data))
    print(part_b(data))
