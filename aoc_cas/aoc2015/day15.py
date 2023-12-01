import numpy as np
from functools import lru_cache


@lru_cache(None)
def amounts(N, hi):
    if N == 1:
        return [[hi]]
    else:
        out = []
        for v1 in range(1, hi - N):
            p1 = [v1]
            for p2 in amounts(N - 1, hi - v1):
                out.append(p1 + p2)
        return out


def parse(line):
    return np.array([int(w.split(" ")[-1]) for w in line.split(", ")])


def part_a(data):
    ingredients = np.array([parse(line) for line in data.splitlines()]).T
    recipes = np.array(amounts(ingredients.shape[1], 100)).T
    cakes = np.matmul(ingredients, recipes)
    cakes[-1, :] = 1
    cakes = np.maximum(cakes, 0)
    return max(np.prod(cakes, 0))


def part_b(data):
    ingredients = np.array([parse(line) for line in data.splitlines()]).T
    recipes = np.array(amounts(ingredients.shape[1], 100)).T
    cakes = np.matmul(ingredients, recipes)
    cakes[-1, :] = cakes[-1, :] == 500
    cakes = np.maximum(cakes, 0)
    return max(np.prod(cakes, 0))


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2015, day=15)
    print(part_a(data))
    print(part_b(data))
