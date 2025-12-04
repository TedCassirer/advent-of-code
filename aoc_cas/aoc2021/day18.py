from itertools import permutations
from functools import reduce


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = None
        if self.left:
            self.left.parent = self
            self.right.parent = self

    def copy(self):
        if self.isVal():
            return Node(val=self.val)
        else:
            left = self.left.copy()
            right = self.right.copy()
            return Node(left=left, right=right)

    def isVal(self):
        return self.val is not None

    def magnitude(self):
        if self.isVal():
            return self.val
        else:
            return 3 * self.left.magnitude() + 2 * self.right.magnitude()

    def leftOf(self):
        cur = self
        while cur.parent:
            if cur.parent.right is cur:
                cur = cur.parent.left
                while cur.right:
                    cur = cur.right
                assert cur.isVal()
                return cur
            else:
                cur = cur.parent
        return None

    def rightOf(self):
        cur = self
        while cur.parent:
            if cur.parent.left is cur:
                cur = cur.parent.right
                while cur.left:
                    cur = cur.left
                assert cur.isVal()
                return cur
            else:
                cur = cur.parent
        return None

    def __add__(self, other):
        node = Node(left=self, right=other)
        self.parent = node
        other.parent = node
        return node.copy()

    def enumerate(self, depth=0):
        if self.isVal():
            yield self, depth
        else:
            yield from self.left.enumerate(depth + 1)
            yield from self.right.enumerate(depth + 1)

    def split(self):
        assert self.isVal()
        assert self.val >= 10
        leftVal = self.val // 2
        rightVal = leftVal + self.val % 2
        self.val = None
        self.left = Node(val=leftVal)
        self.left.parent = self
        self.right = Node(val=rightVal)
        self.right.parent = self

    def explode(self):
        assert not self.isVal()
        assert self.left.isVal()
        assert self.right.isVal()

        toLeft = self.leftOf()
        if toLeft:
            toLeft.val += self.left.val
        toRight = self.rightOf()
        if toRight:
            toRight.val += self.right.val
        self.val = 0
        self.left = None
        self.right = None

    def reduce(self):
        for n, d in self.enumerate():
            if d == 5:
                assert n.isVal()
                n.parent.explode()
                self.reduce()
                return self
        for n, d in self.enumerate():
            if n.val >= 10:
                n.split()
                self.reduce()
                return self
        return self

    def __repr__(self):
        if self.isVal():
            return str(self.val)
        return f"[{self.left},{self.right}]"


def parse(nodeData):
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
