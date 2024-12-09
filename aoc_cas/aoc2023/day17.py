import heapq
from collections import defaultdict
from functools import cache
from typing import Iterator

from aoc_cas.common import Coordinate, DIR_LEFT, DIR_UP, Direction


def a_star(graph: list[list[int]], start: Coordinate, min_moves: int, max_moves: int) -> int:
    M, N = len(graph), len(graph[0])
    goal = Coordinate.create(M - 1, N - 1)

    @cache
    def neighbours(coord: Coordinate, dir: Direction) -> Iterator[tuple[int, int, Coordinate]]:
        d_cost = 0
        for k in range(1, max_moves + 1):
            c = coord.move(dir, k)
            if 0 <= c.y < M and 0 <= c.x < N:
                d_cost += graph[c.y][c.x]
            else:
                break
            if k >= min_moves:
                est = c.md(goal) + cost + d_cost
                yield est, d_cost, c

    queue = [
        (start.md(goal), 0, start, DIR_LEFT),
        (start.md(goal), 0, start, DIR_UP),
    ]
    seen = defaultdict(set)
    while queue:
        _, cost, coord, dir = heapq.heappop(queue)
        if dir in seen[coord]:
            continue
        if coord == goal:
            return cost
        seen[coord].add(dir)

        left_dir = dir.turn_left()
        for est, d_cost, c in neighbours(coord, left_dir):
            heapq.heappush(queue, (est, cost + d_cost, c, left_dir))

        right_dir = dir.turn_right()
        for est, d_cost, c in neighbours(coord, right_dir):
            heapq.heappush(queue, (est, cost + d_cost, c, right_dir))
    raise ValueError("Unable to find a solution")


def parse_graph(data: str) -> list[list[int]]:
    graph = []
    for y, row in enumerate(data.splitlines()):
        graph.append([int(v) for v in row])
    return graph


def part_a(data: str) -> int:
    graph = parse_graph(data)
    return a_star(graph, Coordinate.create(0, 0), 1, 3)


def part_b(data: str) -> int:
    graph = parse_graph(data)
    return a_star(graph, Coordinate.create(0, 0), 4, 10)


if __name__ == "__main__":
    from aoc_cas.util import solve_with_example_input

    solve_with_example_input(year=2023, day=17)
