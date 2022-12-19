dirs = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}


def parseMoves(data):
    for line in data.splitlines():
        dir, k = line.split(" ")
        yield dirs[dir], int(k)


def move(pos, dir):
    return (pos[0] + dir[0], pos[1] + dir[1])


def direction(pos1, pos2):
    dy = pos2[0] - pos1[0]
    dx = pos2[1] - pos1[1]
    if abs(dy) < 2 and abs(dx) < 2:
        return (0, 0)

    dirY = dy // abs(dy) if dy else 0
    dirX = dx // abs(dx) if dx else 0
    return (dirY, dirX)


def part1(data):
    rope = [(0, 0) for _ in range(2)]
    visited = {rope[-1]}
    for dir, k in parseMoves(data):
        for _ in range(k):
            rope[0] = move(rope[0], dir)
            for i in range(len(rope) - 1):
                dir2 = direction(rope[i + 1], rope[i])
                rope[i + 1] = move(rope[i + 1], dir2)
            visited.add(rope[-1])

    return len(visited)


def part2(data):
    rope = [(0, 0) for _ in range(10)]
    visited = {rope[-1]}
    for dir, k in parseMoves(data):
        for _ in range(k):
            rope[0] = move(rope[0], dir)
            for i in range(len(rope) - 1):
                dir2 = direction(rope[i + 1], rope[i])
                rope[i + 1] = move(rope[i + 1], dir2)
            visited.add(rope[-1])

    return len(visited)


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2022, day=9)

    print(part1(data))
    print(part2(data))
