def part_a(data):
    resultScore = {
        "A": {"X": 1 + 3, "Y": 2 + 6, "Z": 3 + 0},
        "B": {"X": 1 + 0, "Y": 2 + 3, "Z": 3 + 6},
        "C": {"X": 1 + 6, "Y": 2 + 0, "Z": 3 + 3},
    }
    score = 0
    for line in data.splitlines():
        opponent, you = line.split(" ")
        score += resultScore[opponent][you]
    return score


def part_b(data):
    resultScore = {
        "X": {"A": 0 + 3, "B": 0 + 1, "C": 0 + 2},
        "Y": {"A": 1 + 3, "B": 2 + 3, "C": 3 + 3},
        "Z": {"A": 2 + 6, "B": 3 + 6, "C": 1 + 6},
    }
    score = 0
    for line in data.splitlines():
        opponent, wantedResult = line.split(" ")
        score += resultScore[wantedResult][opponent]
    return score


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2022, day=2)

    print(part_a(data))
    print(part_b(data))
