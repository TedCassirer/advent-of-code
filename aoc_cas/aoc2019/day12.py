import re
from math import gcd


class Moon:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vx = 0
        self.vy = 0
        self.vz = 0

    def apply_gravity_from(self, other):
        if self.x < other.x:
            self.vx += 1
        elif self.x > other.x:
            self.vx -= 1

        if self.y < other.y:
            self.vy += 1
        elif self.y > other.y:
            self.vy -= 1

        if self.z < other.z:
            self.vz += 1
        elif self.z > other.z:
            self.vz -= 1

    def tick(self):
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz

    def __kinetic_energy(self):
        return abs(self.vx) + abs(self.vy) + abs(self.vz)

    def __potential_energy(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def energy(self):
        return self.__kinetic_energy() * self.__potential_energy()

    def __hash__(self):
        return hash((self.x, self.y, self.z, self.vx, self.vy, self.vz))

    def x_hash(self):
        return hash((self.x, self.vx))

    def y_hash(self):
        return hash((self.y, self.vy))

    def z_hash(self):
        return hash((self.z, self.vz))


def get_moons(data):
    regex = re.compile(r"=(-?\d+)")
    moons = {Moon(*map(int, regex.findall(line))) for line in data.split("\n")}
    return moons


def part1(data):
    moons = get_moons(data)
    for tick in range(1000):
        for m1 in moons:
            for m2 in moons:
                m1.apply_gravity_from(m2)

        for moon in moons:
            moon.tick()
    return sum(moon.energy() for moon in moons)


def part2(data):
    periods = []
    for hash_fun in [Moon.x_hash, Moon.y_hash, Moon.z_hash]:
        moons = get_moons(data)
        states = {}
        for tick in range(100000000000):
            for m1 in moons:
                for m2 in moons:
                    m1.apply_gravity_from(m2)
            state = tuple(hash_fun(m) for m in moons)
            if state in states:
                periods.append(tick - states[state])
                break
            states[state] = tick
            for moon in moons:
                moon.tick()

    x_period, y_period, z_period = periods
    gcf = gcd(x_period, gcd(y_period, z_period))
    return (x_period * y_period * z_period) // gcf ** 2
