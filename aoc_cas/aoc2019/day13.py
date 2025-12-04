from __future__ import annotations

from typing import Iterator, Optional, Tuple

from .IntCodeComputer import IntCodeComputerVM

EMPTY = 0
WALL = 1
BLOCK = 2
PADDLE = 3
BALL = 4


class GameState:
    def __init__(self):
        self.grid = [[EMPTY] * 100 for _ in range(100)]
        self.paddle_pos: Optional[Tuple[int, int]] = None
        self.ball_pos: Optional[Tuple[int, int]] = None
        self.score = 0

    def update(self, x, y, tile):
        if x == -1 and y == 0:
            self.score = tile
            return
        self.grid[y][x] = tile
        if tile == PADDLE:
            self.paddle_pos = (y, x)
        elif tile == BALL:
            self.ball_pos = (y, x)

    def get_input(self) -> Iterator[int]:
        while True:
            if self.ball_pos is None or self.paddle_pos is None:
                yield 0
                continue
            ball_x = self.ball_pos[1]
            paddle_x = self.paddle_pos[1]
            if ball_x == paddle_x:
                yield 0
            else:
                yield abs(ball_x - paddle_x) // (ball_x - paddle_x)


def read_program(data):
    return [int(n) for n in data.split(",")]


def part_a(data):
    computer = IntCodeComputerVM(read_program(data))
    output = list(computer.run())
    return sum(1 for i in range(2, len(output), 3) if output[i] == BLOCK)


def part_b(data):
    program = read_program(data)
    program[0] = 2
    computer = IntCodeComputerVM(program, 4)
    game_state = GameState()
    computer.input_provided_from(game_state.get_input())
    runner = computer.run()
    for x in runner:
        y, tile = next(runner), next(runner)
        game_state.update(x, y, tile)
    return game_state.score
