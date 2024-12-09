import itertools
from math import lcm
from typing import Iterable, Callable


def parse_instructions(data: str) -> tuple[Iterable[int], dict[str, tuple[str, str]]]:
    moves_data, _, *instruction_data = data.splitlines()
    instructions: dict[str, tuple[str, str]] = {}
    for line in instruction_data:
        position, left_right = line.split(" = ")
        left, right = left_right[1:-1].split(", ")
        instructions[position] = (left, right)

    moves = [0 if c == "L" else 1 for c in moves_data]
    return moves, instructions


def steps_to_reach_goal(
    start: str, is_goal: Callable[[str], bool], moves: Iterable[int], instructions: dict[str, tuple[str, str]]
) -> int:
    curr = start
    steps = 0
    for move in itertools.cycle(moves):
        curr = instructions[curr][move]
        steps += 1
        if is_goal(curr):
            return steps


def part_a(data: str) -> int:
    moves, instructions = parse_instructions(data)
    is_goal = lambda p: p == "ZZZ"
    return steps_to_reach_goal("AAA", is_goal, moves, instructions)


def part_b(data: str) -> int:
    moves, instructions = parse_instructions(data)
    is_goal = lambda p: p.endswith("Z")
    start_positions = [pos for pos in instructions.keys() if pos.endswith("A")]
    steps = []
    for pos in start_positions:
        step = steps_to_reach_goal(pos, is_goal, moves, instructions)
        print(pos, step)
        steps.append(step)
    return lcm(*steps)


if __name__ == "__main__":
    from aoc_cas.util import solve_with_example_input

    solve_with_example_input(year=2023, day=8)
