from collections import defaultdict
import heapq


def createStart(data):
    lines = data.splitlines()
    transformations = defaultdict(list)
    for line in lines[:-2]:
        input, output = line.split(" => ")
        transformations[input].append(output)
    startState = lines[-1]
    return startState, dict(transformations)


def searchForSubstring(string, target):
    for i in range(len(string)):
        if string[i:].startswith(target):
            yield i


def transform(startState, transformations):
    for input, outputs in transformations.items():
        for i in searchForSubstring(startState, input):
            for output in outputs:
                yield startState[:i] + output + startState[i + len(input) :]


def part1(data):
    startState, transformations = createStart(data)
    return len(set(transform(startState, transformations)))


def part2(data):
    startState, transformations = createStart(data)
    targetState = "e"
    inverted = defaultdict(list)
    for k, v in transformations.items():
        for k1 in v:
            inverted[k1] = k
    transformations = dict(inverted)

    states = [(len(startState), 0, startState)]
    while states:
        _, steps, curr = heapq.heappop(states)
        if curr == targetState:
            return steps
        for k, v in transformations.items():
            i = curr.find(k)
            if i != -1:
                transformation = curr[:i] + v + curr[i + len(k) :]
                heapq.heappush(states, (len(transformation), steps + 1, transformation))


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2015, day=19)
    print(part1(data))
    print(part2(data))
