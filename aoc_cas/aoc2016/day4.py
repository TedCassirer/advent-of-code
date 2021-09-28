from collections import Counter


def getRoomData(line):
    i = line.index("[")
    left, checkSum = line[:i], line[i + 1 : -1]
    *name, sectorId = left.split("-")
    return name, int(sectorId), checkSum


def fiveMostCommonChars(string):
    charCount = Counter(string)
    return "".join(char for char, count in sorted(charCount.items(), key=lambda cc: (-cc[1], cc[0]))[:5])


def decryptLetter(c, sectorId):
    if c == "-":
        return " "
    return chr(ord("a") + (ord(c) - ord("a") + sectorId) % 26)


def part1(data):
    roomData = map(getRoomData, data.splitlines())
    validIdSum = 0
    for name, sectorId, checkSum in roomData:
        if checkSum == fiveMostCommonChars("".join(name)):
            validIdSum += sectorId
    return validIdSum


def part2(data):
    roomData = map(getRoomData, data.splitlines())
    for name, sectorId, checkSum in roomData:
        decryptedName = "".join((decryptLetter(c, sectorId) for c in "-".join(name)))
        if decryptedName == "northpole object storage":
            return sectorId


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2016, day=4)
    print(part1(data))
    print(part2(data))
