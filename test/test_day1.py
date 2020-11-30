import sys

import pytest
from aoc import day1, common


def testPart1():
    res = day1.part1(common.readFile("data/day1.txt"))
    print(res)
