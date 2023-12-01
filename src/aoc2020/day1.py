def getExpenses(data):
    return [int(e.strip()) for e in data.strip().split("\n")]


def findPairSum(expenses, target):
    seen = set()
    for e in expenses:
        if target - e in seen:
            return e, target - e
        seen.add(e)


def part1(data):
    n1, n2 = findPairSum(getExpenses(data), 2020)
    return n1 * n2


def part2(data):
    expenses = getExpenses(data)
    for i, e1 in enumerate(expenses):
        target = 2020 - e1
        res = findPairSum(expenses[i + 1 :], target)
        if res:
            e2, e3 = res
            return e1 * e2 * e3
