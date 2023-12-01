import logging
from datetime import datetime

import click
from aocd.models import Puzzle
from aocd.utils import AOC_TZ

from . import plugin


@click.command()
@click.option("--year", "-y", default=datetime.now(tz=AOC_TZ).year, type=int)
@click.option("--day", "-d", default=datetime.now(tz=AOC_TZ).day, type=int)
@click.option("--submit", "-s", is_flag=True)
def run_one(year: int, day: int, submit: bool):
    logging.basicConfig(format="%(message)s", level=logging.INFO)

    puzzle = Puzzle(year, day)
    print(f"--- {year} Day {day}: {puzzle.title} ---")
    part_1_result, part_2_result = plugin(year, day)
    print(f"Part1: {part_1_result}")
    print(f"Part2: {part_2_result}")
    if submit:
        puzzle.answer_a = part_1_result
        puzzle.answer_2 = part_2_result
