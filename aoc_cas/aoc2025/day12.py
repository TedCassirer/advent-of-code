# https://adventofcode.com/2025/day/12

import dataclasses


@dataclasses.dataclass(frozen=True, eq=True)
class Piece:
    name: str
    shape: tuple[tuple[int, int], ...]

    @property
    def area(self) -> int:
        return len(self.shape)

    def rotations(self) -> list[tuple[tuple[int, int], ...]]:
        rotations = {tuple(sorted(self.shape))}
        current = self.shape
        for _ in range(3):
            rotated: list[tuple[int, int]] = []
            for y, x in current:
                rotated.append((x, -y))
            current = rotated
            rotations.add(tuple(sorted(current)))
        return list(tuple(rotations))


@dataclasses.dataclass(frozen=True)
class Region:
    height: int
    width: int
    required_pieces: tuple[int, int, int, int, int]

    @property
    def area(self) -> int:
        return self.height * self.width

    def __str__(self) -> str:
        return f"{self.height}x{self.width} <{' '.join(str(n) for n in self.required_pieces)}>"


def parse_input(input: str) -> tuple[list[Piece], list[Region]]:
    *piece_section, grid_sections = input.split("\n\n")
    pieces: list[Piece] = []
    for piece_str in piece_section:
        lines = piece_str.splitlines()
        name = lines[0].strip()
        shape: list[tuple[int, int]] = []
        for y, line in enumerate(lines[1:], start=-1):
            for x, char in enumerate(line, start=-1):
                if char == "#":
                    shape.append((y, x))
        pieces.append(Piece(name, tuple(shape)))

    regions: list[Region] = []
    for grid_str in grid_sections.splitlines():
        dim_str, req_str = grid_str.split(": ")
        height_str, width_str = dim_str.split("x")
        height, width = int(height_str), int(width_str)
        required_pieces = tuple(int(n) for n in req_str.split(" "))
        regions.append(Region(height, width, tuple[int, int, int, int, int](required_pieces)))

    return pieces, regions


def part_a(input: str) -> int:
    pieces, regions = parse_input(input)

    ans = 0
    for region in regions:
        lower_bound_piece_area = sum(pieces[i].area * count for i, count in enumerate(region.required_pieces))
        # Filter out regions that definitely can't fit the pieces
        if lower_bound_piece_area > region.area:
            # Can't fit pieces in region
            continue
        # Filter out regions that can safely fit all pieces by assuming all pieces are
        # 3x3 squares
        simplified_region_area = 9 * (region.height // 3) * (region.width // 3)
        upper_bound_piece_area = 9 * sum(region.required_pieces)
        if upper_bound_piece_area <= simplified_region_area:
            ans += 1
            continue

        # Real input data has no such regions
        print(f"Region needs further analysis: {region}")

    return ans


def part_b(input: str) -> None:
    pass


if __name__ == "__main__":
    from aoc_cas.util import solve_with_real_input_data

    solve_with_real_input_data(
        year=2025,
        day=12,
    )
