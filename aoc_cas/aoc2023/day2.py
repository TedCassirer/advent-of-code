import dataclasses
from collections import defaultdict
from typing import TypeVar


R = TypeVar("R", bound="Round")


@dataclasses.dataclass(frozen=True)
class Round:
    id: int
    red: int = 0
    blue: int = 0
    green: int = 0

    @classmethod
    def from_data_line(cls: type[R], line: str) -> R:
        game_part, cube_part = line.split(": ")
        game_id = int(game_part.split(" ")[1])

        most_seen: dict[str, int] = defaultdict(int)
        for cube_set in cube_part.split("; "):
            for draw in cube_set.split(", "):
                count, color = draw.split(" ")
                most_seen[color] = max(most_seen[color], int(count))

        return cls(game_id, **most_seen)


def part_a(data: str) -> int:
    result = 0
    for round in map(Round.from_data_line, data.splitlines()):
        if round.red <= 12 and round.green <= 13 and round.blue <= 14:
            result += round.id
    return result


def part_b(data: str) -> int:
    result = 0
    for round in map(Round.from_data_line, data.splitlines()):
        result += round.blue * round.green * round.red
    return result


if __name__ == "__main__":
    from aoc_cas.util import solve_with_example_input

    solve_with_example_input(year=2023, day=2)
