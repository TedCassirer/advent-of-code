from collections import defaultdict

DIGIT_LENGTH = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}


def decode(signal, output):
    mapping = dict()
    byLength = defaultdict(set)
    for s in signal:
        byLength[len(s)].add(s)
    mapping[1] = byLength[DIGIT_LENGTH[1]].pop()
    mapping[4] = byLength[DIGIT_LENGTH[4]].pop()
    mapping[7] = byLength[DIGIT_LENGTH[7]].pop()
    mapping[8] = byLength[DIGIT_LENGTH[8]].pop()

    # 2
    for s in byLength[DIGIT_LENGTH[2]]:
        if len(set(mapping[4]) & set(s)) == 2:
            mapping[2] = s
            break
    byLength[DIGIT_LENGTH[2]].discard(mapping[2])

    # 3
    for s in byLength[DIGIT_LENGTH[3]]:
        if len(set(mapping[1]) & set(s)) == 2:
            mapping[3] = s
            break
    byLength[DIGIT_LENGTH[3]].discard(mapping[3])

    # 5
    mapping[5] = byLength[DIGIT_LENGTH[5]].pop()

    # 6
    for s in byLength[DIGIT_LENGTH[6]]:
        if len(set(mapping[1]) & set(s)) == 1:
            mapping[6] = s
            break
    byLength[DIGIT_LENGTH[6]].discard(mapping[6])

    # 9
    for s in byLength[DIGIT_LENGTH[9]]:
        if len(set(mapping[4]) & set(s)) == 4:
            mapping[9] = s
            break
    byLength[DIGIT_LENGTH[9]].discard(mapping[9])

    # 0
    mapping[0] = byLength[DIGIT_LENGTH[0]].pop()

    decoder = {frozenset(s): n for n, s in mapping.items()}

    out = 0
    for o in output:
        out = out * 10 + decoder[frozenset(o)]
    return out


def part_a(data):
    out = 0
    for line in data.splitlines():
        _, digits = line.split(" | ")
        for digit in digits.split(" "):
            out += len(digit) in {2, 4, 3, 7}
    return out


def part_b(data):
    out = 0
    for line in data.splitlines():
        signal, output = line.split(" | ")
        signal = signal.split(" ")
        output = output.split(" ")
        out += decode(signal, output)
    return out


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2021, day=8)

    print(part_a(data))
    print(part_b(data))
