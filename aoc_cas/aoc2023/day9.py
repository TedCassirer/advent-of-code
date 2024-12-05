from typing import Iterator


def extrapolate(numbers: list[int], backwards=False) -> int:
    if all(n == 0 for n in numbers):
        return 0
    num_diff = [n2 - n1 for n1, n2 in zip(numbers, numbers[1:])]
    if backwards:
        return numbers[0] - extrapolate(num_diff, True)
    else:
        return numbers[-1] + extrapolate(num_diff, False)


def parse_numbers(data: str) -> Iterator[list[int]]:
    for line in data.splitlines():
        yield [int(n) for n in line.split()]


def part_a(data: str) -> int:
    return sum(extrapolate(nums) for nums in parse_numbers(data))


def part_b(data: str) -> int:
    return sum(extrapolate(nums, True) for nums in parse_numbers(data))


if __name__ == "__main__":
    from aoc_cas.util import solve_with_example_data

    solve_with_example_data(year=2023, day=9)
