def getData(loop=False):
    while True:
        with open("2018/data/day1") as data:
            yield from data
        if not loop:
            break


def part_a():
    return sum(map(int, getData()))


def part_b():
    seen = {0}
    currentFrequency = 0
    for frequency in map(int, getData(True)):
        currentFrequency += frequency
        if currentFrequency in seen:
            return currentFrequency
        else:
            seen.add(currentFrequency)


if __name__ == "__main__":
    print("Part A:", part_a())
    print("Part B:", part_b())
