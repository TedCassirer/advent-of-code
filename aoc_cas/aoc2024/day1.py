from collections import Counter


def _parse_lists(data: str) -> tuple[list[int], list[int]]:
    left_list, right_list = [], []
    for line in data.splitlines():
        left, right = line.split("   ")
        left_list.append(int(left))
        right_list.append(int(right))
    return left_list, right_list


def part_a(data: str) -> int:
    left, right = _parse_lists(data)
    left.sort()
    right.sort()
    total_dist = 0
    for l, r in zip(left, right):
        total_dist += abs(l - r)
    return total_dist


def part_b(data: str) -> int:
    left, right = _parse_lists(data)
    left_count, right_count = Counter(left), Counter(right)
    return sum(k * left_count[k] * right_count[k] for k in left_count.keys())


if __name__ == "__main__":
    from aoc_cas.util import solve_with_examples

    solve_with_examples(year=2024, day=1)
