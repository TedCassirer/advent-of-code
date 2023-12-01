def seatId(seating, binRepr=str.maketrans("BRFL", "1100")):
    return int(seating.translate(binRepr), 2)


def part_a(data):
    return max(map(seatId, data.splitlines()))


def part_b(data):
    seats = [seatId(seating) for seating in data.splitlines()]
    return sum(range(min(seats), max(seats) + 1)) - sum(seats)
