from aoc_cas.aoc2019 import day22 as aoc


def testPart1():
    data = """deal with increment 7
deal into new stack
deal into new stack"""
    assert aoc.doTheThing(list(range(10)), data.splitlines()) == [
        0,
        3,
        6,
        9,
        2,
        5,
        8,
        1,
        4,
        7,
    ]

    data = """deal into new stack
cut -2
deal with increment 7
cut 8
cut -4
deal with increment 7
cut 3
deal with increment 9
deal with increment 3
cut -1"""
    assert aoc.doTheThing(list(range(10)), data.splitlines()) == [
        9,
        2,
        5,
        8,
        1,
        4,
        7,
        0,
        3,
        6,
    ]

    data = """deal with increment 7
deal with increment 9
cut -2"""
    assert aoc.doTheThing(list(range(10)), data.splitlines()) == [
        6,
        3,
        0,
        7,
        4,
        1,
        8,
        5,
        2,
        9,
    ]

    data = """cut 6
deal with increment 7
deal into new stack"""
    assert aoc.doTheThing(list(range(10)), data.splitlines()) == [
        3,
        0,
        7,
        4,
        1,
        8,
        5,
        2,
        9,
        6,
    ]
