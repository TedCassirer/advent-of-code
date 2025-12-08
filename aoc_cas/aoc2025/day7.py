# https://adventofcode.com/2025/day/7
from functools import cache
from aoc_cas.common import Coordinate


def find_start(input: str) -> Coordinate:
    for y, line in enumerate(input.splitlines()):
        for x, char in enumerate(line):
            if char == "S":
                return Coordinate(y, x)

    raise ValueError("Start position 'S' not found in input")


def part_a(input: str) -> int:
    start = find_start(input)
    lines = input.splitlines()

    beams: list[int] = [start.x]
    splits = 0
    for y in range(start.y + 1, len(lines)):
        nxt_beams: list[int] = []
        for x in beams:
            if lines[y][x] == "^":
                splits += 1
                if not nxt_beams or nxt_beams[-1] != x - 1:
                    nxt_beams.append(x - 1)
                nxt_beams.append(x + 1)
            elif not nxt_beams or nxt_beams[-1] != x:
                nxt_beams.append(x)

        beams = nxt_beams

    return splits


def part_b(input: str) -> int:
    start = find_start(input)
    lines = input.splitlines()

    @cache
    def quantum_splits(beam: int, row: int) -> int:
        if row == len(lines):
            return 1
        if lines[row][beam] == "^":
            return quantum_splits(beam - 1, row + 1) + quantum_splits(beam + 1, row + 1)
        else:
            return quantum_splits(beam, row + 1)

    return quantum_splits(start.x, start.y + 1)


if __name__ == "__main__":
    from aoc_cas.util import solve_with_example_input

    solve_with_example_input(year=2025, day=7)
