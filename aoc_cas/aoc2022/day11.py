from dataclasses import dataclass
from collections.abc import Callable
from functools import reduce


def parseOp(t1, t2, t3):
    def getVal(old, token):
        if token == "old":
            return old
        else:
            return int(token)

    ops = {
        "-": int.__sub__,
        "+": int.__add__,
        "*": int.__mul__,
    }

    return lambda old: ops[t2](getVal(old, t1), getVal(old, t3))


@dataclass
class Monkey:
    id: int
    operation: Callable[[int], int]
    items: list[int]
    test: Callable[[int], int]
    div: int
    inspections: int = 0

    @staticmethod
    def parseMonkey(monkeyStuff):
        idLine, itemsLine, operationLine, testLine, ifTrueLine, ifFalseLine = monkeyStuff.splitlines()

        id = int(idLine[7:-1])

        _, itemsStr = itemsLine.split(": ")
        items = [int(item) for item in itemsStr.split(", ")]

        _, opStr = operationLine.split(" = ")
        tokens = opStr.split(" ")
        operation = parseOp(*tokens)

        testDiv = int(testLine[21:])
        ifTrue = int(ifTrueLine[29:])
        ifFalse = int(ifFalseLine[30:])
        test = lambda v: ifTrue if v % testDiv == 0 else ifFalse

        return Monkey(id=id, operation=operation, test=test, items=items, div=testDiv)

    def inspectItems(self, worryDiv):
        for old in self.items:
            new = self.operation(old) // worryDiv
            yield self.test(new), new
        self.inspections += len(self.items)
        self.items.clear()


def part_a(data):
    monkeyData = data.split("\n\n")
    monkeys = [Monkey.parseMonkey(md) for md in monkeyData]
    for round in range(20):
        for monkey in monkeys:
            for throwTo, item in monkey.inspectItems(3):
                monkeys[throwTo].items.append(item)

    monkeys.sort(key=lambda m: m.inspections)
    m1, m2 = monkeys[-2:]
    return m1.inspections * m2.inspections


def part_b(data):
    monkeyData = data.split("\n\n")
    monkeys = [Monkey.parseMonkey(md) for md in monkeyData]
    modulo = reduce(lambda a, b: a * b, (m.div for m in monkeys))
    for round in range(10_000):
        for monkey in monkeys:
            for throwTo, item in monkey.inspectItems(1):
                monkeys[throwTo].items.append(item % modulo)
    monkeys.sort(key=lambda m: m.inspections)
    m1, m2 = monkeys[-2:]
    return m1.inspections * m2.inspections


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2022, day=11)

    print(part_a(data))
    print(part_b(data))
