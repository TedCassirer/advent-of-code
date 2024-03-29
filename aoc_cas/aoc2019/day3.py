class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__coord = (self.x, self.y)

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)

    def __hash__(self):
        return hash(self.__coord)

    def __eq__(self, other):
        return self.__coord == other.__coord


directions = {
    "U": Coordinate(0, 1),
    "D": Coordinate(0, -1),
    "R": Coordinate(1, 0),
    "L": Coordinate(-1, 0),
}


def get_input(data):
    for line in data.split("\n"):
        yield [(c[0], int(c[1:])) for c in line.split(",")]


def get_line(movements):
    current = Coordinate(0, 0)
    for d, steps in movements:
        direction = directions[d]
        for _ in range(steps):
            current += direction
            yield current


def part_a(data):
    lines = [set(get_line(movements)) for movements in get_input(data)]
    crossings = set.intersection(*lines)
    distance_from_start = map(lambda c: abs(c.x) + abs(c.y), crossings)
    return min(distance_from_start)


def part_b(data):
    lines = [{coord: step + 1 for step, coord in enumerate(get_line(movements))} for movements in get_input(data)]
    crossings = set.intersection(*(set(l.keys()) for l in lines))
    steps_to_crossing = (sum(l[c] for l in lines) for c in crossings)
    return min(steps_to_crossing)
