from functools import lru_cache
from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True, eq=True)
class Tile:
    id: int
    up: Tuple[str]
    down: Tuple[str]
    left: Tuple[str]
    right: Tuple[str]

    @staticmethod
    def createFromData(tileData):
        tileId, *tileString = tileData.splitlines()
        tileId = int(tileId.split()[-1][:-1])
        up = "".join(tileString[0])
        down = "".join(tileString[-1])
        left = "".join(row[0] for row in tileString)
        right = "".join(row[-1] for row in tileString)
        return Tile(tileId, up=up, right=right, down=down, left=left)

    @lru_cache(1)
    def rotate(self):
        return Tile(self.id, up=self.left[::-1], right=self.up, down=self.right[::-1], left=self.down)

    @lru_cache(1)
    def flip(self):
        return Tile(self.id, up=self.up[::-1], right=self.left, down=self.down[::-1], left=self.right)

    def variations(self):
        tile = self
        yield tile
        yield tile.flip()
        for _ in range(3):
            tile = tile.rotate()
            yield tile
            yield tile.flip()

    def __repr__(self):
        return f"{self.id}"

    def __str__(self):
        return "\n".join(self.tile)


def tileItUp(tiles):
    N = int(len(tiles) ** 0.5)
    assert N ** 2 == len(tiles)

    def findRows(row, remainingTiles):
        if len(row) == N:
            yield row
        left = row[-1] if row else None
        for t in remainingTiles:
            for tile in t.variations():
                if not left or left.right == tile.left:
                    yield from findRows(row + (tile,), remainingTiles - {t})

    def stackRows(stack, remainingRows):
        if len(stack) == N:
            yield stack
        prevRow = stack[-1] if stack else set()
        prevRowIds = {t.id for t in prevRow}
        for row in remainingRows:
            if not prevRowIds.isdisjoint({t.id for t in row}):
                continue
            if all(aboveTile.down == rowTile.up for aboveTile, rowTile in zip(prevRow, row)):
                yield from stackRows(stack + (row,), remainingRows - {row})

    allTiles = frozenset(tiles)
    rows = frozenset(findRows(tuple(), allTiles))
    grids = stackRows(tuple(), rows)
    return next(grids)


def getTiles(data):
    tiles = []
    for tileData in data.split("\n\n"):
        tiles.append(Tile.createFromData(tileData))
    return tiles


def part1(data):
    tiles = getTiles(data)
    grid = tileItUp(tiles)

    c1, c2, c3, c4 = grid[0][0], grid[0][-1], grid[-1][0], grid[-1][-1]
    return c1.id * c2.id * c3.id * c4.id


def part2(data):
    pass


if __name__ == "__main__":
    from aocd import get_data

    data = """
Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...
""".strip()

    # data = get_data(year=2020, day=20)

    print(part1(data))
