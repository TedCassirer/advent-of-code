from collections import Counter


def _parse_lists(data: str) -> tuple[list[int], list[int]]:
    left_list, right_list = [], []
    for line in data.splitlines():
        left, right = map(int, line.split("   "))
        left_list.append(left)
        right_list.append(right)
    return left_list, right_list


def part_a(data: str) -> int:
    left, right = _parse_lists(data)
    left.sort()
    right.sort()
    return sum(abs(right_value - left_value) for left_value, right_value in zip(left, right))


def part_b(data: str) -> int:
    left, right = _parse_lists(data)
    left_count, right_count = Counter(left), Counter(right)
    return sum(k * left_count[k] * right_count[k] for k in left_count.keys() & right_count.keys())


if __name__ == "__main__":
    from aoc_cas.util import solve_with_example_input

    solve_with_example_input(year=2024, day=1)
