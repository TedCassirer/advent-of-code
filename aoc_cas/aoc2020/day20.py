from functools import cached_property
from dataclasses import dataclass
from typing import Tuple
from collections import defaultdict


@dataclass(frozen=True, eq=True)
class Tile:
    id: int
    tileString: Tuple[Tuple[str]]
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
        up = tuple(tileString[0])
        down = tuple(tileString[-1])
        left = tuple(row[0] for row in tileString)
        right = tuple(row[-1] for row in tileString)
        return Tile(
            tileId,
            tileString=tuple(map(tuple, tileString)),
            up=up,
            right=right,
            down=down,
            left=left,
            rotations=0,
            flipped=False,
        )

    @cached_property
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

    @cached_property
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

    @cached_property
    def variations(self):
        variations = []
        tile = self
        variations.append(tile)
        variations.append(tile.flip)
        for _ in range(3):
            tile = tile.rotate
            variations.append(tile)
            variations.append(tile.flip)
        return variations

    def tileData(self):
        output = [r[1:-1] for r in self.tileString[1:-1]]
        for _ in range(self.rotations):
            output = list(zip(*output[::-1]))
        if self.flipped:
            output = [r[::-1] for r in output]
        return output


def tileItUp(tiles):
    N = int(len(tiles) ** 0.5)
    assert N ** 2 == len(tiles)

    allTiles = frozenset(tileVariation for tile in tiles for tileVariation in tile.variations)
    tileIndex = defaultdict(list)
    for tile in allTiles:
        tileIndex[tile.left].append(tile)

    def findRows(row, blackList=frozenset()):
        if len(row) == N:
            yield row
            return
        candidates = tileIndex[row[-1].right] if row else allTiles
        for nextTile in candidates:
            if nextTile.id in blackList:
                continue
            yield from findRows(row + (nextTile,), blackList | {nextTile.id})

    def stackRows(stack, remainingRows):
        if len(stack) == N:
            yield stack
        prevRow = stack[-1] if stack else frozenset()
        seenIds = {t.id for row in stack for t in row}
        for row in remainingRows:
            if not seenIds.isdisjoint({t.id for t in row}):
                continue
            if all(aboveTile.down == rowTile.up for aboveTile, rowTile in zip(prevRow, row)):
                yield from stackRows(stack + (row,), remainingRows - {row})

    rows = frozenset(findRows(tuple(), frozenset()))
    grids = stackRows(tuple(), rows)
    return grids


def mergeTiles(grid):
    image = []
    for row in grid:
        lines = zip(*(t.tileData() for t in row))
        lines = tuple(tuple(l for subline in line for l in subline) for line in lines)
        image.extend(lines)
    return image


def countSeaMonsters(image):
    tops = [18]
    mids = [0, 5, 6, 11, 12, 17, 18, 19]
    bots = [1, 4, 7, 10, 13, 16]
    monsters = 0
    for r1, r2, r3 in zip(image, image[1:], image[2:]):
        for i in range(len(r2) - 20):
            if (
                all(r1[i + t] == "#" for t in tops)
                and all(r2[i + m] == "#" for m in mids)
                and all(r3[i + b] == "#" for b in bots)
            ):
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
    seamonster = """
                      # 
    #    ##    ##    ###
     #  #  #  #  #  #   
    """
    tiles = getTiles(data)
    for grid in tileItUp(tiles):
        image = mergeTiles(grid)
        monsters = countSeaMonsters(image)
        if monsters:
            return sum(l.count("#") for l in image) - seamonster.count("#") * monsters


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2020, day=20)
    print(part1(data))
    print(part2(data))
