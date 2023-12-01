from collections import defaultdict
import heapq


def buildGraph(data):
    graph = defaultdict(list)
    for line in data.splitlines():
        city1, _, city2, _, dist = line.split(" ")
        dist = int(dist)
        graph[city1].append((city2, dist))
        graph[city2].append((city1, dist))
    return graph


def search(start, graph, longest=False):
    queue = [(0, start, {start})]
    sign = -1 if longest else 1
    while queue:
        currDist, current, visited = heapq.heappop(queue)
        currDist *= sign
        if len(visited) == len(graph):
            return currDist
        for nextCity, dist in graph[current]:
            if nextCity not in visited:
                heapq.heappush(queue, (sign * (currDist + dist), nextCity, visited | {nextCity}))


def part_a(data):
    graph = buildGraph(data)
    return min(search(start, graph) for start in graph.keys())


def part_b(data):
    graph = buildGraph(data)
    return max(search(start, graph, longest=True) for start in graph.keys())


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2015, day=9)
    print(part_a(data))
    print(part_b(data))
