# https://adventofcode.com/2025/day/10
from collections import deque
from typing import Iterator

import numpy as np

from aoc_cas.util import solve_with_example_input

LampState = int
Button = tuple[int, ...]
Jolt = list[int]
Machine = tuple[LampState, list[Button], Jolt]


def get_machines(input: str) -> Iterator[Machine]:
    for line in input.splitlines():
        lamp_str, *buttons_str, jolt_str = line.split(" ")
        lamp_state = 0

        for k, c in enumerate(lamp_str[1:-1]):
            if c == "#":
                lamp_state |= 1 << k

        buttons: list[Button] = []
        for button_str in buttons_str:
            buttons.append(tuple(int(n) for n in button_str[1:-1].split(",")))

        jolt_requirement = [int(n) for n in jolt_str[1:-1].split(",")]

        yield lamp_state, buttons, jolt_requirement


def get_matrixes(input: str) -> Iterator[tuple[np.ndarray, np.ndarray, np.ndarray]]:
    for line in input.splitlines():
        lamp_str, *buttons_str, jolt_str = line.split(" ")

        lamp_array = []
        for c in lamp_str[1:-1]:
            lamp_array.append(1 if c == "#" else 0)
        b_lamp = np.array(lamp_array, int)

        button_arrays = []
        for button_str in buttons_str:
            button_array = []
            for k in range(len(lamp_array)):
                button_array.append(1 if str(k) in button_str else 0)
            button_arrays.append(button_array)
        A = np.array(button_arrays, int).T  # shape (num_lamps, num_buttons)

        jolt_requirement = [int(n) for n in jolt_str[1:-1].split(",")]
        b_jolt = np.array(jolt_requirement, int)

        yield A, b_lamp, b_jolt


def find_min_button_presses(A: np.ndarray, b: np.ndarray) -> int:
    print("========================== ")
    print("A =\n", A)
    print("b =", b)

    R, pivots = rref(np.hstack([A, b[:, None]]))
    if len(pivots) <= A.shape[0]:
        return R[:, -1].sum()
    _, n_vars = A.shape
    free_vars = np.array([j for j in range(n_vars) if j not in pivots])
    print("row reduced echelon form:\n", R)
    A_basic = A[:, pivots]  # shape (4,4)
    A_free = A[:, free_vars]  # shape (4,2)
    # Select free vars rows in b

    # Calculate free var upper bounds
    print(A_free)
    upper_bounds = [max(A_free[:, i] * b) for i in range(A_free.shape[1])]
    print("Upper bounds for free vars:", upper_bounds)

    # All combinations for free vars within bounds
    ranges = [range(ub + 1) for ub in upper_bounds]

    best_sum = 1e9
    best_solutions = []
    for x_free in np.array(np.meshgrid(*ranges)).T.reshape(-1, len(upper_bounds)):
        # Solve for basic variables
        rhs = b - A_free @ x_free
        x_basic = np.linalg.solve(A_basic, rhs)

        x = np.zeros(n_vars)
        x[pivots] = x_basic
        x[free_vars] = x_free

        # Integer? Non-negative?
        if np.any(x < -1e-9):
            continue
        if not np.allclose(x, x.round()):
            continue
        assert (A @ x == b).all()
        S = x.sum()
        if S < best_sum:
            best_sum = S
            best_solutions = [x]
        elif S == best_sum:
            best_solutions.append(x)

    print("Best sum:", best_sum)
    print("Best solutions:", best_solutions)
    return int(best_sum)


def part_a(input: str) -> int:
    ans = 0
    for lamp_state, buttons, _ in get_machines(input):
        seen = set()
        to_check: deque[tuple[int, LampState]] = deque([(0, lamp_state)])
        bit_buttons: list[int] = []
        for b in buttons:
            button_bits = 0
            for n in b:
                button_bits |= 1 << n
            bit_buttons.append(button_bits)
        while True:
            step, state = to_check.popleft()
            if state == 0:
                ans += step
                break
            for button in bit_buttons:
                new_state = state ^ button
                if new_state not in seen:
                    seen.add(new_state)
                    to_check.append((step + 1, new_state))
    return ans


def part_b(input: str) -> int:
    ans = 0
    for A, _, b_jolt in get_matrixes(input):
        ans += find_min_button_presses(A, b_jolt)
    return ans


