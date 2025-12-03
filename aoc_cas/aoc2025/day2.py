def parse_ranges(input: str) -> list[tuple[int, int]]:
    input = input.strip().replace("\n", "").strip()
    ranges: list[tuple[int, int]] = []
    for r in input.split(","):
        start, end = r.split("-")
        ranges.append((int(start), int(end)))
    return ranges


def repeats(number: int, k: int) -> bool:
    s = str(number)
    if len(s) % k != 0:
        return False
    step = len(s) // k
    return all(s[:step] == s[i : i + step] for i in range(step, len(s), step))


def part_a(input: str) -> int:
    ranges = parse_ranges(input)
    ans = 0
    for start, end in ranges:
        for number in range(start, end + 1):
            if repeats(number, 2):
                ans += number
    return ans


def part_b(input: str) -> int:
    ranges = parse_ranges(input)
    ans = 0
    for start, end in ranges:
        for number in range(start, end + 1):
            for k in range(2, len(str(number)) + 1):
                if repeats(number, k):
                    ans += number
                    break
    return ans


if __name__ == "__main__":
    from aoc_cas.util import solve_with_example_input

    solve_with_example_input(year=2025, day=2)
