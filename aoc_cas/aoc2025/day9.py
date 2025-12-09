# https://adventofcode.com/2025/day/9
from itertools import pairwise

from aoc_cas.common import Coordinate


def get_firepole_coords(input: str) -> list[Coordinate]:
    coords: list[Coordinate] = []
    for line in input.splitlines():
        x_str, y_str = line.split(",")
        coords.append(Coordinate(x=int(x_str), y=int(y_str)))
    return coords


def iter_edges(coords: list[Coordinate]) -> list[tuple[Coordinate, Coordinate]]:
    return list(pairwise(coords + coords[:1]))


def build_horizontal_bands(coords: list[Coordinate]) -> list[tuple[int, int, list[tuple[int, int]]]]:
    edges = iter_edges(coords)
    unique_y = sorted({coord.y for coord in coords})
    bands: list[tuple[int, int, list[tuple[int, int]]]] = []
    for y_low, y_high in pairwise(unique_y):
        if y_low == y_high:
            continue
        y_mid = (y_low + y_high) / 2
        intersections: list[int] = []
        for start, end in edges:
            if start.x != end.x:
                continue
            seg_low = min(start.y, end.y)
            seg_high = max(start.y, end.y)
            if seg_low < y_mid < seg_high:
                intersections.append(start.x)
        intersections.sort()
        spans: list[tuple[int, int]] = []
        for left, right in zip(intersections[::2], intersections[1::2]):
            spans.append((min(left, right), max(left, right)))
        bands.append((y_low, y_high, spans))
    return bands


def rectangle_inside_polygon(
    bands: list[tuple[int, int, list[tuple[int, int]]]],
    x_min: int,
    x_max: int,
    y_min: int,
    y_max: int,
) -> bool:
    if x_min == x_max or y_min == y_max:
        return False
    for band_low, band_high, spans in bands:
        overlap_low = max(band_low, y_min)
        overlap_high = min(band_high, y_max)
        if overlap_low < overlap_high:
            if not any(x_min >= left and x_max <= right for left, right in spans):
                return False
    return True


def part_a(input: str) -> int:
    coords = get_firepole_coords(input)
    max_area = 0
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            if coords[i].x == coords[j].x or coords[i].y == coords[j].y:
                continue
            area = (1 + abs(coords[i].x - coords[j].x)) * (1 + abs(coords[i].y - coords[j].y))
            max_area = max(max_area, area)
    return max_area


def part_b(input: str) -> int:
    coords = get_firepole_coords(input)
    bands = build_horizontal_bands(coords)

    max_area = 0
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            x_min = min(coords[i].x, coords[j].x)
            x_max = max(coords[i].x, coords[j].x)
            y_min = min(coords[i].y, coords[j].y)
            y_max = max(coords[i].y, coords[j].y)
            if not rectangle_inside_polygon(bands, x_min, x_max, y_min, y_max):
                continue
            area = (1 + (x_max - x_min)) * (1 + (y_max - y_min))
            max_area = max(max_area, area)
    return max_area


if __name__ == "__main__":
    from aoc_cas.util import solve_with_example_input

    solve_with_example_input(year=2025, day=9, answers_a=[50], answers_b=[24])
