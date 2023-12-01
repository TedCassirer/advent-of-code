class Computer:
    memory: dict = {"a": 0, "b": 0, "c": 0, "d": 0}
    i: int

    def __inc(self, a, *_):
        self.memory[a] += 1

    def __dec(self, a, *_):
        self.memory[a] -= 1

    def __cpy(self, a, b):
        self.memory[b] = self.__get(a)

    def __jnz(self, a, b):
        if self.__get(a):
            self.i += int(b) - 1

    def __get(self, a):
        if a.isalpha():
            return self.memory[a]
        else:
            return int(a)

    def run(self, program):
        self.i = 0
        while self.i < len(program):
            cmd, *args = program[self.i].split(" ")
            if cmd == "dec":
                self.__dec(*args)
            elif cmd == "inc":
                self.__inc(*args)
            elif cmd == "cpy":
                self.__cpy(*args)
            elif cmd == "jnz":
                self.__jnz(*args)
            self.i += 1
        return self.memory["a"]


def part1(data):
    comp = Computer()
    return comp.run(data.splitlines())


def part2(data):
    comp = Computer()
    comp.memory["c"] = 1
    return comp.run(data.splitlines())


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2016, day=12)

    print(part1(data))
    print(part2(data))
