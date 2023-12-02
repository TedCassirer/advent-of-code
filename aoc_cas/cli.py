from datetime import datetime
from pathlib import Path

import click
from aocd.models import Puzzle
from aocd.utils import AOC_TZ

from . import plugin


@click.group()
def main():
    ...


@main.command()
@click.option("--year", "-y", default=datetime.now(tz=AOC_TZ).year, type=int)
@click.option("--day", "-d", default=datetime.now(tz=AOC_TZ).day, type=int)
@click.option("--submit", "-s", is_flag=True)
def solve(year: int, day: int, submit: bool) -> None:
    puzzle = Puzzle(year, day)
    print(f"--- {year} Day {day}: {puzzle.title} ---")
    part_a_result, part_b_result = plugin(year=year, day=day, data=puzzle.input_data)
    print(f"PartA: {part_a_result}")
    print(f"PartB: {part_b_result}")
    if submit:
        puzzle.answer_a = part_a_result
        puzzle.answer_b = part_b_result


@main.command()
@click.option("--year", "-y", default=datetime.now(tz=AOC_TZ).year, type=int)
@click.option("--day", "-d", default=datetime.now(tz=AOC_TZ).day, type=int)
def init_challenge(year: int, day: int) -> None:
    year_folder = Path.cwd() / "aoc_cas" / f"aoc{year}"
    challenge_template = (Path.cwd() / "challenge_template.txt").read_text()
    if not year_folder.exists():
        year_folder.mkdir()
        year_folder.joinpath("__init__.py").touch()
        print(f"Generated a new year folder: {year_folder}")
    python_file = year_folder / f"day{day}.py"
    if not python_file.exists():
        python_file.write_text(challenge_template.format(day=day, year=year))
        print(f"Generated a new solution file at: {python_file}")

    test_folder = Path.cwd() / f"tests/fixtures/{year}"
    test_folder.mkdir(exist_ok=True)
    test_folder.joinpath(f"{day}.txt").touch()
