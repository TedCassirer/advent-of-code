import math


def traverse(forest, right, down):
    Y, X = len(forest), len(forest[0])
    xi = 0
    trees = 0
    for yi in range(0, Y, down):
        trees += forest[yi][xi] == "#"
        xi = (xi + right) % X
    return trees


def part_a(data):
    forest = data.split("\n")
    return traverse(forest, 3, 1)


def part_b(data):
    forest = data.split("\n")
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    return math.prod(traverse(forest, right, down) for right, down in slopes)
