import re
from functools import cache
from typing import Iterator


def resolve(line: str, groups: list[int]) -> int:
    @cache
    def inner(i0: int, i1: int) -> int:
        if i1 == len(groups):
            return 1 if "#" not in line[i0:] else 0
        if i0 >= len(line):
            return 0
        pattern = re.compile(rf"[#?]{{{groups[i1]}}}([.?]|$)")
        if pattern.match(line, pos=i0):
            result = inner(i0 + groups[i1] + 1, i1 + 1)
        else:
            result = 0
        if line[i0] != "#":
            result += inner(i0 + 1, i1)
        return result

    return inner(0, 0)


def unfold(line: str, groups: list[int]) -> tuple[str, list[int]]:
    return "?".join([line] * 5), groups * 5


def parse(data: str) -> Iterator[tuple[str, list[int]]]:
    for line in data.splitlines():
        springs, nums_str = line.split(" ")
        nums = [int(c) for c in nums_str.split(",")]
        yield springs, nums


def part_a(data: str) -> int:
    return sum(resolve(springs, nums) for springs, nums in parse(data))


def part_b(data: str) -> int:
    return sum(resolve(*unfold(*d)) for d in parse(data))


if __name__ == "__main__":
    from aoc_cas.util import solve_with_examples

    solve_with_examples(year=2023, day=12)
