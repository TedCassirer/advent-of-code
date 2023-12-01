N = 20201227


def calculateLoopSize(publicKey):
    loopSize = 0
    n = 1
    while n != publicKey:
        n = (n * 7) % N
        loopSize += 1
    return loopSize


def calculateEncryptionKey(publicKey, loopSize):
    n = 1
    for _ in range(loopSize):
        n = (n * publicKey) % N
    return n


def part_a(data):
    cardPublicKey, doorPublicKey = map(int, data.splitlines())
    doorLoopSize = calculateLoopSize(doorPublicKey)
    encryptionKey = calculateEncryptionKey(cardPublicKey, doorLoopSize)
    return encryptionKey


def part_b(data):
    pass
