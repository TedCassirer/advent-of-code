import aoc_cas.aoc2022.day6 as aoc


def testPart1():
    assert aoc.part1("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
    assert aoc.part1("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert aoc.part1("nppdvjthqldpwncqszvftbrmjlhg") == 6
    assert aoc.part1("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert aoc.part1("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11


def testPart2():
    assert aoc.part2("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19
    assert aoc.part2("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23
    assert aoc.part2("nppdvjthqldpwncqszvftbrmjlhg") == 23
    assert aoc.part2("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 29
    assert aoc.part2("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 26
