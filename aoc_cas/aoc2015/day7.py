class Value:
    def __init__(self, token, signal):
        self.token = token
        self.value = None
        self.signal = signal

    def get(self, values):
        if self.value is None:
            self.value = self.signal.evaluate(values)
        return self.value

    def reset(self):
        self.value = None


class Signal:
    def __init__(self, op, *values):
        self.op = op
        self.values = values

    def evaluate(self, allValues):
        return self.op(*(allValues[v].get(allValues) if v.isalpha() else int(v) for v in self.values))


def parseLine(line):
    signalString, assignedValue = line.split(" -> ")
    signalParts = signalString.split(" ")
    if len(signalParts) == 1:
        op = lambda n: n
        values = signalParts
    elif len(signalParts) == 2:
        assert signalParts[0] == "NOT"
        op = lambda n: ~n
        values = [signalParts[1]]
    else:
        v1, operation, v2 = signalParts
        values = [v1, v2]
        if operation == "AND":
            op = lambda a, b: a & b
        elif operation == "OR":
            op = lambda a, b: a | b
        elif operation == "RSHIFT":
            op = lambda a, b: a >> b
        elif operation == "LSHIFT":
            op = lambda a, b: a << b
    signal = Signal(op, *values)
    return Value(assignedValue, signal)


def part_a(data):
    values = dict()
    for line in data.splitlines():
        value = parseLine(line.strip())
        values[value.token] = value
    return values["a"].get(values)


def part_b(data):
    values = dict()
    for line in data.splitlines():
        value = parseLine(line.strip())
        values[value.token] = value

    aValue = values["a"].get(values)
    for v in values.values():
        v.reset()
    values["b"].value = aValue
    return values["a"].get(values)


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2015, day=7)

    print(part_a(data))
    print(part_b(data))
