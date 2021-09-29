from collections import defaultdict


class Bot:
    def __init__(self):
        self.__provider1 = None
        self.__provider2 = None
        self.__hi = None
        self.__lo = None

    def __loadValues(self):
        v1, v2 = self.__provider1(), self.__provider2()
        self.__lo, self.__hi = sorted((v1, v2))

    def getHigh(self):
        if self.__hi is None:
            self.__loadValues()
        return self.__hi

    def getLow(self):
        if self.__lo is None:
            self.__loadValues()
        return self.__lo

    def addProvider(self, provider):
        if self.__provider1:
            assert self.__provider2 is None
            self.__provider2 = provider
        else:
            self.__provider1 = provider


class Output:
    def __init__(self):
        self.__provider = None

    def addProvider(self, provider):
        assert self.__provider is None
        self.__provider = provider

    def get(self):
        return self.__provider()


def getBots(data):
    bots = defaultdict(Bot)
    outputs = defaultdict(Output)
    for line in data.splitlines():
        if line.startswith("value "):
            # value 31 goes to bot 50
            parts = line.split(" ")
            n, bot = int(parts[1]), int(parts[5])

            def giveValue(val):
                return lambda: val

            bots[bot].addProvider(giveValue(n))
        else:
            # bot 198 gives low to bot 184 and high to bot 62
            parts = line.split(" ")
            bot = bots[int(parts[1])]

            lowTargetId = int(parts[6])
            lowTarget = bots[lowTargetId] if parts[5] == "bot" else outputs[lowTargetId]

            highTargetId = int(parts[11])
            highTarget = bots[highTargetId] if parts[10] == "bot" else outputs[highTargetId]

            lowTarget.addProvider(bot.getLow)
            highTarget.addProvider(bot.getHigh)

    return bots, outputs


def part1(data):
    bots, _ = getBots(data)
    for id, bot in bots.items():
        if bot.getLow() == 17 and bot.getHigh() == 61:
            return id


def part2(data):
    _, outputs = getBots(data)
    return outputs[0].get() * outputs[1].get() * outputs[2].get()


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2016, day=10)

    print(part1(data))
    print(part2(data))
