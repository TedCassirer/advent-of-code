def parse(data: str) -> list[list[str]]:
    groups = []
    for group in data.split("\n\n"):
        groups.append(group.splitlines())
    return groups


def rotate(group: list[str]) -> list[str]:
    out = []
    for row in zip(*group):
        out.append("".join(row))
    return list(out)


def find_reflection(group: list[str]) -> int:
    for i in range(1, len(group)):
        d = 0
        while group[i - d - 1] == group[i + d]:
            d += 1
            if i - d - 1 == -1 or i + d == len(group):
                return i
    return 0


def find_reflection_with_smudge(group: list[str]) -> int:
    def compare_rows(r1: str, r2: str) -> int:
        return sum(0 if c1 == c2 else 1 for c1, c2 in zip(r1, r2))

    for i in range(1, len(group)):
        d = 0
        smudge_cleaned = False
        while True:
            diff = compare_rows(group[i - d - 1], group[i + d])
            if diff > 1 or (diff == 1 and smudge_cleaned):
                break
            if diff == 1:
                smudge_cleaned = True
            d += 1
            if i - d - 1 == -1 or i + d == len(group):
                if smudge_cleaned:
                    return i
                else:
                    break
    return 0


def part_a(data: str) -> int:
    result = 0
    for group in parse(data):
        horizontal_reflection = find_reflection(group)
        vertical_reflection = find_reflection(rotate(group))
        result += vertical_reflection + 100 * horizontal_reflection
    return result


def part_b(data: str) -> int:
    result = 0
    for group in parse(data):
        horizontal_reflection = find_reflection_with_smudge(group)
        vertical_reflection = find_reflection_with_smudge(rotate(group))
        result += vertical_reflection + 100 * horizontal_reflection

    return result


if __name__ == "__main__":
    from aoc_cas.util import solve_with_examples

    solve_with_examples(year=2023, day=13)
["#.##..##." "..#.##.#." "##......#" "##......#" "..#.##.#." "..##..##." "#.#.##.#."]
