from aoc_cas.common import Coordinate, DIR_UP, Direction, Grid
import typing as t


def _parse_map(data: str) -> tuple[Coordinate, Grid[str]]:
    grid = Grid([list(line) for line in data.splitlines()])
    guard_coord = grid.find("^")
    assert guard_coord is not None
    return guard_coord, grid


def _traverse(grid: Grid[str], start: Coordinate, start_dir: Direction) -> t.Iterator[Coordinate]:
    curr = start
    dir = start_dir
    while grid.in_bounds(curr):
        yield curr
        nxt = curr.move(dir)
        while grid.get(nxt) == "#":
            dir = dir.turn_right()
            nxt = curr.move(dir)
        curr = nxt


def _check_if_loop(grid: Grid[str], start: Coordinate, start_dir: Direction) -> bool:
    prev_coord = start
    visited: set[tuple[Coordinate, Coordinate]] = set()
    for coord in _traverse(grid, start, start_dir):
        if (prev_coord, coord) in visited:
            return True
        visited.add((prev_coord, coord))
        prev_coord = coord
    return False


def part_a(data: str) -> int:
    guard_coord, grid = _parse_map(data)
    return len(set(_traverse(grid, guard_coord, DIR_UP)))


def part_b(data: str) -> int:
    guard_coord, grid = _parse_map(data)
    loops_if_obstacle_placed = 0
    visited_coords = set(_traverse(grid, guard_coord, DIR_UP))
    visited_coords.remove(guard_coord)
    for obstacle in visited_coords:
        prev_val = grid[obstacle]
        grid[obstacle] = "#"
        if _check_if_loop(grid, guard_coord, DIR_UP):
            loops_if_obstacle_placed += 1
        grid[obstacle] = prev_val

    return loops_if_obstacle_placed


if __name__ == "__main__":
    from aoc_cas.util import solve_with_example_input

    solve_with_example_input(year=2024, day=6)
