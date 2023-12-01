def part_a(data):
    count = 0
    for group in data.split("\n\n"):
        count += len(set(group.replace("\n", "")))
    return count


def part_b(data):
    count = 0
    for group in data.split("\n\n"):
        yesses = map(set, group.splitlines())
        count += len(set.intersection(*yesses))
    return count
