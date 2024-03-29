from aoc_cas.aoc2020 import day10 as aoc


data = """
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
""".strip()


def testPartA():
    assert aoc.part_a(data) == 220


def testPartB():
    assert aoc.part_b(data) == 19208
