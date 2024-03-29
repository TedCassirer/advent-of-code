from aoc_cas.aoc2019 import day16 as aoc


def testPartA():
    data = "80871224585914546619083218645595"
    assert aoc.part_a(data) == "24176176"

    data = "19617804207202209144916044189917"
    assert aoc.part_a(data) == "73745418"

    data = "69317163492948606335995924319873"
    assert aoc.part_a(data) == "52432133"


def testPartB():
    data = "03036732577212944063491565474664"
    assert aoc.part_b(data) == "84462026"

    data = "02935109699940807407585447034323"
    assert aoc.part_b(data) == "78725270"

    data = "03081770884921959731165446850517"
    assert aoc.part_b(data) == "53553731"
