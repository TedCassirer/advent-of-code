from collections import namedtuple
import math

Packet = namedtuple("Packet", ("version", "typeId", "value"))
LITERAL_VALUE = 4


def toBinary(hexadecimal):
    out = bin(int(hexadecimal, 16))[2:]
    return "0" * (-len(out) % 4) + out


def parse(binary):
    i = 0
    version = int(binary[i : i + 3], 2)
    typeId = int(binary[i + 3 : i + 6], 2)
    i += 6
    if typeId == LITERAL_VALUE:
        header = int(binary[i])
        valueBinary = binary[i + 1 : i + 5]
        i += 5
        while header == 1:
            header = int(binary[i])
            valueBinary += binary[i + 1 : i + 5]
            i += 5
        value = [int(valueBinary, 2)]
    else:
        lengthTypeId = int(binary[i], 2)
        i += 1
        if lengthTypeId == 0:
            subPacketLength = int(binary[i : i + 15], 2)
            i += 15
            value = []
            parsedBits = 0
            while parsedBits < subPacketLength and i < len(binary):
                packets, di = parse(binary[i + parsedBits : i + subPacketLength])
                value.append(packets)
                parsedBits += di
            i += subPacketLength

        if lengthTypeId == 1:
            subPacketCount = int(binary[i : i + 11], 2)
            i += 11
            value = []
            for k in range(subPacketCount):
                packets, di = parse(binary[i:])
                value.append(packets)
                i += di

    return Packet(version, typeId, value), i


def getPacketVersions(packet):
    yield packet.version
    if packet.typeId != LITERAL_VALUE:
        for p in packet.value:
            yield from getPacketVersions(p)


def sumOp(*values):
    return sum(evaluate(v) for v in values)


def product(*values):
    return math.prod(map(evaluate, values))


def minimum(*values):
    return min(map(evaluate, values))


def maximum(*values):
    return max(map(evaluate, values))


def literalValue(value):
    return value


def gt(v1, v2):
    return evaluate(v1) > evaluate(v2)


def lt(v1, v2):
    return evaluate(v1) < evaluate(v2)


def eq(v1, v2):
    return evaluate(v1) == evaluate(v2)


OPERATORS = {
    0: sumOp,
    1: product,
    2: minimum,
    3: maximum,
    4: literalValue,
    5: gt,
    6: lt,
    7: eq,
}


def evaluate(packet):
    return OPERATORS[packet.typeId](*packet.value)


def part_a(data):
    packet, _ = parse(toBinary(data))
    return sum(getPacketVersions(packet))


def part_b(data):
    packet, _ = parse(toBinary(data))
    return evaluate(packet)


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2021, day=16)

    print(part_a(data))
    print(part_b(data))
