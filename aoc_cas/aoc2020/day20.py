from functools import lru_cache
from dataclasses import dataclass
from typing import Tuple, List
import re

seamonster = """
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
"""


@dataclass(frozen=True, eq=True)
class Tile:
    id: int
    tileString: Tuple[str]
    up: Tuple[str]
    down: Tuple[str]
    left: Tuple[str]
    right: Tuple[str]
    rotations: int
    flipped: bool

    @staticmethod
    def createFromData(tileData):
        tileId, *tileString = tileData.splitlines()
        tileId = int(tileId.split()[-1][:-1])
        up = "".join(tileString[0])
        down = "".join(tileString[-1])
        left = "".join(row[0] for row in tileString)
        right = "".join(row[-1] for row in tileString)
        return Tile(
            tileId, tileString=tuple(tileString), up=up, right=right, down=down, left=left, rotations=0, flipped=False
        )

    @lru_cache(1)
    def rotate(self):
        return Tile(
            self.id,
            tileString=self.tileString,
            up=self.left[::-1],
            right=self.up,
            down=self.right[::-1],
            left=self.down,
            rotations=self.rotations + 1,
            flipped=self.flipped,
        )

    @lru_cache(1)
    def flip(self):
        return Tile(
            self.id,
            tileString=self.tileString,
            up=self.up[::-1],
            right=self.left,
            down=self.down[::-1],
            left=self.right,
            rotations=self.rotations,
            flipped=not self.flipped,
        )

    def variations(self):
        tile = self
        yield tile
        yield tile.flip()
        for _ in range(3):
            tile = tile.rotate()
            yield tile
            yield tile.flip()

    @property
    def tileData(self):
        output = [r[1:-1] for r in self.tileString[1:-1]]
        for _ in range(self.rotations):
            output = ["".join(r) for r in zip(*output[::-1])]
        if self.flipped:
            output = [r[::-1] for r in output]
        return output

    def __repr__(self):
        return f"{self.id}"

    def __str__(self):
        return "\n".join(self.tile)


def tileItUp(tiles):
    N = int(len(tiles) ** 0.5)
    assert N ** 2 == len(tiles)

    def findRows(row, remainingTiles):
        if len(row) == N:
            assert all(t1.right == t2.left for t1, t2 in zip(row, row[1:]))
            yield row
        left = row[-1] if row else None
        for t in remainingTiles:
            for tile in t.variations():
                if not left or left.right == tile.left:
                    yield from findRows(row + (tile,), remainingTiles - {t})

    def stackRows(stack, remainingRows):
        if len(stack) == N:
            ids = {t.id for r in stack for t in r}
            assert(len(ids) == N**2)
            yield stack
        prevRow = stack[-1] if stack else set()
        seenIds = {t.id for row in stack for t in row}
        for row in remainingRows:
            if not seenIds.isdisjoint({t.id for t in row}):
                continue
            if all(aboveTile.down == rowTile.up for aboveTile, rowTile in zip(prevRow, row)):
                yield from stackRows(stack + (row,), remainingRows - {row})

    allTiles = frozenset(tiles)
    rows = frozenset(findRows(tuple(), allTiles))
    grids = stackRows(tuple(), rows)
    return grids


def constructImage(grid):
    image = []
    for row in grid:
        image.extend("".join(rowString) for rowString in zip(*map(lambda t: t.tileData, row)))
    return "\n".join(image)


def findSeamonsters3(image):
    lines = image.splitlines()
    N = len(lines)

    tops = [18]
    mids = [0, 5, 6, 11, 12, 17, 18, 19]
    bots = [1, 4, 7, 10, 13, 16]
    monsters = 0
    for r1, r2, r3 in zip(lines, lines[1:], lines[2:]):
        for i in range(len(r2)-20):
            if all(r1[i+t] == '#' for t in tops) and all(r2[i+m] == '#' for m in mids) and all(r3[i+b] == '#' for b in bots):
                monsters += 1
    return monsters


def getTiles(data):
    return [Tile.createFromData(tileData) for tileData in data.split("\n\n")]


def part1(data):
    tiles = getTiles(data)
    grid = next(tileItUp(tiles))
    c1, c2, c3, c4 = grid[0][0], grid[0][-1], grid[-1][0], grid[-1][-1]
    return c1.id * c2.id * c3.id * c4.id


def part2(data):
    tiles = getTiles(data)
    for grid in tileItUp(tiles):
        image = constructImage(grid)
        monsters = findSeamonsters3(image)
        if monsters:
            return image.count("#") - seamonster.count("#") * monsters


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2020, day=20)
    # print(part1(data))

    print(part2(data))
