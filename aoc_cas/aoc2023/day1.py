def part1(data):
    result = 0
    for line in data.splitlines():
        digits = [int(char) for char in line if char.isdigit()]
        result += digits[0] * 10 + digits[-1]
    return result


def part2(data):
    digits = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    result = 0
    for line in data.splitlines():
        left_digit = min(digits.keys(), key=lambda k: (line + k).find(k))
        right_digit = max(digits.keys(), key=lambda k: line.rfind(k))
        result += 10 * digits[left_digit] + digits[right_digit]
    return result


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2023, day=1)
    print(part1(data))
    print(part2(data))
