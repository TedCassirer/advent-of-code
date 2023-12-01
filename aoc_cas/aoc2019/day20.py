from collections import defaultdict, deque
from dataclasses import dataclass, replace


class Node:
    def __init__(self):
        self.connected = {}


@dataclass(frozen=True, eq=True, order=True, repr=True)
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


def getPortalName(grid, pos):
    Y, X = len(grid), len(grid[0])
    label1 = grid[pos.y][pos.x]
    assert label1.isalpha()
    for p2 in pos.connected():
        if 0 <= p2.y < Y and 0 <= p2.x < X and grid[p2.y][p2.x].isalpha():
            label = label1 + grid[p2.y][p2.x]
            connected = set(getConnected(grid, pos))
            connected |= set(getConnected(grid, p2))
            return label, connected

    raise Exception("What the!?")


def getConnected(grid, pos):
    Y, X = len(grid), len(grid[0])
    for p in pos.connected():
        if 0 <= p.y < Y and 0 <= p.x < X and grid[p.y][p.x] == ".":
            yield p


def buildGraph(data, recursive=False):
    grid = data.splitlines()
    portals = defaultdict(set)
    nodes = defaultdict(Node)
    for y, row in enumerate(grid):
        for x, tile in enumerate(row):
            pos = Coordinate(y, x)
            if tile.isalpha():
                label, connected = getPortalName(grid, pos)
                portals[label].update(connected)
            else:
                for p2 in getConnected(grid, pos):
                    nodes[pos].connected[nodes[p2]] = 0

    Y, X = len(grid), len(grid[0])

    def isInner(pos):
        return 3 < pos.y < (Y - 3) and 3 < pos.x < (X - 3)

    for label, positions in portals.items():
        if len(positions) == 1:
            assert label == "AA" or label == "ZZ"
        else:
            p1, p2 = positions
            n1, n2 = nodes[p1], nodes[p2]
            n1.connected[n2] = 0
            n2.connected[n1] = 0

            if recursive:
                n1.connected[n2] = 1 if isInner(p1) else -1
                n2.connected[n1] = 1 if isInner(p2) else -1
                assert isInner(p1) ^ isInner(p2)
    start = portals["AA"].pop()
    goal = portals["ZZ"].pop()

    return nodes[start], nodes[goal]


def bff(start, goal):
    queue = deque([(0, 0, start)])
    visited = set()
    while queue:
        steps, recLevel, n1 = queue.popleft()
        assert recLevel >= 0

        if (n1, recLevel) in visited:
            continue
        if n1 == goal and recLevel == 0:
            return steps
        visited.add((n1, recLevel))
        for n2, rl in n1.connected.items():
            if rl == -1 and recLevel == 0:
                continue
            queue.append((steps + 1, recLevel + rl, n2))


def part_a(data):
    start, goal = buildGraph(data)
    return bff(start, goal)


def part_b(data):
    start, goal = buildGraph(data, recursive=True)
    return bff(start, goal)
