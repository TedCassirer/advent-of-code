import importlib
import pathlib

import pytest


here = pathlib.Path(__file__).parent
input_files = sorted(here.glob("fixtures/20*/*/*.txt"))


def path2id(input_file):
    *pre, year, day, fname = input_file.parts
    return f"{year} - {day} - {fname}"


def remove_trailing_comments(lines):
    while lines and (not lines[-1].strip() or lines[-1].startswith("#")):
        lines.pop()
    if len(lines):
        lines[-1] = lines[-1].split("#")[0].strip()
    if len(lines) > 1:
        lines[-2] = lines[-2].split("#")[0].strip()


@pytest.mark.parametrize("input_file", input_files, ids=path2id)
def test_example(input_file, request):
    *pre, year, day, fname = input_file.parts
    year = int(year)
    day = int(day)
    lines = input_file.read_text(encoding="utf-8").splitlines()
    remove_trailing_comments(lines)
    if len(lines) < 3:
        pytest.fail(f"test data {input_file} is malformed")
    *lines, expected_answer_a, expected_answer_b = lines
    input_data = "\n".join(lines).rstrip()
    module_name = f"aoc_cas.aoc{year}.day{day}"
    mod = importlib.import_module(module_name)
    if expected_answer_a != "-":
        actual_answer_a = str(mod.part1(input_data))
        assert actual_answer_a == expected_answer_a, f"{actual_answer_a=} {expected_answer_a=}"
    if expected_answer_b != "-":
        actual_answer_b = str(mod.part2(input_data))
        assert actual_answer_b == expected_answer_b, f"{actual_answer_b=} {expected_answer_b=}"



