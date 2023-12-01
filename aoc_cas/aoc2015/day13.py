import itertools
from collections import defaultdict


def parse(line):
    words = line.split(" ")
    p1, happiness, p2 = words[0], int(words[3]), words[-1][:-1]
    if words[2] == "lose":
        happiness *= -1
    return (p1, happiness, p2)


def getScoring(data):
    scoring = defaultdict(lambda: defaultdict(int))
    for p1, happiness, p2 in map(parse, data.splitlines()):
        scoring[p1][p2] = happiness
    return scoring


def score(arangement, scoring):
    score = 0
    for i, n in enumerate(arangement):
        score += scoring[n][arangement[i - 1]]
        score += scoring[n][arangement[(i + 1) % len(arangement)]]
    return score


def part_a(data):
    scoring = getScoring(data)
    people = scoring.keys()
    return max(score(arrangement, scoring) for arrangement in itertools.permutations(people))


def part_b(data):
    scoring = getScoring(data)
    people = list(scoring.keys())
    people.append("ME!!!")
    return max(score(arrangement, scoring) for arrangement in itertools.permutations(people))


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2015, day=13)
    print(part_a(data))
    print(part_b(data))
