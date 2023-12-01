from collections import deque


def getIsWall(data):
    favoriteNumber = int(data)

    def isWall(x, y):
        if y < 0 or x < 0:
            return True
        n = favoriteNumber + x * x + 3 * x + 2 * x * y + y + y * y
        wall = 0
        while n:
            wall ^= n & 1
            n >>= 1
        return bool(wall)

    return isWall


def search(isWall, goal):
    seen = set()
    queue = deque([((1, 1), 0)])
    while queue:
        curr, steps = queue.popleft()
        if curr in seen:
            continue
        seen.add(curr)
        if curr == goal:
            return steps
        y, x = curr
        for nxt in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
            if not isWall(*nxt):
                queue.append((nxt, steps + 1))


def searchMaxSteps(isWall, maxSteps):
    seen = set()
    queue = deque([((1, 1), 0)])
    while queue:
        curr, steps = queue.popleft()
        if curr in seen or steps > maxSteps:
            continue
        seen.add(curr)
        y, x = curr
        for nxt in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
            if not isWall(*nxt):
                queue.append((nxt, steps + 1))
    return len(seen)


def part1(data):
    return search(getIsWall(data), (31, 39))


def part2(data):
    return searchMaxSteps(getIsWall(data), 50)


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2016, day=13)

    print(part1(data))
    print(part2(data))
