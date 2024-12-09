import math
import re
from collections import defaultdict


def get_part_numbers(data: str) -> tuple[int, list[tuple[int, int]]]:
    pattern = re.compile(r"\d+")
    for y, row in enumerate(data.splitlines()):
        for match in pattern.finditer(row):
            part_number = int(row[match.start() : match.end()])
            adjacent = [
                *((y - 1, x) for x in range(match.start() - 1, match.end() + 1)),
                *((y + 1, x) for x in range(match.start() - 1, match.end() + 1)),
                (y, match.start() - 1),
                (y, match.end()),
            ]
            yield part_number, adjacent


def get_symbols(data: str) -> tuple[str, tuple[int, int]]:
    for y, row in enumerate(data.splitlines()):
        yield from ((c, (y, x)) for x, c in enumerate(row) if not c.isdigit() and c != ".")


def part_a(data: str) -> int:
    symbol_coords = set(coord for _, coord in get_symbols(data))
    result = 0
    for part_number, adjacent in get_part_numbers(data):
        if any(c in symbol_coords for c in adjacent):
            result += part_number
    return result


def part_b(data: str) -> int:
    star_symbols = set(coord for symbol, coord in get_symbols(data) if symbol == "*")
    adjacent_part_numbers = defaultdict(list)
    for part_number, adjacent in get_part_numbers(data):
        for coord in star_symbols & set(adjacent):
            adjacent_part_numbers[coord].append(part_number)
    return sum(math.prod(pns) for pns in adjacent_part_numbers.values() if len(pns) == 2)


if __name__ == "__main__":
    from aoc_cas.util import solve_with_example_input

    solve_with_example_input(year=2023, day=3)
