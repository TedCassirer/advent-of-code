def highest_power(jolts: list[int], batteries: int) -> int:
    to_skip = len(jolts) - batteries
    power = []
    for j in jolts:
        while power and power[-1] < j and to_skip > 0:
            power.pop()
            to_skip -= 1
        power.append(j)
    while to_skip > 0:
        power.pop()
        to_skip -= 1
    ans = 0
    for j in power:
        ans = ans * 10 + j
    return ans


def part_a(input: str) -> int:
    ans = 0
    for line in input.splitlines():
        ans += highest_power([int(x) for x in line], 2)
    return ans


def part_b(input: str) -> int:
    ans = 0
    for line in input.splitlines():
        ans += highest_power([int(x) for x in line], 12)
    return ans


if __name__ == "__main__":
    from aoc_cas.util import solve_with_example_input

    solve_with_example_input(year=2025, day=3)
