def part_a(data):
    lines = data.splitlines()
    ones = [sum(map(int, part)) for part in zip(*lines)]
    half = len(lines) // 2
    result = [count > half for count in ones]
    gamma = 0
    epsilon = 0
    for r in result:
        gamma <<= 1
        epsilon <<= 1
        gamma += r
        epsilon += r ^ 1

    return gamma * epsilon


def part_b(data):
    lines = data.splitlines()
    numbers = [int(n, 2) for n in lines]
    o2 = numbers
    co2 = numbers
    for k in range(len(lines[0]) - 1, -1, -1):
        mask = 1 << k

        if len(o2) > 1:
            keepBitO2 = sum(n & mask != 0 for n in o2) >= len(o2) / 2
            o2 = [n for n in o2 if bool(n & mask) == keepBitO2]

        if len(co2) > 1:
            keepBitCO2 = sum(n & mask != 0 for n in co2) < len(co2) / 2
            co2 = [n for n in co2 if bool(n & mask) == keepBitCO2]

    assert len(o2) == 1
    assert len(co2) == 1
    return o2[0] * co2[0]


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2021, day=3)

    print(part_a(data))
    print(part_b(data))
