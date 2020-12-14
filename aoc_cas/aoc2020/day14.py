from collections import defaultdict


def createValueMask(mask):
    mask0, mask1 = 0, 0
    for m in mask:
        mask0 <<= 1
        mask1 <<= 1
        if m == "X":
            mask0 += 1
        else:
            mask0 += int(m)
            mask1 += int(m)

    def applyMask(val):
        return (val & mask0) | mask1

    return applyMask


def createAddressDecoder(maskString):
    masks = [""]
    for m in maskString:
        if m == "X":
            newMasks = []
            for mask in masks:
                newMasks.append(mask + "1")
                newMasks.append(mask + "0")
            masks = newMasks
        else:
            m = m.replace("0", "X")
            for i in range(len(masks)):
                masks[i] += m
    masks = [createValueMask(mask) for mask in masks]

    def decode(val):
        for mask in masks:
            yield mask(val)

    return decode


def part1(data):
    memory = defaultdict(int)
    for line in data.splitlines():
        if line.startswith("mask"):
            mask = createValueMask(line.split(" = ")[1])
        else:
            left, right = line.split(" = ")
            address = int(left[4:-1])
            value = int(right)
            memory[address] = mask(value)
    return sum(memory.values())


def part2(data):
    memory = defaultdict(int)
    for line in data.splitlines():
        if line.startswith("mask"):
            decoder = createAddressDecoder(line.split(" = ")[1])
        else:
            left, right = line.split(" = ")
            address = int(left[4:-1])
            value = int(right)
            for adr in decoder(address):
                memory[adr] = value
    return sum(memory.values())
