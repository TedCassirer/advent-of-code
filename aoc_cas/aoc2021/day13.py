EMPTY = " "
DOT = "#"
Y_AXIS = 0
X_AXIS = 1


def printablePaper(paper):
    columns = max(x for y, x in paper) + 1
    rows = max(y for y, x in paper) + 1
    printable = [[EMPTY] * columns for _ in range(rows)]
    for y, x in paper:
        printable[y][x] = DOT
    return "\n".join("".join(line) for line in printable)


def fold(axis, index, paper):
    folded = set()
    for y, x in paper:
        if axis == Y_AXIS and y > index:
            folded.add((2 * index - y, x))
        elif axis == X_AXIS and x > index:
            folded.add((y, 2 * index - x))
        else:
            folded.add((y, x))
    return folded


def part1(data):
    dots, folds = data.split("\n\n")
    paper = set()
    for line in dots.splitlines():
        x, y = map(int, line.split(","))
        paper.add((y, x))

    axis, index = folds.splitlines()[0][11:].split("=")
    axis = X_AXIS if axis == "x" else Y_AXIS
    index = int(index)
    paper = fold(axis, index, paper)
    return len(paper)


def part2(data):
    dots, folds = data.split("\n\n")
    paper = set()
    for line in dots.splitlines():
        x, y = map(int, line.split(","))
        paper.add((y, x))

    for line in folds.splitlines():
        axis, index = line[11:].split("=")
        axis = X_AXIS if axis == "x" else Y_AXIS
        index = int(index)
        paper = fold(axis, index, paper)
    printable = printablePaper(paper)
    print(printable)
    expected = (
        """
###   ##  #  # ###  #  # #    #  # #   
#  # #  # #  # #  # # #  #    # #  #   
#  # #    #### #  # ##   #    ##   #   
###  # ## #  # ###  # #  #    # #  #   
#    #  # #  # # #  # #  #    # #  #   
#     ### #  # #  # #  # #### #  # ####
""".strip()
        .replace(" ", EMPTY)
        .replace("#", DOT)
    )
    if printable == expected:
        return "PGHRKLKL"
    else:
        return None


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2021, day=13)

    print(part1(data))
    print(part2(data))
