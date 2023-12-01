import importlib
import logging
from datetime import datetime

import click
from aocd import get_data
from aocd.models import Puzzle
from aocd.utils import AOC_TZ


def solve(day, year, data):
    moduleName = "aoc{}.day{}".format(year, day)
    mod = importlib.import_module(moduleName)
    part1 = mod.part1(data)
    part2 = mod.part2(data)
    return part1, part2


@click.command()
@click.option("--year", "-y", default=datetime.now(tz=AOC_TZ).year, type=int)
@click.option("--day", "-d", default=datetime.now(tz=AOC_TZ).day, type=int)
@click.option("--submit", "-s", is_flag=True)
def run_one(year: int, day: int, submit: bool):
    logging.basicConfig(format="%(message)s", level=logging.INFO)

    mod_name = "aoc_cas.aoc{}.day{}".format(year, day)
    print(mod_name)
    mod = importlib.import_module(mod_name)
    data = get_data(year=year, day=day)
    puzzle = Puzzle(year, day)
    print(f"--- {year} Day {day}: {puzzle.title} ---")
    part_1_result = mod.part1(data)
    part_2_result = mod.part2(data)
    print(f"Part1: {part_1_result}")
    print(f"Part2: {part_2_result}")
    if submit:
        puzzle.answer_a = part_1_result
        puzzle.answer_2 = part_2_result
