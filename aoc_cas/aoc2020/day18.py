from operator import add, mul
import math


def evaluate(expr, part_b=False):
    res = 0
    parts = []
    op = add
    for token in expr:
        if token.isdigit():
            res = op(res, int(token))
        elif token == "+":
            op = add
        elif token == "*":
            op = mul
            if part_b:
                parts.append(res)
                res = 1
        elif token == "(":
            res = op(res, evaluate(expr, part_b))
        elif token == ")":
            break
        else:
            raise ValueError(f"What the!? {token}")
    parts.append(res)
    return math.prod(parts)


def part_a(data):
    return sum(evaluate(iter(e.replace(" ", ""))) for e in data.splitlines())


def part_b(data):
    return sum(evaluate(iter(e.replace(" ", "")), part_b=True) for e in data.splitlines())
