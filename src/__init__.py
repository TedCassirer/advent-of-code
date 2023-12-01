import importlib


def solve(day, year, data):
    moduleName = "aoc{}.day{}".format(year, day)
    mod = importlib.import_module(moduleName)
    part1 = mod.part1(data)
    part2 = mod.part2(data)
    return part1, part2
