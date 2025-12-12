# https://adventofcode.com/2025/day/10
from functools import cache
from typing import Iterator

from aoc_cas.util import solve_with_example_input

LampState = int
Button = tuple[int, ...]
Jolt = tuple[int, ...]
Machine = tuple[LampState, tuple[Button, ...], Jolt]


def get_machines(input: str) -> Iterator[Machine]:
    for line in input.splitlines():
        lamp_str, *buttons_str, jolt_str = line.split(" ")
        lamp_state = 0

        for c in reversed(lamp_str[1:-1]):
            lamp_state <<= 1
            if c == "#":
                lamp_state |= 1

        buttons: list[Button] = []
        for button_str in buttons_str:
            button = tuple(int(n) for n in button_str[1:-1].split(","))
            buttons.append(button)

        jolt_requirement = tuple(int(n) for n in jolt_str[1:-1].split(","))

        yield lamp_state, tuple(buttons), jolt_requirement


def button_presses_to_reach_state(buttons: tuple[Button, ...], state: LampState) -> Iterator[tuple[Button, ...]]:
    binary_buttons = []
    for button in buttons:
        b = 0
        for k in button:
            b |= 1 << k
        binary_buttons.append(b)

    def f(i: int, state: LampState) -> Iterator[tuple[Button, ...]]:
        if state == 0:
            yield ()
        if i == len(buttons):
            return
        yield from f(i + 1, state)
        for inner in f(i + 1, state ^ binary_buttons[i]):
            yield (buttons[i], *inner)

    yield from f(0, state)


def part_a(input: str) -> int:
    ans = 0
    for lamp_state, buttons, _ in get_machines(input):
        presses = min(len(buttons) for buttons in button_presses_to_reach_state(buttons, lamp_state))
        ans += presses
    return ans


def get_parity(jolt: Jolt) -> int:
    parity = 0
    for j in reversed(jolt):
        parity <<= 1
        parity |= j & 1
    return parity


def part_b(input: str) -> int:
    ans = 0
    for _, buttons, jolt_requirement in get_machines(input):

        @cache
        def inner(jolt: Jolt) -> int:
            if all(j == 0 for j in jolt):
                return 0
            if any(j < 0 for j in jolt):
                return 1 << 63
            least_presses = 1 << 63
            for button_presses in button_presses_to_reach_state(buttons, get_parity(jolt)):
                nxt_jolt = list(jolt)
                for button in button_presses:
                    for i in button:
                        nxt_jolt[i] -= 1
                presses = len(button_presses) + 2 * inner(tuple(j >> 1 for j in nxt_jolt))
                least_presses = min(least_presses, presses)
            return least_presses

        ans += inner(jolt_requirement)
    return ans


if __name__ == "__main__":
    solve_with_example_input(year=2025, day=10)
