from dataclasses import dataclass


@dataclass
class Circuit:
    register: int = 1

    def noop(self):
        yield self.register

    def addx(self, v):
        yield self.register
        yield self.register
        self.register += v

    def runInstructions(self, instructions):
        for instruction in instructions.splitlines():
            if instruction == "noop":
                yield from self.noop()
            else:
                _, v = instruction.split(" ")
                yield from self.addx(int(v))


def part_a(data):
    circuit = Circuit()
    out = 0
    for i, strength in enumerate(circuit.runInstructions(data)):
        if ((i + 1) % 40) == 20:
            out += strength * (i + 1)
    return out


def part_b(data):
    circuit = Circuit()
    crt = [["."] * 40 for _ in range(6)]
    for i, strength in enumerate(circuit.runInstructions(data)):
        x = i % 40
        y = i // 40
        if abs(x - strength) <= 1:
            crt[y][x] = "#"

    display = "\n".join(("".join(row) for row in crt))
    print()
    print(display)
    expected = """
####..##..#....#..#.###..#....####...##.
#....#..#.#....#..#.#..#.#....#.......#.
###..#....#....####.###..#....###.....#.
#....#.##.#....#..#.#..#.#....#.......#.
#....#..#.#....#..#.#..#.#....#....#..#.
####..###.####.#..#.###..####.#.....##..
""".strip()

    if display == expected:
        return "EGLHBLFJ"
    else:
        return None


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2022, day=10)

    print(part_a(data))
    print(part_b(data))
