def get_input(data):
    return tuple(int(c) for c in data.split("-"))


def get_numbers(start, end):
    for n in range(start, end):
        yield [int(c) for c in str(n)]


def is_double_number(numbers):
    return any(c1 == c2 for c1, c2 in zip(numbers[:-1], numbers[1:]))


def is_sorted(numbers):
    return numbers == sorted(numbers)


def double_number_not_part_of_group(numbers):
    padded_numbers = [None, None] + numbers + [None, None]
    return any(
        c1 != c2 and c2 == c3 and c3 != c4
        for c1, c2, c3, c4 in zip(
            padded_numbers[:-3],
            padded_numbers[1:-2],
            padded_numbers[2:-1],
            padded_numbers[3:],
        )
    )


def get_numbers_matching_predicates(data, *predicates):
    numbers = get_numbers(*get_input(data))
    matching_numbers = filter(lambda n: all(p(n) for p in predicates), numbers)
    return list(matching_numbers)


def part_a(data):
    matching_numbers = get_numbers_matching_predicates(
        data,
        is_sorted,
        is_double_number,
    )
    return len(matching_numbers)


def part_b(data):
    matching_numbers = get_numbers_matching_predicates(
        data,
        is_sorted,
        double_number_not_part_of_group,
    )
    return len(matching_numbers)
