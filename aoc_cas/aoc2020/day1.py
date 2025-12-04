def getExpenses(data):
    return [int(e.strip()) for e in data.strip().split("\n")]


def findPairSum(expenses, target) -> tuple[int, int] | None:
    seen = set()
    for e in expenses:
        if target - e in seen:
            return e, target - e
        seen.add(e)


def part_a(data):
    pair_sum = findPairSum(getExpenses(data), 2020)
    if pair_sum is None:
        raise ValueError("No valid pair found")
    n1, n2 = pair_sum
    return n1 * n2


def part_b(data):
    expenses = getExpenses(data)
    for i, e1 in enumerate(expenses):
        target = 2020 - e1
        res = findPairSum(expenses[i + 1 :], target)
        if res:
            e2, e3 = res
            return e1 * e2 * e3
