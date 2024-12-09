import importlib

from aocd.models import Puzzle


def load_module(year: int, day: int):
    module_name = f"aoc_cas.aoc{year}.day{day}"
    return importlib.import_module(module_name)


def solve_with_real_input_data(year: int, day: int) -> None:
    puzzle = Puzzle(year, day)
    mod = load_module(year, day)
    part_a_result = str(mod.part_a(puzzle.input_data))
    part_b_result = str(mod.part_b(puzzle.input_data))

    print(f"\nReal data input\n")
    print(f"[Part A] {part_a_result}")
    print(f"[Part B] {part_b_result}")


def solve_with_example_input(year: int, day: int) -> None:
    puzzle = Puzzle(year, day)
    print(f"Testing example data")

    puzzle.prose0_path.unlink(missing_ok=True)
    for example in puzzle.examples:
        solve_with_input(year, day, example.input_data, answer_a=example.answer_a, answer_b=example.answer_b)


def solve_with_input(year: int, day: int, input_data: str, *, answer_a: object, answer_b: object = None) -> None:
    mod = load_module(year, day)
    print(f"\n{input_data}\n")
    if answer_a is not None:
        part_a_result = str(mod.part_a(input_data))
        correct = part_a_result == str(answer_a)
        print(f"{'❌✅'[correct]} [Part A] Actual: {part_a_result} - Expected: {answer_a}")
    if answer_b is not None:
        part_b_result = str(mod.part_b(input_data))
        correct = part_b_result == str(answer_b)
        print(f"{'❌✅'[correct]} [Part B] Actual: {part_b_result} - Expected: {answer_b}\n")
