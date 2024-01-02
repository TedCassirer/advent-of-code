import dataclasses
from functools import reduce
from typing import Self

from aocd import get_data


@dataclasses.dataclass(frozen=True)
class Range:
    source: int
    destination: int
    length: int

    def __lt__(self, other: Self) -> bool:
        return self.source < other.source

    @classmethod
    def from_line(cls, line: str) -> Self:
        destination, source, length = line.split(" ")
        return Range(destination=int(destination), source=int(source), length=int(length))

    def overlaps(self, other: Self) -> bool:
        if other.source <= self.destination < other.source + other.length:
            return True
        if other.source <= self.destination + self.length < other.source + other.length:
            return True
        return False

    def cut(self, length: int) -> tuple[Self, Self]:
        assert length < self.length
        left = Range(source=self.source, destination=self.destination, length=length)
        right = Range(
            source=self.source + length,
            destination=self.destination + length,
            length=self.length - length,
        )
        return left, right


@dataclasses.dataclass(frozen=True)
class RangeSet:
    ranges: list[Range]

    @classmethod
    def from_data(cls, group: str) -> Self:
        _, *ranges_str = group.splitlines()
        ranges: list[Range] = sorted(map(Range.from_line, ranges_str))
        return RangeSet(ranges=ranges)

    def add(self, other: Self) -> Self:
        ranges = sorted(self.ranges, key=lambda r: r.destination)
        out: set[Range] = set()
        i1 = 0
        r1 = ranges[i1]
        for r2 in other.ranges:
            while r1.destination + r1.length <= r2.source:
                out.add(r1)
                i1 += 1
                if i1 == len(ranges):
                    return RangeSet(ranges=sorted(out))
                r1 = ranges[i1]

            while r1.overlaps(r2):
                if r1.destination < r2.source:
                    # .|----
                    # ..|---
                    r1_offset = r2.source - r1.destination
                    head = Range(
                        source=r1.source,
                        destination=r1.destination,
                        length=r1_offset,
                    )
                    out.add(head)
                    r1 = Range(
                        source=r1.source + r1_offset,
                        destination=r1.destination + r1_offset,
                        length=r1.length - r1_offset,
                    )
                else:
                    # ..|---
                    # .|----
                    r2_offset = r1.destination - r2.source
                    r2 = Range(
                        source=r2.source + r2_offset,
                        destination=r2.destination + r2_offset,
                        length=r2.length - r2_offset,
                    )

                if r1.destination + r1.length <= r2.source + r2.length:
                    # .|---|...
                    # .|----|.
                    overlap = Range(source=r1.source, destination=r2.destination, length=r1.length)
                    out.add(overlap)
                    i1 += 1
                    if i1 == len(ranges):
                        return RangeSet(ranges=sorted(out))
                    r1 = ranges[i1]
                else:
                    # .|----|.
                    # .|---|...
                    overlap = Range(source=r1.source, destination=r2.destination, length=r2.length)
                    r1 = Range(
                        source=r1.source + overlap.length,
                        destination=r1.destination + overlap.length,
                        length=r1.length - overlap.length,
                    )
                    out.add(overlap)
        out.add(r1)
        out.update(ranges[i1 + 1 :])
        return RangeSet(ranges=sorted(out))


def parse(data: str) -> tuple[list[int], list[RangeSet]]:
    seeds_str, *groups = data.split("\n\n")
    seeds = [int(s) for s in seeds_str.split(" ")[1:]]
    range_sets = list(map(RangeSet.from_data, groups))
    return seeds, range_sets


def part_a(data: str) -> int:
    seeds, range_sets = parse(data)
    ranges = [Range(source=s, destination=s, length=1) for s in seeds]
    initial_rs = RangeSet(ranges=ranges)
    full_transformation = reduce(RangeSet.add, range_sets, initial_rs)
    return min(r.destination for r in full_transformation.ranges)


def part_b(data: str) -> int:
    seeds, range_sets = parse(data)
    ranges = []
    for a, b in zip(seeds[::2], seeds[1::2]):
        ranges.append(Range(source=a, destination=a, length=b))
    initial_rs = RangeSet(ranges=ranges)
    full_transformation = reduce(RangeSet.add, range_sets, initial_rs)
    return min(r.destination for r in full_transformation.ranges)


if __name__ == "__main__":
    from aoc_cas.util import solve_with_examples

    solve_with_examples(year=2023, day=5)
    data = get_data(year=2023, day=5)
