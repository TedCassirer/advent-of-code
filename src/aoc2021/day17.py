from math import sqrt, ceil


def getSquare(data):
    _, coords = data.split(": ")
    x, y = coords.split(", ")
    y, x = y[2:], x[2:]

    y2, y1 = [-int(n) for n in y.split("..")]
    x1, x2 = map(int, x.split(".."))
    return y1, x1, y2, x2


def trajectory(vy, vx):
    y, x = 0, 0
    yield y, x
    while True:
        y += vy
        x += vx
        vy += 1
        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1
        yield y, x


def hit(y, x, y1, x1, y2, x2):
    return y1 <= y <= y2 and x1 <= x <= x2


def part1(data):
    square = getSquare(data)
    y1, x1, y2, x2 = square
    minVx = ceil(-1 / 2 + sqrt(1 / 4 + 2 * x1))
    peakestPeak = 0
    for vy in range(0, -y2 - 1, -1):
        peak = ((-vy) * ((-vy) + 1)) // 2
        for vx in range(minVx, x2 + 1):
            for y, x in trajectory(vy, vx):
                if hit(y, x, *square):
                    peakestPeak = peak
                    break
                if y > y2 or x > x2:
                    break
            if peak == peakestPeak:
                break
    return peakestPeak


def part2(data):
    square = getSquare(data)
    y1, x1, y2, x2 = square
    minVx = ceil(-1 / 2 + sqrt(1 / 4 + 2 * x1))
    hits = set()
    for vy in range(y2, -y2 - 1, -1):
        for vx in range(minVx, x2 + 1):
            for y, x in trajectory(vy, vx):
                if hit(y, x, *square):
                    hits.add((vx, -vy))
                    break
                if y > y2 or x > x2:
                    break
    return len(hits)


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2021, day=17)

    print(part1(data))
    print(part2(data))
