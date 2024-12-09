EMPTY = "."
BALL = "O"
ROCK = "#"


class Board:
    def __init__(self, data: str):
        lines = data.splitlines()
        M, N = len(lines), len(lines[0])
        self.rocks_column = [[-1] for _ in range(N)]
        self.rocks_row = [[-1] for _ in range(M)]
        self.balls = set()
        for y, row in enumerate(lines):
            for x, v in enumerate(row):
                if v == ROCK:
                    self.rocks_column[x].append(y)
                    self.rocks_row[y].append(x)
                elif v == BALL:
                    self.balls.add((y, x))

        for r in self.rocks_column:
            r.append(M)
        for r in self.rocks_row:
            r.append(N)

    def tilt_y(self, up: bool) -> None:
        for x, column in enumerate(self.rocks_column):
            for y0, y1 in zip(column, column[1:]):
                balls_in_area = 0
                for y in range(y0 + 1, y1):
                    if (y, x) in self.balls:
                        balls_in_area += 1
                        self.balls.remove((y, x))
                if up:
                    for y in range(y0 + 1, y0 + balls_in_area + 1):
                        self.balls.add((y, x))
                else:
                    for y in range(y1 - balls_in_area, y1):
                        self.balls.add((y, x))

    def tilt_x(self, left: bool) -> None:
        for y, row in enumerate(self.rocks_row):
            for x0, x1 in zip(row, row[1:]):
                balls_in_area = 0
                for x in range(x0 + 1, x1):
                    if (y, x) in self.balls:
                        balls_in_area += 1
                        self.balls.remove((y, x))
                if left:
                    for x in range(x0 + 1, x0 + balls_in_area + 1):
                        self.balls.add((y, x))
                else:
                    for x in range(x1 - balls_in_area, x1):
                        self.balls.add((y, x))

    def tilt_circle(self) -> None:
        self.tilt_y(up=True)
        self.tilt_x(left=True)
        self.tilt_y(up=False)
        self.tilt_x(left=False)

    def calculate_load(self) -> int:
        M = len(self.rocks_row)
        return sum(M - y for y, x in self.balls)

    def __repr__(self) -> str:
        M = len(self.rocks_row)
        N = len(self.rocks_column)
        board = []
        for row in range(M):
            board.append([EMPTY] * (N))

        for x, rocks in enumerate(self.rocks_column):
            for y in rocks[1:-1]:
                board[y][x] = ROCK
        for y, x in self.balls:
            board[y][x] = BALL

        return "\n".join("".join(r) for r in board)


def part_a(data: str) -> int:
    board = Board(data)
    board.tilt_y(up=True)
    return board.calculate_load()


def part_b(data: str) -> int:
    board = Board(data)
    seen = {}
    for cycle in range(1, 1000001):
        board.tilt_circle()
        fp = frozenset(board.balls)
        if fp in seen:
            cycles_to_repeat = cycle - seen[fp]
            total_remaining = 1000000000 - cycle
            for _ in range(total_remaining % cycles_to_repeat):
                board.tilt_circle()
            return board.calculate_load()
        else:
            seen[fp] = cycle
            seen[frozenset(board.balls)] = cycle
    return board.calculate_load()


if __name__ == "__main__":
    from aoc_cas.util import solve_with_example_input

    solve_with_example_input(year=2023, day=14)
