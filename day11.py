def read_text(filename):
    """
    Reads a .txt file with the given filename and returns a list of newline-separated entries
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f]


def transpose(matrix):
    return list(map(list, zip(*matrix)))


def add_rows(matrix):
    rows_to_add = [i for i, row in enumerate(matrix) if all(c == '.' for c in row)]
    rows_to_add = [i + j for i, j in enumerate(rows_to_add)]
    row_size = len(matrix[0])
    for index in rows_to_add:
        matrix.insert(index, ['.'] * row_size)


def expand_space(space):
    space = transpose(space)
    add_rows(space)
    space = transpose(space)
    add_rows(space)
    return space


def get_all_galaxies(space):
    galaxies = []
    for x, row in enumerate(space):
        for y, galaxy in enumerate(row):
            if galaxy == '#':
                galaxies.append((x, y))
    return galaxies


def taxicab_distance(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x2 - x1) + abs(y2 - y1)


def part_one(data):
    space = [[*line] for line in data]
    space = expand_space(space)
    galaxies = get_all_galaxies(space)
    distances = []
    for i, gal1 in enumerate(galaxies):
        for gal2 in galaxies[i + 1:]:
            distances.append(taxicab_distance(gal1, gal2))
    print(sum(distances))


def get_empty_spaces(matrix):
    return [i for i, row in enumerate(matrix) if all(c == '.' for c in row)]


def count_empty_spaces_between(lst, a, b):
    if a > b:
        a, b = b, a
    return [i for i in lst if a <= i <= b]


def galaxy_distance(a, b, h, v):
    x1, y1 = a
    x2, y2 = b

    horizontal_empty_spaces = len(count_empty_spaces_between(h, x1, x2))
    vertical_empty_spaces = len(count_empty_spaces_between(v, y1, y2))
    horizontal_space = abs(x2 - x1) - horizontal_empty_spaces
    vertical_space = abs(y2 - y1) - vertical_empty_spaces
    MULTIPLIER = 1_000_000
    return horizontal_space + MULTIPLIER * horizontal_empty_spaces \
        + vertical_space + MULTIPLIER * vertical_empty_spaces


def part_two(data):
    space = [[*line] for line in data]
    horizontal_empty_spaces = get_empty_spaces(space)
    vertical_empty_spaces = get_empty_spaces(transpose(space))
    galaxies = get_all_galaxies(space)
    distances = []
    for i, gal1 in enumerate(galaxies):
        for gal2 in galaxies[i + 1:]:
            distances.append(galaxy_distance(gal1, gal2, horizontal_empty_spaces, vertical_empty_spaces))
    print(sum(distances))


def main():
    data = read_text("input.txt")
    part_one(data)
    part_two(data)


if __name__ == "__main__":
    main()
