from collections import namedtuple
import heapq

Effect = namedtuple("Effect", ("name", "turns", "invoke"))
Spell = namedtuple("Spell", ("name", "cost", "invoke"))
shieldEffect = Effect("Shield", 6, lambda g: g.affectPlayer(Player.setArmor, 7))
poisonEffect = Effect("Poison", 6, lambda g: g.affectBoss(Boss.dealDamage, 3))
rechargeEffect = Effect("Recharge", 5, lambda g: g.affectPlayer(Player.restoreMana, 101))
spells = [
    Spell("Magic Missilies", 53, lambda game: game.affectBoss(Boss.dealDamage, 4)),
    Spell("Drain", 73, lambda game: game.affectBoss(Boss.dealDamage, 2).affectPlayer(Player.restoreHealth, 2)),
    Spell("Shield", 113, lambda game: game.affectPlayer(Player.setArmor, 7).addEffect(shieldEffect)),
    Spell("Poison", 173, lambda game: game.addEffect(poisonEffect)),
    Spell("Recharge", 229, lambda game: game.addEffect(rechargeEffect)),
]


class Player:
    def __init__(self, hp, mana, armor, manaSpent):
        self.__hp = hp
        self.__mana = mana
        self.__armor = armor
        self.__manaSpent = manaSpent

    def restoreHealth(self, amount):
        return Player(self.__hp + amount, self.__mana, self.__armor, self.__manaSpent)

    def setArmor(self, armor):
        return Player(self.__hp, self.__mana, armor, self.__manaSpent)

    def spendMana(self, amount):
        assert self.__mana >= amount
        return Player(self.__hp, self.__mana - amount, self.__armor, self.__manaSpent + amount)

    def restoreMana(self, amount):
        return Player(self.__hp, self.__mana + amount, self.__armor, self.__manaSpent)

    def dealDamage(self, damage):
        dps = max(1, damage - self.__armor)
        return Player(self.__hp - dps, self.__mana, 0, self.__manaSpent)

    def manaSpent(self):
        return self.__manaSpent

    def mana(self):
        return self.__mana

    def isDead(self):
        return self.__hp <= 0


class Boss:
    def __init__(self, hp, damage):
        self.__hp = hp
        self.damage = damage

    def dealDamage(self, damage):
        return Boss(self.__hp - damage, self.damage)

    def isDead(self):
        return self.__hp <= 0
    def hp(self):
        return self.__hp
class Game:
    def __init__(self, player, boss, effects = {}):
        self.__player = player
        self.__boss = boss
        self.__effects = effects.copy()

    def addEffect(self, effect):
        assert effect.name not in self.__effects
        self.__effects[effect.name] = effect
        return self

    def affectPlayer(self, effect, amount):
        return Game(effect(self.__player, amount), self.__boss, self.__effects)

    def affectBoss(self, effect, amount):
        return Game(self.__player, effect(self.__boss, amount), self.__effects)

    def isActive(self):
        return not self.__player.isDead() and not self.__boss.isDead()

    def boss(self):
        return self.__boss

    def player(self):
        return self.__player
    
    def effects(self):
        return self.__effects

    def startTurn(self):
        game = Game(self.player(), self.boss(), self.effects())
        for effect in game.effects().values():
            game = effect.invoke(game)

        updatedEffects = {}
        for effect in game.effects().values():
            if effect.turns > 1:
                updatedEffects[effect.name] = Effect(effect.name, effect.turns - 1, effect.invoke)
        game = Game(game.player(), game.boss(), updatedEffects)

        if not game.isActive():
            return game
        current = game
        for spell in current.availableSpells():
            game = spell.invoke(current)
            game = game.affectPlayer(Player.spendMana, spell.cost)
            if not game.isActive():
                return game

            for effect in game.effects().values():
                game = effect.invoke(game)
            updatedEffects = {}
            for effect in game.effects().values():
                if effect.turns > 1:
                    updatedEffects[effect.name] = Effect(effect.name, effect.turns - 1, effect.invoke)
            game.effect = updatedEffects

            game = game.affectPlayer(Player.dealDamage, game.__boss.damage)
            yield game

    def availableSpells(self):
        for spell in spells:
            if spell.name in self.__effects:
                continue
            if spell.cost > self.__player.mana():
                continue
            yield spell

    def __lt__(self, other):
        return (self.__player.manaSpent(), self.__boss.hp()) < (other.player().manaSpent(), other.boss().hp())

    def __repr__(self):
        return f'{self.player.hp} - {self.boss.hp} / {self.player.manaSpent} / {list(self.__effects.keys())}'


def getBoss(data):
    hp, damage = (int(line.split(": ")[1]) for line in data.splitlines())
    return Boss(hp, damage)


def part1(data):
    player = Player(25, 250, 0, 0)
    boss = getBoss(data)
    boss = Boss(14, 8)
    start = Game(player, boss)
    game = Game(player, boss)
    heap = [game]
    while heap:
        current = heapq.heappop(heap)
        if current.boss().isDead():
            return current.player.manaSpent
        elif current.player().isDead():
            continue
        for game in current.startTurn():
            heapq.heappush(heap, game)
    return "fart"


def part2(data):
    pass


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2015, day=22)
    print(part1(data))
    print(part2(data))
