class Board:
    def __init__(self, board):
        self.board = board
        self.rows = list()
        self.columns = list()
        for row in board:
            self.rows.append(set(row))
        for column in zip(*board):
            self.columns.append(set(column))

    def markNumber(self, number):
        for row in self.rows:
            row.discard(number)
        for column in self.columns:
            column.discard(number)

    def isBingo(self):
        return any(not r for r in self.rows) or any(not c for c in self.columns)

    def unmarkedNumbers(self):
        out = set()
        for r in self.rows:
            out.update(r)
        for c in self.columns:
            out.update(c)
        return out


def getNumbers(data):
    return [int(n) for n in data.split("\n\n")[0].split(",")]


def createBoards(data):
    boards = list()
    for boardStr in data.split("\n\n")[1:]:
        board = []
        for row in boardStr.splitlines():
            board.append([*map(int, row.strip().replace("  ", " ").split(" "))])
        boards.append(Board(board))
    return boards


def part_a(data):
    boards = createBoards(data)
    for n in getNumbers(data):
        for b in boards:
            b.markNumber(n)
            if b.isBingo():
                return n * sum(b.unmarkedNumbers())


def part_b(data):
    boards = set(createBoards(data))
    for n in getNumbers(data):
        bingodBoards = set()
        for b in boards:
            b.markNumber(n)
            if b.isBingo():
                if len(boards) == 1:
                    return n * sum(b.unmarkedNumbers())
                bingodBoards.add(b)
        boards -= bingodBoards


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2021, day=4)

    print(part_a(data))
    print(part_b(data))
