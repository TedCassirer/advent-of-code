from .common import readFile


def part1(inputLines):
    print(inputLines)
    return len(inputLines)


def part2(inputLines):
    pass


if __name__ == "__main__":
    inputLines = readFile("data/day1.txt")
    print(part1(inputLines))
    print(part2(inputLines))
