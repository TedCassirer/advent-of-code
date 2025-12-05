# https://adventofcode.com/2025/day/5
from typing import NamedTuple

from aoc_cas.util import solve_with_example_input


Range = NamedTuple("Range", [("start", int), ("end", int)])


def parse_input(input: str) -> tuple[list[Range], list[int]]:
    ranges_str, ingredients_str = input.split("\n\n")
    ranges: list[Range] = []
    for line in ranges_str.splitlines():
        start, end = map(int, line.split("-"))
        ranges.append(Range(start, end))
    ranges.sort()

    merged_ranges: list[Range] = [ranges[0]]
    for r in ranges[1:]:
        last = merged_ranges[-1]
        if r.start <= last.end + 1:
            merged_ranges[-1] = Range(last.start, max(last.end, r.end))
        else:
            merged_ranges.append(r)
    ingredients = [int(ingredient) for ingredient in ingredients_str.splitlines()]
    return merged_ranges, ingredients


def contained_in_ranges(ranges: list[Range], n: int) -> bool:
    lo, hi = 0, len(ranges) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        r = ranges[mid]
        if r.start <= n <= r.end:
            return True
        elif n < r.start:
            hi = mid - 1
        else:
            lo = mid + 1
    return False


def part_a(input: str) -> int:
    ranges, ingredients = parse_input(input)

    spoiled = 0
    for ingredient in ingredients:
        if contained_in_ranges(ranges, ingredient):
            spoiled += 1
    return spoiled


def part_b(input: str) -> int:
    ranges, _ = parse_input(input)
    fresh_ids = 0
    for r in ranges:
        fresh_ids += r.end - r.start + 1
    return fresh_ids


if __name__ == "__main__":
    from aoc_cas.util import solve_with_real_input_data

    solve_with_real_input_data(year=2025, day=5)
    solve_with_example_input(year=2025, day=5)
