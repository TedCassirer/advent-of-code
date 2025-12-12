# https://adventofcode.com/2025/day/11

from collections import defaultdict


def build_graph(input: str) -> dict[str, list[str]]:
    graph: dict[str, list[str]] = defaultdict(list)
    for line in input.splitlines():
        node, neighbors_str = line.split(": ")
        graph[node].extend(neighbors_str.split(" "))
    return graph


def find_number_of_paths(graph: dict[str, list[str]], start: str, end: str) -> int:
    from functools import cache

    @cache
    def inner(curr: str) -> int:
        if curr == end:
            return 1
        return sum((inner(neighbor) for neighbor in graph[curr]), 0)

    return inner(start)


def part_a(input: str) -> int:
    graph = build_graph(input)
    return find_number_of_paths(graph, "you", "out")


def part_b(input: str) -> int:
    graph = build_graph(input)
    svr_dac = find_number_of_paths(graph, "svr", "dac")
    dac_fft = find_number_of_paths(graph, "dac", "fft")
    fft_out = find_number_of_paths(graph, "fft", "out")

    svr_fft = find_number_of_paths(graph, "svr", "fft")
    fft_dac = find_number_of_paths(graph, "fft", "dac")
    dac_out = find_number_of_paths(graph, "dac", "out")

    dac_first = svr_dac * dac_fft * fft_out
    fft_first = svr_fft * fft_dac * dac_out
    total_paths = dac_first + fft_first

    return total_paths


if __name__ == "__main__":
    inp = """
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
""".strip()
    part_b(inp)
