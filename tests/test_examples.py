import pathlib

import pytest

from aoc_cas.util import load_module

here = pathlib.Path(__file__).parent.resolve()
input_files = sorted(here.glob("fixtures/20*/*.txt"))


def path2id(input_file: pathlib.Path) -> str:
    *pre, year, file_name = input_file.parts
    return f"{year=} - {file_name=}"


@pytest.mark.parametrize("input_file", input_files, ids=path2id)
def test_examples(input_file: pathlib.Path) -> None:
    *pre, year, fname = input_file.parts
    year = int(year)
    day = int(fname[:-4])
    groups = input_file.read_text(encoding="utf-8").split("\n===\n")
    for group in groups:
        lines = group.splitlines()
        if len(lines) < 3:
            pytest.fail(f"test data {input_file} is malformed")
        *lines, expected_answer_a, expected_answer_b = lines
        input_data = "\n".join(lines)
        mod = load_module(year, day)
        if expected_answer_a != "-":
            actual_answer_a = str(mod.part_a(input_data))
            assert actual_answer_a == expected_answer_a, f"{actual_answer_a=} {expected_answer_a=}"
        if expected_answer_b != "-":
            actual_answer_b = str(mod.part_b(input_data))
            assert actual_answer_b == expected_answer_b, f"{actual_answer_b=} {expected_answer_b=}"
