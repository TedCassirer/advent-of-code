from collections import defaultdict


def parse_game(line: str) -> tuple[int, int]:
    line = line.replace("  ", " ")
    card_id, board = line.split(": ")
    winning_nums_str, owned_nums_str = board.split(" | ")
    winning_nums = set(winning_nums_str.split(" "))
    owned_nums = set(owned_nums_str.split(" "))
    return int(card_id[card_id.find(" ") + 1 :]), len(winning_nums & owned_nums)


def part_a(data: str) -> int:
    result = 0
    for _, winning_nums in map(parse_game, data.splitlines()):
        result += int(2 ** (winning_nums - 1))
    return result


def part_b(data: str) -> int:
    num_cards = defaultdict(int)
    for card_id, winning_nums in map(parse_game, data.splitlines()):
        num_cards[card_id] += 1
        for extra_card in range(card_id + 1, card_id + winning_nums + 1):
            num_cards[extra_card] += num_cards[card_id]
    return sum(num_cards.values())


if __name__ == "__main__":
    from aoc_cas.util import solve_with_examples

    solve_with_examples(year=2023, day=4)
