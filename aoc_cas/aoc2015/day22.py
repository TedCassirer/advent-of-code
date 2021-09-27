from collections import namedtuple
import heapq
from dataclasses import dataclass

Spell = namedtuple("Spell", ("name", "cost"))
spells = [
    Spell("Magic Missiles", 53),
    Spell("Drain", 73),
    Spell("Shield", 113),
    Spell("Poison", 173),
    Spell("Recharge", 229),
]


@dataclass
class Player:
    hp: int
    mana: int
    manaSpent: 0
    shield: int
    recharge: int
    hard: bool

    def onTurnStart(self):
        player = self.copy()
        if player.hard:
            player.hp -= 1
        if player.recharge:
            player.recharge -= 1
            player.mana += 101
        if player.shield:
            player.shield -= 1
        return player

    def castableSpells(self):
        for spell in spells:
            if spell.cost > self.mana:
                continue
            if spell.name == "Shield" and self.shield:
                continue
            if spell.name == "Recharge" and self.recharge:
                continue
            if spell.name == "Drain" and self.hp > 1:
                continue
            yield spell

    def castSpell(self, spell, boss):
        player = self.copy()
        boss = boss.copy()
        player.mana -= spell.cost
        player.manaSpent += spell.cost
        if spell.name == "Magic Missiles":
            boss.hp -= 4
        elif spell.name == "Drain":
            boss.hp -= 2
            player.hp += 2
        elif spell.name == "Shield":
            player.shield = 6
        elif spell.name == "Poison":
            boss.poison = 6
        elif spell.name == "Recharge":
            player.recharge = 5
        return player, boss

    def copy(self):
        return Player(self.hp, self.mana, self.manaSpent, self.shield, self.recharge, self.hard)


@dataclass
class Boss:
    hp: int
    damage: int
    poison: int

    def onTurnStart(self):
        if self.poison:
            return Boss(self.hp - 3, self.damage, self.poison - 1)
        else:
            return self

    def slapPlayer(self, player):
        dps = max(1, self.damage - 7) if player.shield else self.damage
        player = player.copy()
        player.hp -= dps
        return player

    def dealDamage(self, amount):
        return Boss(self.hp - amount, self.damage, self.poison)

    def copy(self):
        return Boss(self.hp, self.damage, self.poison)


@dataclass(frozen=True)
class Game:
    player: Player
    boss: Boss
    playersTurn: bool
    events: tuple[str] = tuple()

    def startTurn(self):
        boss = self.boss.onTurnStart()
        player = self.player.onTurnStart()
        if boss.hp <= 0:
            yield Game(player, boss, True, self.events + ("Boss died from posion",))
            return
        if self.playersTurn:
            if player.mana < 53:
                return
            for spell in player.castableSpells():
                p, b = player.castSpell(spell, boss)
                event = (f"{spell.name} - {p.hp}|{b.hp} {p.mana}/{p.manaSpent}",)
                yield Game(p, b, False, self.events + event)
        else:
            player = boss.slapPlayer(player)
            event = (f"Slap! - {player.hp}|{boss.hp}",)
            yield Game(player, boss, True, self.events + event)

    def __lt__(self, other):
        return self.player.manaSpent < other.player.manaSpent

    def __repr__(self):
        return " -> ".join(self.events)


def getBoss(data):
    hp, damage = (int(line.split(": ")[1]) for line in data.splitlines())
    return Boss(hp, damage, 0)


def part1(data):
    player = Player(50, 500, 0, 0, 0, False)
    boss = getBoss(data)
    game = Game(player, boss, True)
    heap = [game]
    while heap:
        current = heapq.heappop(heap)
        if current.player.hp <= 0:
            continue
        elif current.boss.hp <= 0:
            return current.player.manaSpent
        for game in current.startTurn():
            heapq.heappush(heap, game)
    return "Hepp"


def part2(data):
    player = Player(50, 500, 0, 0, 0, True)
    boss = getBoss(data)
    game = Game(player, boss, True)
    heap = [game]
    while heap:
        current = heapq.heappop(heap)
        if current.player.hp <= 0:
            continue
        elif current.boss.hp <= 0:
            return current.player.manaSpent
        for game in current.startTurn():
            heapq.heappush(heap, game)
    return "Hepp"


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2015, day=22)
    print(part1(data))
    print(part2(data))
