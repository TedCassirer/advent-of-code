def buildVisibilityMapsFromOutside(heights):
    M, N = len(heights), len(heights[0])

    left = [[-1] * N for _ in range(M)]
    for y in range(1, M - 1):
        for x in range(1, N - 1):
            left[y][x] = max(left[y][x - 1], heights[y][x - 1])

    top = [[-1] * N for _ in range(M)]
    for x in range(1, N - 1):
        for y in range(1, M - 1):
            top[y][x] = max(top[y - 1][x], heights[y - 1][x])

    right = [[-1] * N for _ in range(M)]
    for y in range(1, M - 1):
        for x in range(N - 2, 0, -1):
            right[y][x] = max(right[y][x + 1], heights[y][x + 1])

    bot = [[-1] * N for _ in range(M)]
    for x in range(1, N - 1):
        for y in range(M - 2, 0, -1):
            bot[y][x] = max(bot[y + 1][x], heights[y + 1][x])

    return left, top, right, bot


def part_a(data):
    heights = [[int(c) for c in row] for row in data.splitlines()]
    visibilities = buildVisibilityMapsFromOutside(heights)
    visible = 0
    for y, row in enumerate(heights):
        for x, height in enumerate(row):
            visible += any(height > v[y][x] for v in visibilities)
    return visible


def part_b(data):
    heights = [[int(c) for c in row] for row in data.splitlines()]
    M, N = len(heights), len(heights[0])

    def viewScore(r, c):
        h = heights[r][c]
        if r == 0 or r == M - 1 or c == 0 or c == N - 1 or h == 0:
            return 0

        x = c - 1
        while x > 0 and heights[r][x] < h:
            x -= 1
        left = c - x

        y = r - 1
        while y > 0 and heights[y][c] < h:
            y -= 1
        up = r - y

        x = c + 1
        while x < N - 1 and heights[r][x] < h:
            x += 1
        right = x - c

        y = r + 1
        while y < M - 1 and heights[y][c] < h:
            y += 1
        down = y - r

        return left * up * right * down

    return max(viewScore(r, c) for r in range(M) for c in range(N))


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2022, day=8)

    print(part_a(data))
    print(part_b(data))
