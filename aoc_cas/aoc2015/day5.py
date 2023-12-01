def part_a(data):
    def rule1(s):
        vowels = set("aeiou")
        count = 0
        for c in s:
            count += c in vowels
        return count >= 3

    def rule2(s):
        for c1, c2 in zip(s, s[1:]):
            if c1 == c2:
                return True
        return False

    def rule3(s):
        forbidden = ["ab", "cd", "pq", "xy"]
        for f in forbidden:
            if f in s:
                return False
        return True

    return len([s for s in data.splitlines() if rule1(s) and rule2(s) and rule3(s)])


def part_b(data):
    def rule1(s):
        pairs = [c1 + c2 for c1, c2 in zip(s, s[1:])]
        for i in range(len(pairs)):
            p1 = pairs[i]
            if p1 in pairs[i + 2 :]:
                return True
        return False

    def rule2(s):
        for c1, c2, c3 in zip(s, s[1:], s[2:]):
            if c1 == c3:
                return True
        return False

    return len([s for s in data.splitlines() if rule1(s) and rule2(s)])


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2015, day=5)

    print(part_a(data))
    print(part_b(data))