if __name__ == "__main__":
    solve_with_example_input(year=2025, day=10)
    # solve_with_real_input_data(year=2025, day=10)


def rref(A):
    A = A.copy()
    m, n = A.shape
    row = 0
    pivots = []

    for col in range(n):
        if row >= m:
            break

        # Find pivot
        pivot = np.argmax(np.abs(A[row:, col])) + row
        if A[pivot, col] == 0:
            continue  # no pivot in this column

        # Swap pivot row
        A[[row, pivot]] = A[[pivot, row]]

        # Normalize pivot row
        A[row] = A[row] / A[row, col]

        # Eliminate other rows
        for r in range(m):
            if r != row:
                A[r] -= A[r, col] * A[row]

        pivots.append(col)  # <--- this column has a pivot
        row += 1

    return A, pivots


# A = np.array(
#     [
#         [0, 0, 0, 0, 1, 1],
#         [0, 1, 0, 0, 0, 1],
#         [0, 0, 1, 1, 1, 0],
#         [1, 1, 0, 1, 0, 0],
#     ],
#     int,
# )
# b = np.array([3, 5, 4, 7], int)
# M = np.hstack([A, b[:, None]])  # shape (4, 7)
#
# R, pivots = rref(A)
# # print("RREF:\n", R)
# # print("pivot cols:", pivots)
# _, n_vars = A.shape
# free_vars = [j for j in range(n_vars) if j not in pivots]
# # print("free vars:", free_vars)
#
# A_basic = A[:, pivots]   # shape (4,4)
# A_free  = A[:, free_vars]    # shape (4,2)
#
# best_sum = 1e9
# best_solutions = []
#
# for s in range(5):      # x3 = s
#     for t in range(4):  # x5 = t
#         x_free = np.array([s, t])
#
#         # Solve for basic variables
#         rhs = b - A_free @ x_free
#         x_basic = np.linalg.solve(A_basic, rhs)
#
#         x = np.zeros(6)
#         x[pivots] = x_basic
#         x[free_vars]  = x_free
#
#         # Integer? Non-negative?
#         if np.any(x < -1e-9): continue
#         if not np.allclose(x, x.round()): continue
#
#         S = x.sum()
#         if S < best_sum:
#             best_sum = S
#             best_solutions = [x]
#         elif S == best_sum:
#             best_solutions.append(x)


# print("A_basic:\n", A_basic)
# print("A_free:\n", A_free)

# print("x_basic:\n", x_basic)
# print("x_free:\n", x_free)

# print("Best sum:", best_sum)
# print("Best solutions:", best_solutions)

# print("Check solutions:")
# for sol in best_solutions:
#     print("x:", sol)
#     print("A @ x:", A @ sol)
#     print("b:", b)
#     print()
# print(A)
# print(np.linalg.matrix_rank(A))
# print(b)
#
# print(rref(np.hstack((A, b))))

"""
A = [[0 0 0 0 1 1]
 [0 1 0 0 0 1]
 [0 0 1 1 1 0]
 [1 1 0 1 0 0]]
 b = [[3]
 [5]
 [4]
 [7]]
 
A augmented with b:
[[0 0 0 0 1 1 3]
[0 1 0 0 0 1 5]
[0 0 1 1 1 0 4]
[1 1 0 1 0 0 7]]

row reduced echelon form:
[[ 1  0  0  1  0 -1  2]
 [ 0  1  0  0  0  1  5]
 [ 0  0  1  1  0 -1  1]
 [ 0  0  0  0  1  1  3]]
 
 
x0 + x3 - x5 = 2
x1 + x5 = 5
x2 + x3 - x5 = 1
x4 + x5 = 3

x0 = 2 - x3 + x5
x1 = 5 - x5
x2 = 1 - x3 + x5
x4 = 4 - x5

x3 = s
x5 = t

x0 = 2 - s + t
x1 = 5 - t
x2 = 1 - s + t
x3 = s
x4 = 3 - t
x5 = t


sum = 11 - s + t


(3) (1,3) (2) (2,3) (0,2) (0,1)

[4, 5, 1+4, 2+5]
[4, 5, 5, 7]

"""
