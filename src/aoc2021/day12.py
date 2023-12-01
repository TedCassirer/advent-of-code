from collections import defaultdict


def getGraph(data):
    graph = defaultdict(list)
    for line in data.splitlines():
        n1, n2 = line.split("-")
        if n2 != "start":
            graph[n1].append(n2)
        if n1 != "start":
            graph[n2].append(n1)
    return graph


def findPaths(graph, allowExtraVisit):
    stack = [("start", frozenset(), allowExtraVisit)]
    paths = 0
    while stack:
        curr, visited, extraVisit = stack.pop()
        if curr.islower() and curr in visited:
            if extraVisit:
                extraVisit = False
            else:
                continue
        if curr == "end":
            paths += 1
            continue
        visited = visited | {curr}
        for connected in graph[curr]:
            stack.append((connected, visited, extraVisit))
    return paths


def part1(data):
    return findPaths(getGraph(data), False)


def part2(data):
    return findPaths(getGraph(data), True)


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2021, day=12)

    print(part1(data))
    print(part2(data))
