from itertools import combinations, product
from collections import namedtuple
import math


class Equipment:
    def __init__(self, cost, damage, armor):
        self.cost = cost
        self.damage = damage
        self.armor = armor

    def __add__(self, other):
        return Equipment(self.cost + other.cost, self.damage + other.damage, self.armor + other.armor)

    def __lt__(self, other):
        return (self.cost, self.damage, self.armor) < (
            other.cost,
            other.damage,
            other.armor,
        )


Fighter = namedtuple("Fighter", ("hp", "damage", "armor"))

weapons = [
    Equipment(8, 4, 0),
    Equipment(10, 5, 0),
    Equipment(25, 6, 0),
    Equipment(40, 7, 0),
    Equipment(74, 8, 0),
]

armors = [
    Equipment(0, 0, 0),
    Equipment(13, 0, 1),
    Equipment(31, 0, 2),
    Equipment(53, 0, 3),
    Equipment(75, 0, 4),
    Equipment(102, 0, 5),
]

rings = [
    Equipment(0, 0, 0),
    Equipment(25, 1, 0),
    Equipment(50, 2, 0),
    Equipment(100, 3, 0),
    Equipment(20, 0, 1),
    Equipment(40, 0, 2),
    Equipment(80, 0, 3),
]
rings = [r1 + r2 for r1, r2 in combinations(rings, 2)]
rings.append(Equipment(0, 0, 0))

loadouts = sorted(weapon + armor + ring for weapon, armor, ring in product(weapons, armors, rings))
playerHp = 100


def winsFight(fighter, opponent):
    fighterDps = max(1, fighter.damage - opponent.armor)
    opponentDps = max(1, opponent.damage - fighter.armor)
    turnsToKillOpponent = math.ceil(opponent.hp / fighterDps)
    turnsToKillFighter = math.ceil(fighter.hp / opponentDps)
    return turnsToKillOpponent <= turnsToKillFighter


def getBossStats(data):
    stats = {}
    for line in data.splitlines():
        stat, val = line.split(": ")
        stats[stat] = int(val)
    return Fighter(hp=stats["Hit Points"], damage=stats["Damage"], armor=stats["Armor"])


def part_a(data):
    boss = getBossStats(data)
    for equipmentStats in loadouts:
        fighter = Fighter(playerHp, equipmentStats.damage, equipmentStats.armor)
        if winsFight(fighter, boss):
            return equipmentStats.cost


def part_b(data):
    boss = getBossStats(data)
    for equipmentStats in loadouts[::-1]:
        fighter = Fighter(playerHp, equipmentStats.damage, equipmentStats.armor)
        if not winsFight(fighter, boss):
            return equipmentStats.cost


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2015, day=21)
    print(part_a(data))
    print(part_b(data))
