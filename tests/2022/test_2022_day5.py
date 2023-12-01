import aoc_cas.aoc2022.day5 as aoc

testData = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


def testPartA():
    assert aoc.part_a(testData) == "CMZ"


def testPartB():
    assert aoc.part_b(testData) == "MCD"
