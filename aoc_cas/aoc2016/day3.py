import re


def parseDataRow(data):
    for line in data.splitlines():
        yield tuple(int(n) for n in re.findall(r"\d+", line))


def parseDataColumn(data):
    rowData = list(n for row in parseDataRow(data) for n in row)
    n1 = rowData[0::3]
    n2 = rowData[1::3]
    n3 = rowData[2::3]
    byColumn = n1 + n2 + n3
    return zip(byColumn[0::3], byColumn[1::3], byColumn[2::3])


def checkLengths(n1, n2, n3):
    return n1 + n2 > n3


def part_a(data):
    valid = 0
    for nums in parseDataRow(data):
        valid += checkLengths(*sorted(nums))
    return valid


def part_b(data):
    valid = 0
    for nums in parseDataColumn(data):
        valid += checkLengths(*sorted(nums))
    return valid


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2016, day=3)

    print(part_a(data))
    print(part_b(data))
