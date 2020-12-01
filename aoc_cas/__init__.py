import runpy


def solve(day, year, data):
    moduleName = "aoc_cas.aoc{}.day{}".format(year, day)
    mod = runpy.importlib.import_module(moduleName)
    part1 = mod.part1(data)
    part2 = mod.part2(data)
    return part1, part2
