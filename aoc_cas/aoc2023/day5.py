import dataclasses
from typing import Self

from aocd import get_data


@dataclasses.dataclass(frozen=True)
class Map:
    source: int
    destination: int
    length: int

    def __lt__(self, other: Self) -> bool:
        return self.source < other.source

    @classmethod
    def from_line(cls, line: str) -> Self:
        destination, source, length = line.split(" ")
        return Map(destination=int(destination), source=int(source), length=int(length))


@dataclasses.dataclass(frozen=True)
class Transformation:
    name: str
    ranges: list[Map]

    @classmethod
    def from_transformation_data(cls, group: str) -> Self:
        name, *ranges_str = group.splitlines()
        ranges: list[Map] = sorted(map(Map.from_line, ranges_str))
        return Transformation(name=name, ranges=ranges)

    def map(self, input: int) -> int:
        if input < self.ranges[0].source:
            return input

        for range in self.ranges:
            if range.source > input:
                break
            if range.source + range.length > input:
                d = input - range.source
                if d <= range.length:
                    return range.destination + d
                else:
                    break
        return input


def parse(data: str) -> tuple[list[int], list[Transformation]]:
    seeds_str, *groups = data.split("\n\n")
    seeds = [int(s) for s in seeds_str.split(" ")[1:]]
    transformations = list(map(Transformation.from_transformation_data, groups))
    return seeds, transformations


def part_a(data: str) -> int:
    seeds, transformations = parse(data)

    lowest = 1 << 63
    for x in seeds:
        for transformation in transformations:
            x = transformation.map(x)
        lowest = min(x, lowest)
    return lowest


def part_b(data: str) -> int:
    seeds, transformations = parse(data)

    lowest = 1 << 63
    seeds_to_check = sum(seeds[1::2])
    print("Seeds to check:", seeds_to_check)

    checked = 0
    for a, b in zip(seeds[::2], seeds[1::2]):
        for x in range(a, a+b):
            checked += 1
            if checked % 1000000 == 0:
                print(checked, round(checked / seeds_to_check, 5))
            for transformation in transformations:
                x = transformation.map(x)
            lowest = min(x, lowest)
    return lowest


if __name__ == "__main__":
    from aoc_cas.util import solve_with_examples

    solve_with_examples(year=2023, day=5)
    data = get_data(year=2023, day=5)
    print(part_a(data))
    print(part_b(data))
