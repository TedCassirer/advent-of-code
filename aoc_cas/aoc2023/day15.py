from typing import Iterator


def parse_sequence(data: str) -> Iterator[str]:
    for sequence in data.split(","):
        yield sequence


def hash(string: str) -> int:
    val = 0
    for c in string:
        val += ord(c)
        val *= 17
        val %= 256
    return val


def part_a(data: str) -> int:
    return sum(hash(seq) for seq in parse_sequence(data))


def part_b(data: str) -> int:
    boxes = [dict() for _ in range(256)]

    for i, seq in enumerate(parse_sequence(data)):
        if "=" in seq:
            label, focal_length = seq.split("=")
            box = boxes[hash(label)]
            if label in box:
                box[label][1] = int(focal_length)
            else:
                box[label] = [i, int(focal_length)]
        else:
            label = seq[:-1]
            box = boxes[hash(label)]
            box.pop(label, None)

    focusing_power = 0
    for box_num, box in enumerate(boxes, start=1):
        lenses = sorted(box.values())
        for lens_num, (_, focal_length) in enumerate(lenses, start=1):
            focusing_power += box_num * lens_num * focal_length
    return focusing_power


if __name__ == "__main__":
    from aoc_cas.util import solve_with_example_data

    solve_with_example_data(year=2023, day=15)
