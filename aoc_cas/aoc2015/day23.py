from dataclasses import dataclass


@dataclass
class State:
    a: int
    b: int
    offset: int

    def half(self, register, *_):
        if register == "a":
            self.a //= 2
        elif register == "b":
            self.b //= 2
        self.offset += 1

    def tripple(self, register, *_):
        if register == "a":
            self.a *= 3
        elif register == "b":
            self.b *= 3
        self.offset += 1

    def increment(self, register, *_):
        if register == "a":
            self.a += 1
        elif register == "b":
            self.b += 1
        self.offset += 1

    def jump(self, distance, *_):
        distance = int(distance)
        self.offset += distance

    def jumpIfEven(self, register, distance):
        if register == "a":
            val = self.a
        elif register == "b":
            val = self.b
        if val % 2 == 0:
            self.jump(distance)
        else:
            self.offset += 1

    def jumpIfOne(self, register, distance):
        if register == "a":
            val = self.a
        elif register == "b":
            val = self.b
        if val == 1:
            self.jump(distance)
        else:
            self.offset += 1


ops = {
    "hlf": State.half,
    "inc": State.increment,
    "tpl": State.tripple,
    "jmp": State.jump,
    "jie": State.jumpIfEven,
    "jio": State.jumpIfOne,
}


def getInstruction(line):
    op = line[:3]
    args = line[4:].split(", ")
    return ops[op], args


def part_a(data):
    instructions = [getInstruction(line) for line in data.splitlines()]
    state = State(0, 0, 0)
    while state.offset < len(instructions):
        op, args = instructions[state.offset]
        op(state, *args)
    return state.b


def part_b(data):
    instructions = [getInstruction(line) for line in data.splitlines()]
    state = State(1, 0, 0)
    while state.offset < len(instructions):
        op, args = instructions[state.offset]
        op(state, *args)
    return state.b


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2015, day=23)
    print(part_a(data))
    print(part_b(data))
