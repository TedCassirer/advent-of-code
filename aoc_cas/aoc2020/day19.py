from functools import lru_cache


def validate(rules, message):
    @lru_cache(None)
    def inner(message, rule):
        groups = rule.split(" | ")
        if len(groups) > 1:
            offsets = []
            for group in groups:
                offsets.extend(inner(message, group))
            return offsets
        elif rule.startswith('"'):
            return [1] if message[:1] == rule[1] else []
        else:
            offsets = [0]
            for r in rule.split():
                expandedRule = rules[int(r)]
                offsets = [o + offset for offset in offsets for o in inner(message[offset:], expandedRule)]
            return offsets

    return len(message) in inner(message, rules[0])


def part_a(data):
    rulesData, messages = data.split("\n\n")
    rules = {}
    for rule in rulesData.splitlines():
        id, parts = rule.split(": ")
        rules[int(id)] = parts
    validMessages = [m for m in messages.splitlines() if validate(rules, m)]
    return len(validMessages)


def part_b(data):
    rulesData, messages = data.split("\n\n")
    rules = {}
    for rule in rulesData.splitlines():
        id, parts = rule.split(": ")
        rules[int(id)] = parts
    rules[8] = "42 | 42 8"
    rules[11] = "42 31 | 42 11 31"

    validMessages = [m for m in messages.splitlines() if validate(rules, m)]
    return len(validMessages)


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2020, day=19)
    print(part_b(data))
