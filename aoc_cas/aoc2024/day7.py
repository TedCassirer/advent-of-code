from operator import add, mul
import typing as t

Operator = t.Callable[[int, int], int]


def _parse_input(data: str) -> t.Iterator[tuple[int, list[int]]]:
    for line in data.splitlines():
        val, nums = line.split(": ")
        yield int(val), [int(n) for n in nums.split(" ")]


def _can_reach_val(val: int, nums: list[int], ops: list[Operator]) -> bool:
    def inner(i: int, curr: int) -> bool:
        if i == len(nums):
            return curr == val
        if curr > val:
            return False
        return any(inner(i + 1, op(curr, nums[i])) for op in ops)

    return inner(1, nums[0])


def part_a(data: str) -> int:
    val_sum = 0
    for val, nums in _parse_input(data):
        if _can_reach_val(val, nums, [add, mul]):
            val_sum += val
    return val_sum


def part_b(data: str) -> int:
    def concatenate(a, b):
        return int(f"{a}{b}")

    val_sum = 0
    for val, nums in _parse_input(data):
        if _can_reach_val(val, nums, [add, mul, concatenate]):
            val_sum += val
    return val_sum


if __name__ == "__main__":
    from aoc_cas.util import solve_with_example_input

    solve_with_example_input(year=2024, day=7)
