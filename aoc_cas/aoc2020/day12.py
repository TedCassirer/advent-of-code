from dataclasses import dataclass, replace


@dataclass
class Coordinate:
    __slots__ = "y", "x"
    y: int
    x: int

    def __add__(self, other):
        return Coordinate(self.y + other.y, self.x + other.x)

    def __mul__(self, v):
        return Coordinate(self.y * v, self.x * v)

    def north(self, steps=1):
        return replace(self, y=self.y + steps)

    def east(self, steps=1):
        return replace(self, x=self.x + steps)

    def south(self, steps=1):
        return replace(self, y=self.y - steps)

    def west(self, steps=1):
        return replace(self, x=self.x - steps)

    def rotate(self, degrees):
        newPos = self
        for _ in range((degrees % 360) // 90):
            newPos = Coordinate(x=newPos.y, y=-newPos.x)
        return newPos

    def manhattanDistance(self, other):
        return abs(other.x - self.x) + abs(other.y - self.y)


def part_a(data):
    actions = ((line[0], int(line[1:])) for line in data.splitlines())

    shippyBoi = Coordinate(x=0, y=0)
    direction = Coordinate(x=1, y=0)

    # "Nice ifs bro!"
    for action, val in actions:
        if action == "W":
            shippyBoi = shippyBoi.west(val)
        elif action == "E":
            shippyBoi = shippyBoi.east(val)
        elif action == "S":
            shippyBoi = shippyBoi.south(val)
        elif action == "N":
            shippyBoi = shippyBoi.north(val)
        elif action == "F":
            shippyBoi += direction * val
        elif action == "R":
            direction = direction.rotate(val)
        elif action == "L":
            direction = direction.rotate(-val)
        else:
            raise Exception("What the!?")
    return shippyBoi.manhattanDistance(Coordinate(0, 0))


def part_b(data):
    actions = ((line[0], int(line[1:])) for line in data.splitlines())

    shippyBoi = Coordinate(x=0, y=0)
    wayPoint = Coordinate(x=10, y=1)

    for action, val in actions:
        if action == "W":
            wayPoint = wayPoint.west(val)
        elif action == "E":
            wayPoint = wayPoint.east(val)
        elif action == "S":
            wayPoint = wayPoint.south(val)
        elif action == "N":
            wayPoint = wayPoint.north(val)
        elif action == "F":
            shippyBoi += wayPoint * val
        elif action == "R":
            wayPoint = wayPoint.rotate(val)
        elif action == "L":
            wayPoint = wayPoint.rotate(-val)
        else:
            raise Exception("What the!?")
    return shippyBoi.manhattanDistance(Coordinate(0, 0))
