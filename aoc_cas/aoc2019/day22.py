def cut(deck, n):
    return deck[n:] + deck[:n]


def dealWithIncrement(deck, N):
    newDeck = [None] * len(deck)
    for i in range(len(deck)):
        newDeck[(i * N) % len(deck)] = deck[i]
    return newDeck


def doTheThing(deck, instructions):
    for instruction in instructions:
        first, *middle, last = instruction.split(" ")
        if first == "cut":
            deck = cut(deck, int(last))
        elif first == "deal":
            if last == "stack":
                deck = list(reversed(deck))
            else:
                deck = dealWithIncrement(deck, int(last))
        else:
            raise Exception
    return deck


def trackTheThing(pos, deckSize, instructions):
    for instruction in instructions:
        first, *middle, last = instruction.split(" ")
        if first == "cut":
            pos = (pos - int(last)) % deckSize
        elif first == "deal":
            if last == "stack":
                pos = (~pos) % deckSize
            else:
                pos = (pos * int(last)) % deckSize
        else:
            raise Exception
    return pos


def part_a(data, decksize=10007):
    deck = list(range(decksize))
    deck = doTheThing(deck, data.splitlines())
    return deck.index(2019)


def part_b(data):
    deckSize = 119315717514047
    iterations = 101741582076661
    startPos = 2020
    pos = trackTheThing(startPos, deckSize, data.splitlines())
    shifted = pos - startPos
    totalShift = (startPos + shifted * iterations) % deckSize

    return totalShift


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2019, day=22)
    print(part_a(data))
    print(part_b(data))
