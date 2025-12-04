from __future__ import annotations

from typing import Optional

from utils import readData, timeIt


class LinkedNode:
    def __init__(self, value: int):
        self.value = value
        self.prev: Optional["LinkedNode"] = None
        self.next: Optional["LinkedNode"] = None

    def remove(self):
        if self.prev is None or self.next is None:
            raise RuntimeError("Cannot remove a detached node")
        prev = self.prev
        prev.next = self.next
        self.next.prev = prev

    def insertAfter(self, node: "LinkedNode"):
        if self.next is None:
            raise RuntimeError("Node is not linked")
        node.prev = self
        node.next = self.next
        self.next.prev = node
        self.next = node

    def __repr__(self):
        return str(self.value)


class GameBoard:
    def __init__(self):
        self.currentMarble = LinkedNode(0)
        self.currentMarble.next = self.currentMarble
        self.currentMarble.prev = self.currentMarble
        self.head = self.currentMarble

    def placeMarble(self, value):
        if value % 23 == 0:
            for _ in range(6):
                assert self.currentMarble.prev is not None
                self.currentMarble = self.currentMarble.prev
            assert self.currentMarble.prev is not None
            score = value + self.currentMarble.prev.value
            self.currentMarble.prev.remove()
        else:
            newMarble = LinkedNode(value)
            assert self.currentMarble.next is not None
            self.currentMarble.next.insertAfter(newMarble)
            self.currentMarble = newMarble
            score = 0
        return score

    def __repr__(self):
        current = self.head
        res = []
        while True:
            res.append(current.value)
            next_node = current.next
            if next_node is None or next_node == self.head:
                break
            current = next_node
        return str(self.currentMarble.value) + " | " + str(res)


@timeIt
def part_a():
    line = next(readData("2018/data/day_9")).split(" ")
    playerCount, lastMarble = int(line[0]), int(line[-2])
    players = [0] * playerCount
    currentMarble = 1
    board = GameBoard()
    while currentMarble <= lastMarble:
        for pi in range(playerCount):
            players[pi] += board.placeMarble(currentMarble)
            currentMarble += 1
            if currentMarble > lastMarble:
                break
    return max(players)


@timeIt
def part_b():
    line = next(readData("2018/data/day_9")).split(" ")
    playerCount, lastMarble = int(line[0]), int(line[-2])
    lastMarble *= 100
    players = [0] * playerCount
    currentMarble = 1
    board = GameBoard()
    while currentMarble <= lastMarble:
        for pi in range(playerCount):
            players[pi] += board.placeMarble(currentMarble)
            currentMarble += 1
            if currentMarble > lastMarble:
                break
    return max(players)


if __name__ == "__main__":
    print("Part A:", part_a())
    print("Part B:", part_b())
