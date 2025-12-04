import re

ruleMatch = re.compile(r"(.+): (\d+-\d+) or (\d+-\d+)")


def parseRules(rules):
    allowedNumbers = []
    for r in rules.splitlines():
        match = ruleMatch.match(r)
        if not match:
            raise ValueError(f"Invalid rule: {r}")
        name, r1, r2 = match.groups()
        r1a, r1b = map(int, r1.split("-"))
        r2a, r2b = map(int, r2.split("-"))
        allowedNumbers.append((name, set(range(r1a, r1b + 1)) | set(range(r2a, r2b + 1))))
    return allowedNumbers


def part_a(data):
    rules, myTicket, nearbyTickets = data.split("\n\n")
    rules = parseRules(rules)
    allowedNumbers = set.union(*(r for name, r in rules))
    nearbyTickets = nearbyTickets.splitlines()[1:]
    result = 0

    for tickets in nearbyTickets:
        tickets = [int(t) for t in tickets.split(",")]
        result += sum(t for t in tickets if t not in allowedNumbers)

    return result


def part_b(data):
    rules, myTicket, nearbyTickets = data.split("\n\n")
    myTicket = [int(n) for n in myTicket.split("\n")[1].split(",")]
    rules = parseRules(rules)
    allowedNumbers = set.union(*(r for name, r in rules))

    nearbyTickets = nearbyTickets.splitlines()[1:]
    validTickets = []
    for tickets in nearbyTickets:
        tickets = [int(t) for t in tickets.split(",")]
        if all(t in allowedNumbers for t in tickets):
            validTickets.append(tickets)

    possibleRuleIndex = {name: set() for name, r in rules}
    for i, n in enumerate(zip(*validTickets)):
        for name, rule in rules:
            if all(t in rule for t in n):
                possibleRuleIndex[name].add(i)

    taken = set()
    res = 1
    for name, possible in sorted(possibleRuleIndex.items(), key=lambda r: len(r[1])):
        possible -= taken
        assert len(possible) == 1
        i = possible.pop()
        taken.add(i)
        if name.startswith("departure"):
            res *= myTicket[i]
    return res
