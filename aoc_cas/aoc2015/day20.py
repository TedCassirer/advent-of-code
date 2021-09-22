from itertools import takewhile
from functools import lru_cache
from collections import Counter


def getPrimes(maxVal, primes=[2, 3]):
    for n in range(primes[-1] + 2, maxVal + 1, 2):
        for i in range(len(primes)):
            p = primes[i]
            if p ** 2 > n:
                primes.append(n)
                break
            if n % p == 0:
                break
    yield from takewhile(lambda p: p <= maxVal, primes)


@lru_cache(None)
def getPrimeFactors(number):
    if number == 1:
        return tuple()
    for p in getPrimes(int(number ** 0.5)):
        if number % p == 0:
            return (p,) + getPrimeFactors(number // p)
    return (number,)


def factorSum(number):
    factor_sum = 1
    for prime, power in Counter(getPrimeFactors(number)).items():
        factor_sum *= (prime ** (power + 1) - 1) // (prime - 1)
    return factor_sum


def part1(data):
    target = int(data) // 10
    for n in range(2, target):
        if factorSum(n) >= target:
            return n


def part2(data):
    target = int(data)
    for n in range(2, target // 11):
        fs = factorSum(n)
        if 11 * fs >= target:
            for n2 in range(1, 1 + n // 50):
                if n % n2 == 0:
                    fs -= n2
                if 11 * fs < target:
                    break
            else:
                return n
