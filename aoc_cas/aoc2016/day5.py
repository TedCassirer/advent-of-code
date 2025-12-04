from hashlib import md5
from typing import Iterator, List, Optional


def findLeadingZeros(start: str, N: int) -> Iterator[str]:
    leading = "0" * N
    for n in range(0, 1 << 32):
        string = start + str(n)
        digest = md5(string.encode("utf-8")).hexdigest()
        if digest.startswith(leading):
            yield digest


def part_a(data: str) -> str:
    numbers = findLeadingZeros(data, 5)
    return "".join(next(numbers)[5] for _ in range(8))


def part_b(data: str) -> str:
    pw: List[Optional[str]] = [None for _ in range(8)]
    for hash in findLeadingZeros(data, 5):
        i, c = int(hash[5], 16), hash[6]
        if i < 8 and not pw[i]:
            pw[i] = c
            if all(char is not None for char in pw):
                return "".join(char for char in pw if char is not None)
    raise ValueError("Password never completed")


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2016, day=5)
    print(part_a(data))
    print(part_b(data))
