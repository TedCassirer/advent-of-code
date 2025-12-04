import dataclasses
from collections import Counter
from functools import cache
from typing import Iterator

HIGH_CARD_A: dict[str, int] = {
    c: i for i, c in enumerate(["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"])
}
HIGH_CARD_B: dict[str, int] = {
    c: i for i, c in enumerate(["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"])
}


def hand_strength(matching_label_count: list[int]) -> int:
    match matching_label_count:
        case [5]:
            return 0
        case [1, 4]:
            return 1
        case [2, 3]:
            return 2
        case [1, 1, 3]:
            return 3
        case [1, 2, 2]:
            return 4
        case [1, 1, 1, 2]:
            return 5
        case [1, 1, 1, 1, 1]:
            return 6
    raise ValueError(matching_label_count)


@dataclasses.dataclass(frozen=True)
class Hand:
    cards: tuple[str, ...]
    bid: int

    @cache
    def part_a_cmp(self) -> tuple[int, tuple[int, ...]]:
        matching_label_count = sorted(Counter(self.cards).values())
        strength = hand_strength(matching_label_count)
        high_card = tuple(HIGH_CARD_A[c] for c in self.cards)
        return strength, high_card

    @cache
    def part_b_cmp(self) -> tuple[int, tuple[int, ...]]:
        count = Counter(self.cards)
        joker_count = count.pop("J", 0)
        matching_label_count = sorted(count.values())
        if joker_count == 5:
            matching_label_count = [5]
        else:
            matching_label_count[-1] += joker_count
        strength = hand_strength(matching_label_count)
        high_card = tuple(HIGH_CARD_B[c] for c in self.cards)
        return strength, high_card


def parse(data: str) -> Iterator[Hand]:
    for line in data.splitlines():
        cards, bid = line.split(" ")
        yield Hand(cards=tuple(cards), bid=int(bid))


def part_a(data: str) -> int:
    hands = sorted(parse(data), key=Hand.part_a_cmp, reverse=True)
    result = 0
    for rank, hand in enumerate(hands, start=1):
        result += rank * hand.bid
    return result


def part_b(data: str) -> int:
    hands = sorted(parse(data), key=Hand.part_b_cmp, reverse=True)
    result = 0
    for rank, hand in enumerate(hands, start=1):
        result += rank * hand.bid
    return result


if __name__ == "__main__":
    from aoc_cas.util import solve_with_example_input

    solve_with_example_input(year=2023, day=7)
