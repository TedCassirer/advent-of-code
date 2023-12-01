import importlib
import pathlib

import pytest


here = pathlib.Path(__file__).parent.resolve()
input_files = sorted(here.glob("fixtures/20*/*.txt"))


def path2id(input_file) -> str:
    *pre, year, fname = input_file.parts
    return f"{year} - {fname[:-4]}"


@pytest.mark.parametrize("input_file", input_files, ids=path2id)
def test_examples(input_file) -> None:
    *pre, year, fname = input_file.parts
    year = int(year)
    day = int(fname[:-4])
    groups = input_file.read_text(encoding="utf-8").split("\n===\n")
    for group in groups:
        lines = group.splitlines()
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
