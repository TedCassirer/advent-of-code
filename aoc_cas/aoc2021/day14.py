from collections import Counter


def getRules(data):
    _, rulesString = data.split("\n\n")
    rules = dict()
    for line in rulesString.splitlines():
        k, v = line.split(" -> ")
        rules[k] = v
    return rules


def getPolymer(data):
    polymerString = data.splitlines()[0]
    polymer = Counter(c1 + c2 for c1, c2 in zip(polymerString, polymerString[1:]))
    charCount = Counter(polymerString)
    return polymer, charCount


def insertPairs(polymer, charCount, rules):
    polymerOut = Counter()
    for pair, count in polymer.items():
        c1, c3 = pair
        c2 = rules[pair]
        polymerOut[c1 + c2] += count
        polymerOut[c2 + c3] += count
        charCount[c2] += count

    return polymerOut, charCount


def part_a(data):
    polymer, charCount = getPolymer(data)
    rules = getRules(data)
    for _ in range(10):
        polymer, charCount = insertPairs(polymer, charCount, rules)
    return max(charCount.values()) - min(charCount.values())


def part_b(data):
    polymer, charCount = getPolymer(data)
    rules = getRules(data)
    for _ in range(40):
        polymer, charCount = insertPairs(polymer, charCount, rules)
    return max(charCount.values()) - min(charCount.values())


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2021, day=14)

    print(part_a(data))
    print(part_b(data))
