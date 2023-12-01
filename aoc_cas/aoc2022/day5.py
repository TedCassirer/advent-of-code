def parseData(data):
    stackData, instructionData = data.split("\n\n")
    numStacks = (data.index("\n") + 1) // 4
    stacks = [[] for _ in range(numStacks)]
    instructions = []

    for stackRow in stackData.splitlines()[-2::-1]:
        for i, content in enumerate(stackRow[1::4]):
            if content != " ":
                stacks[i].append(content)

    for line in instructionData.splitlines():
        qnt, fromStack, toStack = map(int, line.split(" ")[1::2])
        instructions.append((qnt, fromStack - 1, toStack - 1))

    return stacks, instructions


def part1(data):
    stacks, instructions = parseData(data)
    for qnt, fromStack, toStack in instructions:
        stacks[toStack].extend(stacks[fromStack][: -qnt - 1 : -1])
        del stacks[fromStack][-qnt:]
    return "".join(s[-1] for s in stacks)


def part2(data):
    stacks, instructions = parseData(data)
    for qnt, fromStack, toStack in instructions:
        stacks[toStack].extend(stacks[fromStack][-qnt:])
        del stacks[fromStack][-qnt:]
    return "".join(s[-1] for s in stacks)


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2022, day=5)

    print(part1(data))
    print(part2(data))
