from collections import Counter
from typing import NamedTuple


class HexTile(NamedTuple):
    col: int
    row: int

    def northWest(self):
        return HexTile(self.col - (self.row & 1), self.row - 1)

    def northEast(self):
        return HexTile(self.col + 1 - (self.row & 1), self.row - 1)

    def east(self):
        return HexTile(self.col + 1, self.row)

    def southWest(self):
        return HexTile(self.col - (self.row & 1), self.row + 1)

    def southEast(self):
        return HexTile(self.col + 1 - (self.row & 1), self.row + 1)

    def west(self):
        return HexTile(self.col - 1, self.row)

    def buddies(self):
        yield self.northWest()
        yield self.northEast()
        yield self.east()
        yield self.southEast()
        yield self.southWest()
        yield self.west()


MOVES = {
    "nw": HexTile.northWest,
    "ne": HexTile.northEast,
    "e": HexTile.east,
    "se": HexTile.southEast,
    "sw": HexTile.southWest,
    "w": HexTile.west,
}


def getMoves(line):
    chars = list(reversed(line))
    while chars:
        token = chars.pop()
        if token == "n" or token == "s":
            token += chars.pop()
        yield MOVES[token]


def getBlackTiles(data):
    black = set()
    for line in data.splitlines():
        current = HexTile(0, 0)
        for move in getMoves(line):
            current = move(current)
        black ^= {current}
    return black


def part1(data):
    return len(getBlackTiles(data))


def part2(data):
    black = getBlackTiles(data)
    for day in range(100):
        tilesWithAfricanAmericanBuddies = Counter()
        for tile in black:
            for buddy in tile.buddies():
                tilesWithAfricanAmericanBuddies[buddy] += 1
        newBlack = set()
        for tile, africanAmericanBuddies in tilesWithAfricanAmericanBuddies.items():
            if africanAmericanBuddies == 2 or (tile in black and africanAmericanBuddies == 1):
                newBlack.add(tile)
        black = newBlack
    return len(black)
