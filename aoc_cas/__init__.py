from .util import load_module


def plugin(year: int, day: int, data: str) -> tuple:
    mod = load_module(year, day)
    return mod.part_a(data), mod.part_b(data)
