class Raindeer:
    def __init__(self, name, speed, flyTime, restTime):
        self.name = name
        self.speed = speed
        self.flyTime = flyTime
        self.restTime = restTime

    def distanceFlied(self, time):
        cycleTime = self.flyTime + self.restTime
        cycleDist = self.speed * self.flyTime

        cyclesFlied, remainingTime = divmod(time, cycleTime)
        distanceFlied = cyclesFlied * cycleDist
        distanceFlied += min(remainingTime, self.flyTime) * self.speed
        return distanceFlied


def parse(line):
    words = line[:-1].split(" ")
    return Raindeer(words[0], int(words[3]), int(words[6]), int(words[13]))


def part1(data):
    return max(r.distanceFlied(2503) for r in map(parse, data.splitlines()))


def part2(data):
    bois = [parse(line) for line in data.splitlines()]
    score = {r.name: 0 for r in bois}
    for t in range(1, 2504):
        best = (0, [])
        for r in bois:
            distanceFlied = r.distanceFlied(t)
            if best[0] == distanceFlied:
                best[1].append(r.name)
            elif best[0] < distanceFlied:
                best = (distanceFlied, [r.name])
        for name in best[1]:
            score[name] += 1
    return max(v for k, v in score.items())


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2015, day=14)

    print(part1(data))
    print(part2(data))
