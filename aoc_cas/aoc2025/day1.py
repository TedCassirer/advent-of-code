from typing import Iterator


def get_knob_turns(input: str) -> Iterator[int]:
    for line in input.splitlines():
        dir, val = line[0], int(line[1:])
        if dir == "L":
            yield -val
        elif dir == "R":
            yield val


def part_a(input: str) -> int:
    knob = 50
    ans = 0
    for turn in get_knob_turns(input):
        knob = (knob + turn) % 100
        if knob == 0:
            ans += 1
    return ans


def part_b(input: str) -> int:
    knob = 50
    ans = 0
    for turn in get_knob_turns(input):
        ans += abs(turn) // 100
        turn = (turn % 100) if turn >= 0 else -(abs(turn) % 100)
        if knob != 0 and (knob + turn >= 100 or knob + turn <= 0):
            ans += 1
        knob = (knob + turn) % 100
    return ans


if __name__ == "__main__":
    from aoc_cas.util import solve_with_example_input

    solve_with_example_input(year=2025, day=1, answers_b=[6])
