from collections import namedtuple
import re

Policy = namedtuple("Policy", "low high char")
regex = re.compile(r"(\d+)-(\d+)\s(\w):\s(\w+)")


def parseData(data):
    for line in data.strip().split("\n"):
        low, high, c, pwd = regex.match(line).groups()
        policy = Policy(int(low), int(high), c)
        yield policy, pwd


def part1(data):
    return sum(policy.low <= pwd.count(policy.char) <= policy.high for policy, pwd in parseData(data))


def part2(data):
    return sum(
        (pwd[policy.low - 1] == policy.char) ^ (pwd[policy.high - 1] == policy.char) for policy, pwd, in parseData(data)
    )
