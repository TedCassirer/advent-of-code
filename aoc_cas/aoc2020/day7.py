from collections import defaultdict
import re
from functools import lru_cache

bagRegex1 = re.compile(r"(\w+ \w+) bags contain (.+)")
bagRegex2 = re.compile(r"(\d+ \w+ \w+)")
myBag = ("shiny", "gold")


def getBaggyGraph(data):
    contains = defaultdict(dict)
    for line in data.splitlines():
        outer, rest = bagRegex1.match(line).groups()
        outerBag = tuple(outer.split(" "))
        if rest.startswith("no"):
            contains[outerBag] = dict()
        for inner in bagRegex2.findall(rest):
            count, adj, color = inner.split(" ")
            contains[outerBag][(adj, color)] = int(count)
    return dict(contains)


def part_a(data):
    baggyGraph = getBaggyGraph(data)

    @lru_cache(None)
    def containsBag(bag):
        return any(bagInner == myBag or containsBag(bagInner) for bagInner in baggyGraph[bag])

    return sum(containsBag(bag) for bag in baggyGraph)


def part_b(data):
    baggyGraph = getBaggyGraph(data)

    def totalBagCount(bag):
        return 1 + sum(count * totalBagCount(innerBag) for innerBag, count in baggyGraph[bag].items())

    return totalBagCount(myBag) - 1  # Subtract the outermost bag from the bag count
