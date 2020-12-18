from operator import add, mul
import math


def evaluate(expr, part2=False):
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
            if part2:
                parts.append(res)
                res = 1
        elif token == "(":
            res = op(res, evaluate(expr, part2))
        elif token == ")":
            break
        else:
            raise ValueError(f"What the!? {token}")
    parts.append(res)
    return math.prod(parts)


def part1(data):
    return sum(evaluate(iter(e.replace(" ", ""))) for e in data.splitlines())


def part2(data):
    return sum(evaluate(iter(e.replace(" ", "")), part2=True) for e in data.splitlines())
