def deriv(f):
    def g(x):
        fc1, fc2 = f(x), f(x + 1)
        if fc1 > fc2:
            return -1
        elif fc1 == fc2:
            return 0
        else:
            return 1

    return g


def binarySearch(f, lo, hi):
    while lo != hi - 1:
        mid = (lo + hi) // 2
        r = f(mid)
        if r == -1:
            lo = mid
        elif r == 1:
            hi = mid
        else:
            return mid
    return hi


def part_a(data):
    positions = [*map(int, data.split(","))]
    fuelCost = lambda x: sum(abs(p - x) for p in positions)

    lo, hi = min(positions), max(positions)
    optimalPosition = binarySearch(deriv(fuelCost), lo, hi)
    return fuelCost(optimalPosition)


def part_b(data):
    def fuelCostFunction(position):
        def f(x):
            d = abs(position - x)
            return d * (d + 1) / 2

        return f

    positions = [*map(int, data.split(","))]
    fuelCosts = [*map(fuelCostFunction, positions)]
    fuelCost = lambda x: int(sum(f(x) for f in fuelCosts))

    lo, hi = min(positions), max(positions)
    optimalPosition = binarySearch(deriv(fuelCost), lo, hi)
    return fuelCost(optimalPosition)


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2021, day=7)

    print(part_a(data))
    print(part_b(data))
