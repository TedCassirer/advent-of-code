def part1(data):
    def get_edge_sum(line):
        digits = [int(char) for char in line if char.isdigit()]
        res = digits[0] * 10 + digits[-1]
        return res

    return sum(map(get_edge_sum, data.splitlines()))


def part2(data):
    spelled_out = {
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
        left_digit = min(((line + k).find(k), v) for k, v in spelled_out.items())[1]
        right_digit = max((line.rfind(k), v) for k, v in spelled_out.items())[1]
        result += 10 * left_digit + right_digit
    return result


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2023, day=1)
    print(part1(data))
    print(part2(data))
