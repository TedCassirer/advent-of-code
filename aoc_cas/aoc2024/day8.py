import math
from collections import defaultdict

from aoc_cas.common import Grid, Coordinate, Vector


def _parse_grid(data: str) -> Grid[str]:
    return Grid([list(line) for line in data.splitlines()])


def _get_antennas(grid: Grid[str]) -> dict[str, list[Coordinate]]:
    antennas: dict[str, list[Coordinate]] = defaultdict(list)
    for coord, val in grid.items():
        if val != ".":
            antennas[val].append(coord)
    return antennas


def part_a(data: str) -> int:
    grid = _parse_grid(data)
    antennas = _get_antennas(grid)
    antinodes: set[Coordinate] = set()

    for antenna_group in antennas.values():
        for ant1 in antenna_group:
            for ant2 in antenna_group:
                if ant1 != ant2:
                    v = ant2 - ant1
                    antinode = ant2 + v
                    antinodes.add(antinode)

    return len([a for a in antinodes if grid.in_bounds(a)])


def part_b(data: str) -> int:
    grid = _parse_grid(data)
    antennas = _get_antennas(grid)
    antinodes: set[Coordinate] = set()

    for antenna_group in antennas.values():
        for ant1 in antenna_group:
            for ant2 in antenna_group:
                if ant1 != ant2:
                    v12 = ant2 - ant1
                    gcd = math.gcd(v12.y, v12.x)
                    v = Vector(v12.y // gcd, v12.x // gcd)
                    antinode = ant1
                    while grid.in_bounds(antinode):
                        antinodes.add(antinode)
                        antinode += v
    return len(antinodes)


if __name__ == "__main__":
    from aoc_cas.util import solve_with_example_input

    solve_with_example_input(year=2024, day=8)
