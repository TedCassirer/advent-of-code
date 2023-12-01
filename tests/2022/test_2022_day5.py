import aoc_cas.aoc2022.day5 as aoc

testData = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


def testPart1():
    assert aoc.part1(testData) == "CMZ"


def testPart2():
    assert aoc.part2(testData) == "MCD"
