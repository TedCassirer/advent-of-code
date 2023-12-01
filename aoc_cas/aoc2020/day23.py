from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    __slots__ = "val", "next"
    val: int
    next: Any


def cupGame(numbers, rounds):
    N = max(numbers)
    first = Node(val=numbers[0], next=None)
    prev = first
    cups = {numbers[0]: first}
    for n in numbers[1:]:
        node = Node(val=n, next=None)
        cups[n] = node
        prev.next, prev = node, node
    prev.next = first
    currentCup = first

    for _ in range(rounds):
        a = currentCup.next
        b = a.next
        c = b.next
        target = (currentCup.val - 2) % N + 1
        while (targetCup := cups[target]).val in {a.val, b.val, c.val}:
            target = (target - 2) % N + 1

        currentCup.next = c.next
        c.next = targetCup.next
        targetCup.next = a
        currentCup = currentCup.next

    return cups


def part1(data):
    numbers = [int(n) for n in data]
    cups = cupGame(numbers, 100)

    result = 0
    start = cups[1]
    current = start.next
    while current != start:
        result = 10 * result + current.val
        current = current.next
    return result


def part2(data):
    numbers = [int(n) for n in data]
    numbers += list(range(max(numbers) + 1, 1000001))
    cups = cupGame(numbers, 10000000)

    return cups[1].next.val * cups[1].next.next.val
