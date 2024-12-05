import re


def _mul_sum(data: str) -> int:
    return sum(int(n1) * int(n2) for n1, n2 in re.findall(r"mul\((\d+),(\d+)\)", data))


def part_a(data: str) -> int:
    return _mul_sum(data)


def part_b(data: str) -> int:
    data = data.replace("\n", "")
    enabled_data = re.sub(r"(don't\(\).+?do\(\))|(don't\(\).+?$)", "", data)
    return _mul_sum(enabled_data)


if __name__ == "__main__":
    from aoc_cas.util import solve_with_example_data

    solve_with_example_data(year=2024, day=3)
