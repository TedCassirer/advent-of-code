from dataclasses import dataclass
from typing import Tuple
from collections import defaultdict


@dataclass(frozen=True, eq=True)
class Tile:
    id: int
    data: Tuple[Tuple[str]]

    @staticmethod
    def createFromData(tileData):
        tileId, *data = tileData.splitlines()
        tileId = int(tileId.split()[-1][:-1])
        return Tile(tileId, data=tuple(map(tuple, data)))

    @property
    def up(self):
        return tuple(self.data[0])

    @property
    def right(self):
        return tuple(row[-1] for row in self.data)

    @property
    def down(self):
        return tuple(self.data[-1])

    @property
    def left(self):
        return tuple(row[0] for row in self.data)

    def rotate(self):
        return Tile(self.id, data=rotateMatrix(self.data))

    def flip(self):
        return Tile(self.id, data=flipMatrix(self.data))

    def variations(self):
        tile = self
        yield tile
        yield tile.flip()
        for _ in range(3):
            tile = tile.rotate()
            yield tile
            yield tile.flip()

    def stripBorders(self):
        return [r[1:-1] for r in self.data[1:-1]]


def flipMatrix(matrix):
    return matrix[::-1]


def rotateMatrix(matrix):
    return tuple(zip(*matrix[::-1]))


def tileItUp(tiles):
    N = int(len(tiles) ** 0.5)
    assert N ** 2 == len(tiles)

    allTiles = frozenset(tileVariation for tile in tiles for tileVariation in tile.variations())
    borderIndex = defaultdict(list)
    for tile in allTiles:
        borderIndex[tile.left].append(tile)

    def findRows(row, blackList=frozenset()):
        if len(row) == N:
            yield row
            return
        candidates = borderIndex[row[-1].right] if row else allTiles
        for nextTile in candidates:
            if nextTile.id in blackList:
                continue
            yield from findRows(row + (nextTile,), blackList | {nextTile.id})

    def stackRows(stack, remainingRows):
        if len(stack) == N:
            yield stack
            return
        prevRow = stack[-1] if stack else frozenset()
        seenIds = {t.id for row in stack for t in row}
        for row in remainingRows:
            if not seenIds.isdisjoint({t.id for t in row}):
                continue
            if all(aboveTile.down == rowTile.up for aboveTile, rowTile in zip(prevRow, row)):
                yield from stackRows(stack + (row,), remainingRows - {row})

    rows = frozenset(findRows(tuple(), frozenset()))
    yield from stackRows(tuple(), rows)


def mergeTiles(grid):
    image = []
    for row in grid:
        lines = zip(*(t.stripBorders() for t in row))
        lines = tuple(tuple(l for subline in line for l in subline) for line in lines)
        image.extend(lines)
    return image


def countSeaMonsters(image):
    # Indices for every # in the seamonster
    top = [18]
    mid = [0, 5, 6, 11, 12, 17, 18, 19]
    bot = [1, 4, 7, 10, 13, 16]
    monsters = 0
    for r1, r2, r3 in zip(image, image[1:], image[2:]):
        for i in range(len(r2) - 20):
            if (
                all(r1[i + t] == "#" for t in top)
                and all(r2[i + m] == "#" for m in mid)
                and all(r3[i + b] == "#" for b in bot)
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
    seaMonster = """
                      # 
    #    ##    ##    ###
     #  #  #  #  #  #   
    """
    tiles = getTiles(data)
    grid = next(tileItUp(tiles))
    image = mergeTiles(grid)
    monsters = countSeaMonsters(image)
    while not (monsters := countSeaMonsters(image) or countSeaMonsters(flipMatrix(image))):
        image = rotateMatrix(image)
    return sum(l.count("#") for l in image) - seaMonster.count("#") * monsters


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2020, day=20)
    print(part1(data))
    print(part2(data))
