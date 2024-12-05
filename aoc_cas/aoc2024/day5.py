import functools
import typing as t
from collections import defaultdict
from functools import cmp_to_key

Update = list[int]
Sorter = t.Callable[[Update], Update]


def _build_sorter(rule_data: str) -> Sorter:
    rule: dict[int, set[int]] = defaultdict(set)
    for line in rule_data.splitlines():
        n1, n2 = line.split("|")
        rule[int(n1)].add(int(n2))

    def compare(n1: int, n2: int) -> int:
        if n2 in rule[n1]:
            return -1
        return 0

    return functools.partial(lambda u: sorted(u, key=cmp_to_key(compare)))


def _build_updates(page_data: str) -> list[Update]:
    updates = []
    for line in page_data.splitlines():
        updates.append([int(n) for n in line.split(",")])
    return updates


def _parse_data(data: str) -> tuple[Sorter, list[Update]]:
    rule_data, page_data = data.split("\n\n")
    return _build_sorter(rule_data), _build_updates(page_data)


def part_a(data: str) -> int:
    sorter, updates = _parse_data(data)
    mid_page_sum = 0
    for update in updates:
        if update == sorter(update):
            mid_page_sum += update[len(update) // 2]
    return mid_page_sum


def part_b(data: str) -> int:
    sorter, updates = _parse_data(data)
    mid_page_sum = 0
    for update in updates:
        sorted_update = sorter(update)
        if update != sorted_update:
            mid_page_sum += sorted_update[len(sorted_update) // 2]
    return mid_page_sum


if __name__ == "__main__":
    from aoc_cas.util import solve_with_example_data

    solve_with_example_data(year=2024, day=5)
