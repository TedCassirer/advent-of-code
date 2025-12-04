import re
from dataclasses import dataclass
from itertools import combinations, product
import heapq
from functools import lru_cache


@lru_cache(None)
def estimate(e, itemsOnFloors):
    dist = e - 3
    itemsOnFloors = list(itemsOnFloors)
    itemsOnFloors[e] -= 1
    floorsWithItems = [i for i, v in enumerate(itemsOnFloors) if v > 0]
    for floor in floorsWithItems:
        if floor == 3:
            break
        n = itemsOnFloors[floor]
        toTop = 3 - floor
        dist += n * toTop * 2
    return dist


@dataclass(frozen=True)
class State:
    elevator: int
    chips: tuple[frozenset[str], ...]
    generators: tuple[frozenset[str], ...]
    steps: int = 0

    def isValid(self):
        for chips, generators in zip(self.chips, self.generators):
            if generators and not generators.issuperset(chips):
                return False

        return True

    def goal(self):
        for i in range(3):
            if self.chips[i] or self.generators[i]:
                return False
        return True

    def moves(self):
        floors = [i for i in [self.elevator - 1, self.elevator + 1] if 0 <= i < 4]
        for floor in (f for f in floors):
            for c in (2, 1):
                for chipsToMove in combinations(self.chips[self.elevator], c):
                    chips = list(self.chips)
                    chipsToMove = set(chipsToMove)
                    chips[self.elevator] -= chipsToMove
                    chips[floor] |= chipsToMove
                    state = State(
                        elevator=floor,
                        chips=tuple(chips),
                        generators=self.generators,
                        steps=self.steps + 1,
                    )
                    if state.isValid():
                        yield state
                for generatorsToMove in combinations(self.generators[self.elevator], c):
                    generators = list(self.generators)
                    generatorsToMove = set(generatorsToMove)
                    generators[self.elevator] -= generatorsToMove
                    generators[floor] |= generatorsToMove
                    state = State(
                        elevator=floor,
                        chips=self.chips,
                        generators=tuple(generators),
                        steps=self.steps + 1,
                    )
                    if state.isValid():
                        yield state

            for chipToMove, generatorToMove in product(self.chips[self.elevator], self.generators[self.elevator]):
                generators = list(self.generators)
                generators[self.elevator] -= {generatorToMove}
                generators[floor] |= {generatorToMove}
                chips = list(self.chips)
                chips[self.elevator] -= {chipToMove}
                chips[floor] |= {chipToMove}
                state = State(
                    elevator=floor,
                    chips=tuple(chips),
                    generators=tuple(generators),
                    steps=self.steps + 1,
                )
                if state.isValid():
                    yield state

        # for floor in (f for f in floors if f < self.elevator):
        #     for chipsToMove in combinations(self.chips[self.elevator], 1):
        #         chips = list(self.chips)
        #         chipsToMove = set(chipsToMove)
        #         chips[self.elevator] -= chipsToMove
        #         chips[floor] |= chipsToMove
        #         state = State(elevator=floor, chips=tuple(chips), generators=self.generators, steps=self.steps + 1)
        #         if state.isValid():
        #             yield state
        #             break
        #     for generatorsToMove in combinations(self.generators[self.elevator], 1):
        #         generators = list(self.generators)
        #         generatorsToMove = set(generatorsToMove)
        #         generators[self.elevator] -= generatorsToMove
        #         generators[floor] |= generatorsToMove
        #         state = State(elevator=floor, chips=self.chips, generators=tuple(generators), steps=self.steps + 1)
        #         if state.isValid():
        #             yield state
        #             break

    @lru_cache(None)
    def est(self):
        return estimate(
            self.elevator,
            tuple(len(self.chips[i]) + len(self.generators[i]) for i in range(4)),
        )

    def __hash__(self):
        return hash((self.elevator, self.chips, self.generators))

    def __lt__(self, other):
        return self.steps + self.est() < other.steps + other.est()

    def __repr__(self):
        out = ""
        for i in range(3, -1, -1):
            out += "F" + str(i) + " "
            out += "E" if i == self.elevator else " "
            out += " "
            out += " ".join("C" + s[:3] for s in sorted(self.chips[i]))
            out += "\t"
            out += " ".join("G" + s[:3] for s in sorted(self.generators[i]))
            out += "\n"
        return out


def getState(data):
    chips = []
    generators = []
    for line in data.splitlines():
        generators.append(frozenset(re.findall(r" (\w+) generator", line)))
        chips.append(frozenset(re.findall(r" (\w+)-compatible microchip", line)))
    return State(0, tuple(chips), tuple(generators))


def search(start):
    seen = set()
    queue = [start]
    while queue:
        curr = heapq.heappop(queue)
        if hash(curr) in seen:
            continue
        if curr.goal():
            print(len(seen))
            return curr.steps
        seen.add(hash(curr))
        for nxt in curr.moves():
            heapq.heappush(queue, nxt)


def part_a(data):
    state = getState(data)
    return search(state)


def part_b(data):
    return
    extraStuff = {"elerium", "dilithium"}
    state = getState(data)
    chips = list(state.chips)
    chips[0] |= extraStuff
    generators = list(state.generators)
    generators[0] |= extraStuff
    state = State(elevator=1, chips=tuple(chips), generators=tuple(generators))

    return search(state)


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2016, day=11)
    # data = """
    # The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
    # The second floor contains a hydrogen generator.
    # The third floor contains a lithium generator.
    # The fourth floor contains nothing relevant.
    # """.strip()
    print(part_a(data))
    print(part_b(data))
