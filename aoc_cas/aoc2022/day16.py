import re
from collections import deque, defaultdict
from itertools import combinations
import heapq

REGEX = re.compile(r"Valve ([A-Z]{2}) has flow rate=(\d+); tunnels? leads? to valves? (.+)$")


def buildGraph(data):
    flowRates = dict()
    graph = dict()
    for line in data.splitlines():
        pipe, flowRate, connected = REGEX.search(line).groups()
        flowRate = int(flowRate)
        connections = connected.split(", ")
        if flowRate:
            flowRates[pipe] = flowRate
        graph[pipe] = connections

    costGraph = defaultdict(dict)

    for p1, p2 in combinations(flowRates.keys(), 2):
        steps = findPath(graph, p1, p2)
        costGraph[p1][p2] = steps
        costGraph[p2][p1] = steps

    for pipe in flowRates.keys():
        stepsFromStart = findPath(graph, "AA", pipe)
        costGraph["AA"][pipe] = stepsFromStart

    return costGraph, flowRates


def findPath(graph, start, goal):
    visited = set()
    toVisit = deque([(0, start)])
    while True:
        steps, cur = toVisit.popleft()
        if cur in visited:
            continue
        visited.add(cur)
        for nxt in graph[cur]:
            if nxt == goal:
                return steps + 1
            toVisit.append((steps + 1, nxt))


def estimate(flowRates, time, toVisit):
    return sum(flowRates[p] for p in toVisit) * time


def search(graph, flowRates, time, toVisit):
    seen = defaultdict(int)
    toSearch = [(-1, 0, time, "AA", toVisit)]
    maxPressureLost = 0
    while toSearch:
        e, pressureLost, time, cur, toVisit = heapq.heappop(toSearch)
        maxPressureLost = max(maxPressureLost, -pressureLost)
        key = (cur, toVisit)
        if seen[key] >= -e:
            continue
        seen[key] = -e
        for p2 in toVisit:
            steps = graph[cur][p2]
            if steps >= time:
                continue
            pl = flowRates[p2] * (time - steps - 1)
            tv = toVisit - {p2}
            est = estimate(flowRates, time - steps - 1, tv)
            heapq.heappush(toSearch, (pressureLost - pl - est, pressureLost - pl, time - steps - 1, p2, tv))
    return maxPressureLost


def part1(data):
    graph, flowRates = buildGraph(data)
    return search(graph, flowRates, 30, frozenset(flowRates.keys()))


def part2(data):

    graph, flowRates = buildGraph(data)
    maxFlowLost = 0
    for groupSize in range(len(flowRates) // 2 - 1, len(flowRates) // 2 + 1):
        for g1 in combinations(flowRates, groupSize):
            g1 = frozenset(g1)
            g2 = frozenset(flowRates.keys() - g1)
            pl1 = search(graph, flowRates, 26, g1)
            pl2 = search(graph, flowRates, 26, g2)
            maxFlowLost = max(maxFlowLost, pl1 + pl2)
    return maxFlowLost


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2022, day=16)

    print(part1(data))
    print(part2(data))
