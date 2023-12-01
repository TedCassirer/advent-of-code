import importlib

from aocd import get_data


def plugin(year, day, **kwargs):
    module_name = f"aoc_cas.aoc{year}.day{day}"
    mod = importlib.import_module(module_name)
    data = get_data(year=year, day=day)
    return mod.part1(data), mod.part2(data)
