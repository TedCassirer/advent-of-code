import aoc_cas.aoc2020.day5 as aoc


def testSeatId():
    assert aoc.seatId("FBFBBFFRLR") == 357
    assert aoc.seatId("BFFFBBFRRR") == 567
    assert aoc.seatId("FFFBBBFRRR") == 119
    assert aoc.seatId("BBFFBBFRLL") == 820
