from hashlib import md5

def findLeadingZeros(start, N):
    leading = '0' * N
    for n in range(0, 1 << 32):
        string = start + str(n)
        digest = md5(string.encode('utf-8')).hexdigest()
        if digest.startswith(leading):
            yield digest

def part1(data):
    numbers = findLeadingZeros(data, 5)
    return ''.join(str(next(numbers)[5]) for _ in range(8))

def part2(data):
    pw = [None] * 8
    for hash in findLeadingZeros(data, 5):
        i, c = int(hash[5], 16), hash[6]
        if i < 8 and not pw[i]:
            pw[i] = c
            if all(pw):
                return ''.join(pw)
if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2016, day=5)
    print(part1(data))
    print(part2(data))
