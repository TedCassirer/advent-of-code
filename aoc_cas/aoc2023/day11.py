Coordinate = tuple[int, int]


def get_galaxy_coords(data: str) -> list[Coordinate]:
    coords = []
    for y, row in enumerate(data.splitlines()):
        for x, v in enumerate(row):
            if v == "#":
                coords.append((y, x))
    return coords


def calculate_expanded_distance(coords: list[Coordinate]) -> int:
    distance = 0
    seen_galaxies = 0
    remaining_galaxies = len(coords)
    by_y = sorted(c[0] for c in coords)
    prev = 0
    for y in by_y:
        if y - 1 > prev:
            distance += (y - 1 - prev) * (seen_galaxies * remaining_galaxies)
        seen_galaxies += 1
        remaining_galaxies -= 1
        prev = y

    seen_galaxies = 0
    remaining_galaxies = len(coords)
    by_x = sorted(c[1] for c in coords)
    prev = 0
    for x in by_x:
        if x - 1 > prev:
            distance += (x - 1 - prev) * (seen_galaxies * remaining_galaxies)
        seen_galaxies += 1
        remaining_galaxies -= 1
        prev = x

    return distance


def total_distance(coords: list[Coordinate]) -> int:
    total = 0
    for i, c1 in enumerate(coords):
        for c2 in coords[i + 1 :]:
            total += abs(c2[0] - c1[0]) + abs(c2[1] - c1[1])

    return total


def part_a(data: str) -> int:
    coords = get_galaxy_coords(data)
    distance = total_distance(coords)
    return distance + calculate_expanded_distance(coords)


def part_b(data: str, expansion: int = 1000000) -> int:
    coords = get_galaxy_coords(data)
    distance = total_distance(coords)
    return distance + calculate_expanded_distance(coords) * (expansion - 1)


if __name__ == "__main__":
    from aoc_cas.util import solve_with_example_data

    solve_with_example_data(year=2023, day=11)
