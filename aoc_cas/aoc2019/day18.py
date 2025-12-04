from functools import lru_cache
import heapq
from dataclasses import dataclass, replace
from typing import FrozenSet, List, Tuple, cast
from collections import deque


def getMaze(data):
    return Maze([line.strip() for line in data.split("\n")])


@dataclass(frozen=True, eq=True, order=True)
class Coordinate:
    __slots__ = "y", "x"
    y: int
    x: int

    def connected(self):
        return [self.up(), self.right(), self.down(), self.left()]

    def up(self, steps=1):
        return replace(self, y=self.y - steps)

    def right(self, steps=1):
        return replace(self, x=self.x + steps)

    def down(self, steps=1):
        return replace(self, y=self.y + steps)

    def left(self, steps=1):
        return replace(self, x=self.x - steps)

    def manhattanDistance(self, other):
        return abs(other.x - self.x) + abs(other.y - self.y)


@dataclass(frozen=True, eq=True, repr=True, order=True)
class AStarNode1:
    __slots__ = "pos", "remaining"
    pos: Coordinate
    remaining: FrozenSet[Coordinate]

    def getNeighbours(self, maze):
        for p2 in sorted(self.remaining):
            res = maze.calculateCost(self.pos, p2)
            if not res:
                continue
            stepsToKey, requiredKeys = res
            if not self.remaining.isdisjoint(requiredKeys):
                continue
            yield stepsToKey, AStarNode1(p2, self.remaining - {p2})

    def estimateCost(self, maze):
        if not self.remaining:
            return 0
        if len(self.remaining) == 1:
            return self.pos.manhattanDistance(next(iter(self.remaining)))
        left, right = min(self.remaining), max(self.remaining)
        firstRoute = min(self.pos.manhattanDistance(left), self.pos.manhattanDistance(right))
        secondRoute = left.manhattanDistance(right)
        return firstRoute + secondRoute


@dataclass(frozen=True, eq=True, order=True)
class AStarNode2:
    __slots__ = "positions", "remaining"
    positions: Tuple[Coordinate, ...]
    remaining: FrozenSet[Coordinate]

    def getNeighbours(self, maze):
        for p2 in sorted(self.remaining):
            for i, p1 in enumerate(self.positions):
                res = maze.calculateCost(p1, p2)
                if res:
                    stepsToKey, requiredKeys = res
                    if not self.remaining.isdisjoint(requiredKeys):
                        continue
                    newPositions = list(self.positions)
                    newPositions[i] = p2
                    yield stepsToKey, AStarNode2(tuple(newPositions), self.remaining - {p2})
                    break

    def estimateCost(self, maze):
        if not self.remaining:
            return 0

        def inner(p1):
            if len(self.remaining) == 1:
                return p1.manhattanDistance(next(iter(self.remaining)))
            return min(p1.manhattanDistance(p2) for p2 in self.remaining)

        return min(map(inner, self.positions))


class Maze:
    @dataclass(frozen=True, eq=True, order=True)
    class MazeNode:
        __slots__ = "pos", "target"
        pos: Coordinate

        @lru_cache(None)
        def getNeighbours(self, maze):
            visited = {self.pos}
            queue = deque([(0, self.pos)])
            neighbours = []
            while queue:
                steps, p1 = queue.popleft()
                for p2 in p1.connected():
                    tile = maze.getTile(p2)
                    if p2 in visited or tile == "#":
                        continue
                    visited.add(p2)
                    if tile.isalpha():
                        neighbours.append((steps + 1, replace(self, pos=p2)))
                        continue
                    queue.append((steps + 1, p2))
            return neighbours

    def __init__(self, maze):
        self.maze = maze
        self.keyLocations = self.getKeyLocations()
        self.startPositions = tuple(self.getStartPositions())
        self.allKeys = frozenset(sorted(self.keyLocations.keys()))

    @lru_cache(None)
    def calculateCost(self, p1, p2):
        start = Maze.MazeNode(p1)
        res = aStarSolve(self, start, path=True, estimateCost=lambda n: n.pos.manhattanDistance(p2))
        if res:
            _, steps, path = cast(Tuple[object, int, List["Maze.MazeNode"]], res)
            requiredKeys = {
                self.keyLocations[tile.lower()]
                for tile in (self.getTile(p.pos) for p in path)
                if tile and tile.isalpha()
            }
            return steps, requiredKeys

    def getTile(self, pos):
        return self.maze[pos.y][pos.x]

    def getKeyLocations(self):
        return {c: Coordinate(y=y, x=x) for y, row in enumerate(self.maze) for x, c in enumerate(row) if c.islower()}

    def getStartPositions(self):
        return [Coordinate(y=y, x=x) for y, row in enumerate(self.maze) for x, c in enumerate(row) if c == "@"]


# @lru_cache(None)
def getNeighbours(maze, node):
    return tuple(node.getNeighbours(maze))


def aStarSolve(maze, start, estimateCost, path=False):
    initial_path: List[Maze.MazeNode] = []
    stuff = [(0, 0, start, initial_path)]
    seen = dict()
    while stuff:
        _, cost, n1, p = heapq.heappop(stuff)
        for costToMove, n2 in getNeighbours(maze, n1):
            totalCost = cost + costToMove
            estimatedCost = estimateCost(n2)
            if estimatedCost == 0:
                if path:
                    return n2, totalCost, p
                else:
                    return n2, totalCost
            if n2 in seen and seen[n2] <= totalCost:
                continue
            seen[n2] = totalCost
            new_path = p + [n2] if path else p
            heapq.heappush(stuff, (totalCost + estimatedCost, totalCost, n2, new_path))
    raise ValueError("No path found")


def part_a(data):
    maze = getMaze(data)
    assert len(maze.startPositions) == 1
    startPos = maze.startPositions[0]
    node = AStarNode1(startPos, frozenset(maze.keyLocations.values()))
    return aStarSolve(maze, node, estimateCost=lambda n: n.estimateCost(maze))[1]


def part_b(data):
    maze = getMaze(data)
    if len(maze.startPositions) == 1:
        y, x = maze.startPositions[0].y, maze.startPositions[0].x
        mazeRows = maze.maze.copy()
        mazeRows[y - 1] = mazeRows[y - 1][: x - 1] + "@#@" + mazeRows[y - 1][x + 2 :]
        mazeRows[y] = mazeRows[y][: x - 1] + "###" + mazeRows[y][x + 2 :]
        mazeRows[y + 1] = mazeRows[y + 1][: x - 1] + "@#@" + mazeRows[y + 1][x + 2 :]
        maze = Maze(mazeRows)
    assert len(maze.startPositions) == 4
    node = AStarNode2(maze.startPositions, frozenset(maze.keyLocations.values()))
    return aStarSolve(maze, node, estimateCost=lambda n: n.estimateCost(maze))[1]


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(day=18, year=2019)
    print(part_a(data))
    print(part_b(data))
