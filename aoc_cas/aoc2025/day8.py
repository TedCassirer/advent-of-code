# https://adventofcode.com/2025/day/8
from typing import NamedTuple

Coordinate = NamedTuple("Coordinate", [("x", int), ("y", int), ("z", int)])


def distance_squared(a: Coordinate, b: Coordinate) -> int:
    return (a.x - b.x) ** 2 + (a.y - b.y) ** 2 + (a.z - b.z) ** 2


def get_junctions(input: str) -> list[Coordinate]:
    junctions: list[Coordinate] = []
    for line in input.splitlines():
        x_str, y_str, z_str = line.split(",")
        junctions.append(Coordinate(int(x_str), int(y_str), int(z_str)))
    return junctions


def get_circuits(connections: list[set[int]]) -> list[set[int]]:
    visited = set()
    circuits: list[set[int]] = []

    for start in range(len(connections)):
        if start in visited:
            continue

        circuit = set()
        stack = [start]

        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            circuit.add(node)
            for neighbor in connections[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

        circuits.append(circuit)

    return circuits


# Change k to 1000 for real input
def part_a(input: str, k: int = 10) -> int:
    junctions = get_junctions(input)
    N = len(junctions)
    junction_pairs = [(i, j) for i in range(N) for j in range(i + 1, N)]
    junction_pairs.sort(key=lambda pair: distance_squared(junctions[pair[0]], junctions[pair[1]]))

    connections: list[set[int]] = [set() for _ in range(N)]
    for a, b in junction_pairs[:k]:
        connections[a].add(b)
        connections[b].add(a)

    circuits = get_circuits(connections)
    circuit_sizes = sorted(len(circuit) for circuit in circuits)

    return circuit_sizes[-1] * circuit_sizes[-2] * circuit_sizes[-3]


def part_b(input: str) -> int:
    junctions = get_junctions(input)
    N = len(junctions)
    junction_pairs = [(i, j) for i in range(N) for j in range(i + 1, N)]
    junction_pairs.sort(key=lambda pair: distance_squared(junctions[pair[0]], junctions[pair[1]]))
    connections: list[set[int]] = [{i} for i in range(N)]
    for a, b in junction_pairs:
        if b not in connections[a]:
            # Join circuits
            connections[a].update(connections[b])
            for node in connections[b]:
                connections[node] = connections[a]

            if len(connections[a]) == N:
                return junctions[a].x * junctions[b].x

    raise ValueError("All junctions are not connected")


if __name__ == "__main__":
    from aoc_cas.util import solve_with_example_input

    solve_with_example_input(year=2025, day=8)
