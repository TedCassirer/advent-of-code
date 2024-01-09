from aoc_cas.common import Coordinate, DIR_RIGHT, DIR_DOWN, DIR_UP, DIR_LEFT, Direction

directions: dict[str, Direction] = {
    "U": DIR_UP,
    "D": DIR_DOWN,
    "R": DIR_RIGHT,
    "L": DIR_LEFT,
}
directions_hexa = [
    DIR_RIGHT,
    DIR_DOWN,
    DIR_LEFT,
    DIR_UP,
]


def parse_dig_coords(data: str, use_encoded: bool = False) -> tuple[list[Coordinate], int]:
    coords: list[Coordinate] = [Coordinate.create(0, 0)]
    total_distance = 0
    for line in data.splitlines():
        direction, k, encoded = line.split(" ")
        if use_encoded:
            distance_str = encoded[2:7]
            dir_str = encoded[7]
            dir = directions_hexa[int(dir_str, 16)]
            distance = int(distance_str, 16)
        else:
            dir = directions[direction]
            distance = int(k)
        coords.append((coords[-1].move(dir, distance)))
        total_distance += distance - 1
        # for _ in range(int(distance)):
        #     coords.append(coords[-1].move(dir))
    return coords[:-1], total_distance - 1


def calculate_area(coords: list[Coordinate]) -> int:
    shifted = coords[1:] + [coords[0]]
    s1 = sum((c1.y + c2.y) * (c1.x - c2.x) for c1, c2 in zip(coords, shifted))
    return s1 // 2 + len(coords) // 2 + 1


def part_a(data: str) -> int:
    dig_coords, length = parse_dig_coords(data)
    area = calculate_area(dig_coords)
    return area + length // 2 + 1


def part_b(data: str) -> int:
    dig_coords, length = parse_dig_coords(data, use_encoded=True)
    area = calculate_area(dig_coords)
    return area + length // 2 + 1


if __name__ == "__main__":
    from aoc_cas.util import solve_with_examples

    solve_with_examples(year=2023, day=18)
