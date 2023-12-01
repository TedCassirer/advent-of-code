from aoc_cas.aoc2020 import day9 as aoc


data = """
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
""".strip()


def testPartA():
    numbers = [int(n) for n in data.splitlines()]
    assert numbers[aoc.findWeakness(numbers, 5)] == 127


def testPartB():
    numbers = [int(n) for n in data.splitlines()]
    assert aoc.findEncryptionWeakness(numbers, 5) == 62
