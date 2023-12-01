CLOSING = {"{": "}", "(": ")", "[": "]", "<": ">"}


def part1(data):
    SCORE = {")": 3, "]": 57, "}": 1197, ">": 25137}
    score = 0
    for line in data.splitlines():
        stack = []
        for c in line:
            if c not in CLOSING:
                if c != stack.pop():
                    score += SCORE[c]
            else:
                stack.append(CLOSING[c])
    return score


def part2(data):
    SCORE = {")": 1, "]": 2, "}": 3, ">": 4}
    scores = []
    for line in data.splitlines():
        stack = []
        for c in line:
            if c not in CLOSING:
                if c != stack.pop():
                    break
            else:
                stack.append(CLOSING[c])
        else:
            score = 0
            for s in reversed(stack):
                score *= 5
                score += SCORE[s]
            if score:
                scores.append(score)
    scores.sort()
    return scores[len(scores) // 2]


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2021, day=10)

    print(part1(data))
    print(part2(data))
