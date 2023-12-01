from collections import deque


def parseHeightMap(data):
    rows = data.splitlines()
    R, C = len(rows), len(rows[0])

    heightMap = [[0] * C for _ in range(R)]

    for r, row in enumerate(rows):
        for c, h in enumerate(row):
            if h == "S":
                start = (r, c)
                h = "a"
            elif h == "E":
                end = (r, c)
                h = "z"
            heightMap[r][c] = ord(h)
    return heightMap, start, end


def search(heightMap, start, connected, isEnd):
    seen = set()
    queue = deque([(0, start)])
    while queue:
        steps, pos = queue.popleft()
        if isEnd(pos):
            return steps
        if pos in seen:
            continue
        seen.add(pos)
        for y, x in connected(heightMap, *pos):
            queue.append((steps + 1, (y, x)))


def part_a(data):
    heightMap, start, end = parseHeightMap(data)

    def connected(heightMap, y, x):
        h = heightMap[y][x]
        if y > 0 and heightMap[y - 1][x] - h <= 1:
            yield y - 1, x
        if x > 0 and heightMap[y][x - 1] - h <= 1:
            yield y, x - 1
        if y < len(heightMap) - 1 and heightMap[y + 1][x] - h <= 1:
            yield y + 1, x
        if x < len(heightMap[0]) - 1 and heightMap[y][x + 1] - h <= 1:
            yield y, x + 1

    return search(heightMap, start, connected, end.__eq__)


def part_b(data):
    heightMap, start, end = parseHeightMap(data)

    def connected(heightMap, y, x):
        h = heightMap[y][x]
        if y > 0 and heightMap[y - 1][x] - h >= -1:
            yield y - 1, x
        if x > 0 and heightMap[y][x - 1] - h >= -1:
            yield y, x - 1
        if y < len(heightMap) - 1 and heightMap[y + 1][x] - h >= -1:
            yield y + 1, x
        if x < len(heightMap[0]) - 1 and heightMap[y][x + 1] - h >= -1:
            yield y, x + 1

    return search(heightMap, end, connected, lambda pos: heightMap[pos[0]][pos[1]] == ord("a"))


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2022, day=12)

    print(part_a(data))
    print(part_b(data))
