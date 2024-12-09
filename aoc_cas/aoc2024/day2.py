import typing as t


def _parse_levels(data: str) -> t.Iterator[list[int]]:
    for line in data.splitlines():
        level = [int(n) for n in line.split(" ")]
        yield level


def _is_increasing(level: list[int]) -> bool:
    return all(level[i] < level[i + 1] for i in range(len(level) - 1))


def _is_decreasing(level: list[int]) -> bool:
    return all(level[i] > level[i + 1] for i in range(len(level) - 1))


def _max_distance(level: list[int], k: int) -> int:
    return all(abs(level[i + 1] - level[i]) <= k for i in range(len(level) - 1))


def _is_safe(level: list[int]) -> bool:
    return (_is_increasing(level) or _is_decreasing(level)) and _max_distance(level, 3)


def part_a(data: str) -> int:
    safe_levels = 0
    for level in _parse_levels(data):
        if _is_safe(level):
            safe_levels += 1
    return safe_levels


def part_b(data: str) -> int:
    safe_levels = 0
    for level in _parse_levels(data):
        for i in range(len(level) + 1):
            fixed = level[:i] + level[i + 1 :]
            if _is_safe(fixed):
                safe_levels += 1
                break
    return safe_levels


if __name__ == "__main__":
    from aoc_cas.util import solve_with_example_input

    solve_with_example_input(year=2024, day=2)
