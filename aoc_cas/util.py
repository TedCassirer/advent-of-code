import importlib

from aocd.models import Puzzle


def load_module(year: int, day: int):
    module_name = f"aoc_cas.aoc{year}.day{day}"
    return importlib.import_module(module_name)


def test_with_examples(year: int, day: int) -> None:
    mod = load_module(year, day)
    puzzle = Puzzle(year, day)
    print(f"Testing example data")
    for example in puzzle.examples:
        print(f"\n{example.input_data}\n")
        if example.answer_a is not None:
            part_a_result = str(mod.part_a(example.input_data))
            correct = part_a_result == example.answer_a
            print(f"{'❌✅'[correct]} [Part A] Actual: {part_a_result} - Expected: {example.answer_a}")
        if example.answer_b is not None:
            part_b_result = mod.part_b(example.input_data)
            correct = part_b_result == example.answer_a
            print(f"{'❌✅'[correct]} [Part B] Actual: {part_b_result} - Expected: {example.answer_b}\n")
