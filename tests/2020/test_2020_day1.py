import aoc_cas.aoc2020.day1 as aoc

testData1 = """
    1721
    979
    366
    299
    675
    1456
""".strip()


def testPartA():
    assert aoc.part_a(testData1) == 514579


def testPartB():
    assert aoc.part_b(testData1) == 241861950
