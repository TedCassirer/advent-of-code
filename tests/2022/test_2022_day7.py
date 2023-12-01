import aoc_cas.aoc2022.day7 as aoc

testData = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
""".strip()


def testPartA():
    assert aoc.part_a(testData) == 95437


def testPartB():
    assert aoc.part_b(testData) == 24933642
