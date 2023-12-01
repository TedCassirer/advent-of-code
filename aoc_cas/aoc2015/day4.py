import hashlib


def part_a(data):
    for i in range(10000000):
        hash = hashlib.md5(str.encode(f"{data}{i}")).hexdigest()
        if hash[:5] == "00000":
            return i


def part_b(data):
    for i in range(10000000):
        hash = hashlib.md5(str.encode(f"{data}{i}")).hexdigest()
        if hash[:6] == "000000":
            return i


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2015, day=4)

    print(part_a(data))
    print(part_b(data))
