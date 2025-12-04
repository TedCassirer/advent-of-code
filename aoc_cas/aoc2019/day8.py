BLACK = 0
WHITE = 1
TRANSPARENT = 2


def get_image_data_layers(data, height, width):
    layer_size = width * height
    data = [int(s.strip()) for line in data.split("\n") for s in line]
    for layer_start in range(0, len(data), layer_size):
        layer_data = data[layer_start : layer_start + layer_size]
        layer = []
        for row_start in range(0, layer_size, width):
            layer.append(layer_data[row_start : row_start + width])
        yield layer


def count_number_of(num, layer):
    return sum(n == num for row in layer for n in row)


def to_printable_image(image):
    symbols = {BLACK: "░", WHITE: "▓", TRANSPARENT: "I'm invisible"}
    decoded_image = []
    for row in image:
        decoded_image.append("".join([symbols[s] for s in row]))
    return "\n" + "\n".join(decoded_image)


def get_pixels_matching(image, mode):
    for y, row in enumerate(image):
        for x, n in enumerate(image[y]):
            if n == mode:
                yield (y, x)


def part_a(data):
    height, width = 6, 25
    fewest_blacks = min(
        get_image_data_layers(data, height, width),
        key=lambda layer: len(list(get_pixels_matching(layer, BLACK))),
    )
    whites = count_number_of(WHITE, fewest_blacks)
    transparents = count_number_of(TRANSPARENT, fewest_blacks)
    return whites * transparents


def part_b(data):
    height, width = 6, 25
    layers = get_image_data_layers(data, height, width)
    final_image = [[TRANSPARENT] * width for _ in range(height)]
    for layer in layers:
        for y, x in get_pixels_matching(final_image, TRANSPARENT):
            final_image[y][x] = layer[y][x]

    image = to_printable_image(final_image)
    print(image)
    return "KYHFE"
