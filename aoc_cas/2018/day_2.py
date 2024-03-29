from collections import Counter
from utils import timeIt, readData


@timeIt
def part_a():
    letterCounts = map(dict.values, map(Counter, readData("2018/data/day_2")))

    threeLetters = 0
    twoLetters = 0

    for letterCount in letterCounts:
        threeLetters += 3 in letterCount
        twoLetters += 2 in letterCount

    return threeLetters * twoLetters


@timeIt
def part_b():
    def maskLetter(word, i):
        return word[:i] + word[i + 1 :]

    words = list(readData("2018/data/day_2"))
    N = len(words[0])
    for i in range(N):
        seen = set()
        for word in words:
            maskedWord = maskLetter(word, i)
            if maskedWord in seen:
                return maskedWord
            else:
                seen.add(maskedWord)


if __name__ == "__main__":
    print("Part A:", part_a())
    print("Part B:", part_b())
