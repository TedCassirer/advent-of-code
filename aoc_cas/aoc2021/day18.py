from __future__ import annotations

from functools import reduce
from itertools import permutations
from typing import Generator, Optional, Tuple


class Node:
    def __init__(self, val: Optional[int] = None, left: Optional["Node"] = None, right: Optional["Node"] = None):
        self.val = val
        self.left = left
        self.right = right
        self.parent: Optional["Node"] = None
        if self.left is not None:
            self.left.parent = self
        if self.right is not None:
            self.right.parent = self

    def copy(self) -> "Node":
        if self.isVal():
            return Node(val=self.val)
        else:
            assert self.left is not None and self.right is not None
            left = self.left.copy()
            right = self.right.copy()
            return Node(left=left, right=right)

    def isVal(self) -> bool:
        return self.val is not None

    def magnitude(self) -> int:
        if self.isVal():
            assert self.val is not None
            return self.val
        else:
            assert self.left is not None and self.right is not None
            return 3 * self.left.magnitude() + 2 * self.right.magnitude()

    def leftOf(self) -> Optional["Node"]:
        cur: Optional["Node"] = self
        while cur is not None and cur.parent is not None:
            parent = cur.parent
            if parent.right is cur:
                candidate = parent.left
                while candidate and candidate.right:
                    candidate = candidate.right
                if candidate is not None:
                    assert candidate.isVal()
                    return candidate
            cur = parent
        return None

    def rightOf(self) -> Optional["Node"]:
        cur: Optional["Node"] = self
        while cur is not None and cur.parent is not None:
            parent = cur.parent
            if parent.left is cur:
                candidate = parent.right
                while candidate and candidate.left:
                    candidate = candidate.left
                if candidate is not None:
                    assert candidate.isVal()
                    return candidate
            cur = parent
        return None

    def __add__(self, other: "Node") -> "Node":
        node = Node(left=self, right=other)
        self.parent = node
        other.parent = node
        return node.copy()

    def enumerate(self, depth: int = 0) -> Generator[Tuple["Node", int], None, None]:
        if self.isVal():
            yield self, depth
        else:
            assert self.left is not None and self.right is not None
            yield from self.left.enumerate(depth + 1)
            yield from self.right.enumerate(depth + 1)

    def split(self):
        assert self.isVal()
        assert self.val is not None and self.val >= 10
        leftVal = self.val // 2
        rightVal = leftVal + self.val % 2
        self.val = None
        self.left = Node(val=leftVal)
        self.left.parent = self
        self.right = Node(val=rightVal)
        self.right.parent = self

    def explode(self):
        assert not self.isVal()
        assert self.left is not None and self.left.isVal()
        assert self.right is not None and self.right.isVal()

        toLeft = self.leftOf()
        if toLeft and self.left.val is not None:
            assert toLeft.val is not None
            toLeft.val += self.left.val
        toRight = self.rightOf()
        if toRight and self.right.val is not None:
            assert toRight.val is not None
            toRight.val += self.right.val
        self.val = 0
        self.left = None
        self.right = None

    def reduce(self):
        for n, d in self.enumerate():
            if d == 5:
                assert n.isVal()
                if n.parent is None:
                    raise RuntimeError("Malformed tree without parent")
                n.parent.explode()
                self.reduce()
                return self
        for n, d in self.enumerate():
            if n.val is not None and n.val >= 10:
                n.split()
                self.reduce()
                return self
        return self

    def __repr__(self):
        if self.isVal():
            return str(self.val)
        return f"[{self.left},{self.right}]"


def parse(nodeData) -> Node:
    if isinstance(nodeData, int):
        return Node(val=nodeData)
    else:
        return Node(left=parse(nodeData[0]), right=parse(nodeData[1]))


def part_a(data):
    nodes = map(parse, map(eval, data.splitlines()))
    sumNode = reduce(lambda n1, n2: (n1 + n2).reduce(), nodes)
    return sumNode.magnitude()


def part_b(data):
    nodes = [parse(eval(line)) for line in data.splitlines()]
    return max((n1 + n2).reduce().magnitude() for n1, n2 in permutations(nodes, 2))


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2021, day=18)

    print(part_a(data))
    print(part_b(data))
