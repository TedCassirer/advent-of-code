def dayPassed(state):
    nextState = state[1:]
    nextState[6] += state[0]
    nextState.append(state[0])
    return nextState


def createInitialState(data):
    state = [0] * 9
    for n in map(int, data.split(",")):
        state[n] += 1
    return state


def part_a(data):
    state = createInitialState(data)
    for _ in range(80):
        state = dayPassed(state)

    return sum(state)


def part_b(data):
    state = createInitialState(data)
    for _ in range(256):
        state = dayPassed(state)

    return sum(state)


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2021, day=6)

    print(part_a(data))
    print(part_b(data))
