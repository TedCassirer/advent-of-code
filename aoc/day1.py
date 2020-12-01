from aocd import get_data


def getExpenses(data):
    return [int(e.strip()) for e in data.strip().split("\n")]


def findPairSum(expenses, target):
    expenses = set(expenses)
    for e in expenses:
        if target - e in expenses:
            return e, target - e


def part1(data):
    n1, n2 = findPairSum(getExpenses(data), 2020)
    return n1 * n2


def part2(data):
    expenses = set(getExpenses(data))
    for e1 in expenses:
        target = 2020 - e1
        res = findPairSum(expenses - {e1}, target)
        if res:
            e2, e3 = res
            return e1 * e2 * e3


if __name__ == "__main__":
    data = get_data(day=1, year=2020)
    print(part1(data))
    print(part2(data))
