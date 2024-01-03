def create_graph(data: str) -> tuple[tuple[int, int], list[list[int]]]:
    lines = data.splitlines()
    M, N = len(lines), len(lines[0])

    edges = [[1] * (2 * N + 1) for _ in range(2 * M + 1)]
    start = -1, -1
    for y, row in enumerate(lines):
        yy = y * 2 + 1
        for x, v in enumerate(row):
            xx = x * 2 + 1
            edges[yy - 1][xx - 1] = 0
            edges[yy - 1][xx + 1] = 0
            edges[yy + 1][xx - 1] = 0
            edges[yy + 1][xx + 1] = 0
            match v:
                case "|":
                    edges[yy - 1][xx] &= 1
                    edges[yy + 1][xx] &= 1
                    edges[yy][xx - 1] &= 0
                    edges[yy][xx + 1] &= 0
                case "-":
                    edges[yy - 1][xx] &= 0
                    edges[yy + 1][xx] &= 0
                    edges[yy][xx - 1] &= 1
                    edges[yy][xx + 1] &= 1
                case "L":
                    edges[yy - 1][xx] &= 1
                    edges[yy + 1][xx] &= 0
                    edges[yy][xx - 1] &= 0
                    edges[yy][xx + 1] &= 1
                case "J":
                    edges[yy - 1][xx] &= 1
                    edges[yy + 1][xx] &= 0
                    edges[yy][xx - 1] &= 1
                    edges[yy][xx + 1] &= 0
                case "7":
                    edges[yy - 1][xx] &= 0
                    edges[yy + 1][xx] &= 1
                    edges[yy][xx - 1] &= 1
                    edges[yy][xx + 1] &= 0
                case "F":
                    edges[yy - 1][xx] &= 0
                    edges[yy + 1][xx] &= 1
                    edges[yy][xx - 1] &= 0
                    edges[yy][xx + 1] &= 1
                case ".":
                    edges[yy][xx] = 0
                    edges[yy - 1][xx] &= 0
                    edges[yy + 1][xx] &= 0
                    edges[yy][xx - 1] &= 0
                    edges[yy][xx + 1] &= 0
                case "S":
                    edges[yy - 1][xx] &= 1
                    edges[yy + 1][xx] &= 1
                    edges[yy][xx - 1] &= 1
                    edges[yy][xx + 1] &= 1
                    start = yy, xx
                case _:
                    edges[yy][xx] = 0
                    edges[yy - 1][xx] &= 0
                    edges[yy + 1][xx] &= 0
                    edges[yy][xx - 1] &= 0
                    edges[yy][xx + 1] &= 0
    return start, edges


def trace_path(start: tuple[int, int], graph: list[list[int]]) -> list[tuple[int, int]]:
    current = start
    path = []
    prev = None
    while not (prev == start and len(path) > 2):
        y, x = current
        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            if graph[y + dy][x + dx] == 1 and graph[y + 2 * dy][x + 2 * dx] == 1 and (y + 2 * dy, x + 2 * dx) != prev:
                prev = current
                path.append((y + dy, x + dx))
                path.append((y + 2 * dy, x + 2 * dx))
                current = y + 2 * dy, x + 2 * dx
                break
    return path[:-1]


def part_a(data: str) -> int:
    start, graph = create_graph(data)
    path = trace_path(start, graph)
    return len(path) // 4


def part_b(data: str) -> int:
    start, graph = create_graph(data)
    path = trace_path(start, graph)
    M, N = len(graph), len(graph[0])
    current = {(0, 0)}  # Guaranteed to not be part of path
    seen = set(path)
    while current:
        nxt = set()
        for y, x in current - seen:
            seen.add((y, x))
            for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if 0 <= y + dy < M and 0 <= x + dx < N:
                    nxt.add((y + dy, x + dx))
        current = nxt

    all_nodes = {(y, x) for y in range(M) for x in range(N) if y % 2 == 1 and x % 2 == 1}
    return len(all_nodes - seen)


if __name__ == "__main__":
    from aoc_cas.util import solve_with_examples

    solve_with_examples(year=2023, day=10)
