from collections import deque


def hasPairSum(targetSum, numbers):
    seen = set()
    for n in numbers:
        if targetSum - n in seen:
            return n, targetSum - n
        seen.add(n)


def findWeakness(numbers, preamble):
    recent = deque(numbers[:preamble])
    for i in range(preamble, len(numbers)):
        n = numbers[i]
        if not hasPairSum(n, recent):
            return i
        else:
            recent.popleft()
            recent.append(n)


def findEncryptionWeakness(numbers, preamble):
    weakness = findWeakness(numbers, preamble)
    targetSum = numbers[weakness]
    rangeSum = 0
    left = 0
    for right, n in enumerate(numbers):
        rangeSum += n
        while rangeSum > targetSum:
            rangeSum -= numbers[left]
            left += 1
        if rangeSum == targetSum:
            smallest = min(numbers[left : right + 1])
            largest = max(numbers[left : right + 1])
            return smallest + largest


def part1(data):
    numbers = [int(n) for n in data.splitlines()]
    return numbers[findWeakness(numbers, 25)]


def part2(data):
    numbers = [int(n) for n in data.splitlines()]
    return findEncryptionWeakness(numbers, 25)
