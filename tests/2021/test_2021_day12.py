import aoc_cas.aoc2021.day12 as aoc

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


def testPartA():
    assert aoc.part_a(testData1) == 10
    assert aoc.part_a(testData2) == 19
    assert aoc.part_a(testData3) == 226


def testPartB():
    assert aoc.part_b(testData1) == 36
    assert aoc.part_b(testData2) == 103
    assert aoc.part_b(testData3) == 3509
