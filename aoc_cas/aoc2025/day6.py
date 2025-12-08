# https://adventofcode.com/2025/day/6

import re
from functools import reduce
from typing import Callable


def add(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b


def parse_by_row(input: str) -> tuple[list[list[int]], list[Callable[[int, int], int]]]:
    columns: list[list[int]] = []
    *number_lines, operators = input.splitlines()
    for line in number_lines:
        for c, num in enumerate(re.split(r"\s+", line.strip())):
            if c == len(columns):
                columns.append([])
            columns[c].append(int(num))
    ops: list[Callable[[int, int], int]] = []
    for c, op in enumerate(re.split(r"\s+", operators.strip())):
        op = op.strip()
        if op == "+":
            ops.append(add)
        elif op == "*":
            ops.append(multiply)
        else:
            raise ValueError(f"Unknown operation: {op}")

    return columns, ops


def parse_by_column(input: str) -> int:
    lines = input.splitlines()
    columns: list[int] = []
    ans = 0
    for col in range(len(lines[0]) - 1, -1, -1):
        col_num = 0
        for row in range(len(lines)):
            char = lines[row][col]
            if char.isdigit():
                col_num = col_num * 10 + int(char)
            elif char == "*" or char == "+":
                op = multiply if char == "*" else add
                columns.append(col_num)
                ans += reduce(op, columns)
                columns.clear()
                col_num = 0
                break
        if col_num != 0:
            columns.append(col_num)
    return ans


def part_a(input: str) -> int:
    cols, ops = parse_by_row(input)
    col_res: list[int] = []
    for col, op in zip(cols, ops):
        col_res.append(reduce(op, col))

    return sum(col_res)


def part_b(input: str) -> int:
    return parse_by_column(input)


if __name__ == "__main__":
    from aoc_cas.util import solve_with_example_input

    solve_with_example_input(year=2025, day=6)
