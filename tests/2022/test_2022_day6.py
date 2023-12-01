import aoc_cas.aoc2022.day6 as aoc


def testPartA():
    assert aoc.part_a("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
    assert aoc.part_a("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert aoc.part_a("nppdvjthqldpwncqszvftbrmjlhg") == 6
    assert aoc.part_a("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert aoc.part_a("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11


def testPartB():
    assert aoc.part_b("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19
    assert aoc.part_b("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23
    assert aoc.part_b("nppdvjthqldpwncqszvftbrmjlhg") == 23
    assert aoc.part_b("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 29
    assert aoc.part_b("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 26
