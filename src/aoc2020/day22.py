from collections import deque


def part1(data):
    player1, player2 = data.split("\n\n")
    player1 = deque(int(n) for n in player1.splitlines()[1:])
    player2 = deque(int(n) for n in player2.splitlines()[1:])

    while player1 and player2:
        c1, c2 = player1.popleft(), player2.popleft()
        if c1 > c2:
            player1.extend([c1, c2])
        else:
            player2.extend([c2, c1])

    winner = player1 or player2
    return sum((i + 1) * n for i, n in enumerate(reversed(winner)))


def part2(data):
    player1, player2 = data.split("\n\n")
    player1 = tuple(int(n) for n in player1.splitlines()[1:])
    player2 = tuple(int(n) for n in player2.splitlines()[1:])

    def recursiveCombat(player1, player2):
        seen = set()
        while player1 and player2:
            if (player1, player2) in seen:
                return player1, tuple()
            seen.add((player1, player2))

            c1, player1 = player1[0], tuple(player1[1:])
            c2, player2 = player2[0], tuple(player2[1:])

            if c1 <= len(player1) and c2 <= len(player2):
                d1, d2 = recursiveCombat(player1[:c1], player2[:c2])
                player1WinsRound = len(d1) > 0
            else:
                player1WinsRound = c1 > c2

            if player1WinsRound:
                player1 += (c1, c2)
            else:
                player2 += (c2, c1)

        return player1, player2

    player1, player2 = recursiveCombat(player1, player2)
    winner = player1 or player2
    return sum((i + 1) * n for i, n in enumerate(reversed(winner)))
