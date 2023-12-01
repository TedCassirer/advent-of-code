def getFuel(data):
    return [int(s) for s in data.split("\n")]


def fuelbois(n):
    return (n // 3) - 2


def part_a(data):
    return sum(map(fuelbois, getFuel(data)))


def part_b(data):
    return sum(map(doTheThing, getFuel(data)))


def doTheThing(n):
    s = fuelbois(n)
    if s <= 0:
        return 0
    return s + doTheThing(s)
