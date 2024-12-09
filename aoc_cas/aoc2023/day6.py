import math
import re


def ways_to_win(time, distance) -> int:
    x1 = time / 2 + (time**2 / 4 - distance) ** 0.5
    x2 = time / 2 - (time**2 / 4 - distance) ** 0.5
    return (int(x1) - math.ceil(x2)) + 1 - (x1.is_integer() + x2.is_integer())


def part_a(data: str) -> int:
    time_data, distance_data = data.splitlines()
    time = map(int, re.findall(r"\d+", time_data))
    distance = map(int, re.findall(r"\d+", distance_data))
    return math.prod(ways_to_win(t, d) for t, d in zip(time, distance))


def part_b(data: str) -> int:
    time_data, distance_data = data.splitlines()
    time = int(re.sub(r"\D", "", time_data))
    distance = int(re.sub(r"\D", "", distance_data))
    return ways_to_win(time, distance)


if __name__ == "__main__":
    from aoc_cas.util import solve_with_example_input

    solve_with_example_input(year=2023, day=6)
