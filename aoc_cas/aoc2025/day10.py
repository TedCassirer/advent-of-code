# https://adventofcode.com/2025/day/10
from collections import deque
import enum
from functools import cache
from typing import Iterator

from aoc_cas.util import solve_with_real_input_data


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
    print(len(list(get_machines(input))))
    for i, (_, buttons, jolt_requirement) in enumerate(get_machines(input)):
        print(i)
        @cache
        def get_valid_buttons_for_k(k:int) -> list[Button]:
            return [button for button in buttons if button[0] == k]

        def generate_press_combinations(jolt: Jolt, required_presses: int, valid_buttons: list[Button]) -> Iterator[Jolt]:
            if min(jolt) < 0:
                return
            if required_presses == 0:
                yield jolt
                return
            if not valid_buttons:
                return
            for first_button_presses in range(required_presses + 1):
                for b in valid_buttons[0]:
                    jolt[b] -= first_button_presses
                yield from generate_press_combinations(jolt, required_presses - first_button_presses, valid_buttons[1:])
                for b in valid_buttons[0]:
                    jolt[b] += first_button_presses

        def dfs(jolt: Jolt, r: int, best: int) -> int:
            if r >= best:
                return best
            if max(jolt) == 0:
                return r
            k = next(i for i, j in enumerate(jolt) if j > 0)
            valid_buttons = get_valid_buttons_for_k(k)
            allowed_presses = jolt[k]
            for current_jolt in generate_press_combinations(jolt, allowed_presses, valid_buttons):
                best = dfs(current_jolt, r + allowed_presses, best)
            return best


        ans += dfs(jolt_requirement, 0, 1<<63)

    return ans









if __name__ == "__main__":
    from aoc_cas.util import solve_with_example_input

    solve_with_example_input(year=2025, day=10)
    solve_with_real_input_data(year=2025, day=10)
