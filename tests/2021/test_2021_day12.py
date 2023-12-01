import aoc2021.day12 as aoc

testData1 = """
start-A
start-b
A-c
A-b
b-d
A-end
b-end
""".strip()

testData2 = """
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
""".strip()

testData3 = """
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
""".strip()


def testPart1():
    assert aoc.part1(testData1) == 10
    assert aoc.part1(testData2) == 19
    assert aoc.part1(testData3) == 226


def testPart2():
    assert aoc.part2(testData1) == 36
    assert aoc.part2(testData2) == 103
    assert aoc.part2(testData3) == 3509
