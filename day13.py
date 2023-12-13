def read_text(filename):
    """
    Reads a .txt file with the given filename and returns a list of newline-separated entries
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f]


def transpose(matrix):
    return list(map(list, zip(*matrix)))


def is_full_reflection(matrix, row_num):
    i, j = row_num-1, row_num+2
    try:
        while True:
            assert 0 <= i < j < len(matrix)
            if matrix[i] != matrix[j]:
                return False
            i -= 1
            j += 1
    except (AssertionError, IndexError):
        return True


def find_dividing_line(matrix):
    for i, row in enumerate(matrix[:-1]):
        if row == matrix[i+1] and is_full_reflection(matrix, i):
            return i + 1
    return 0


def parse_patterns(data):
    matrices = []
    current_matrix = []
    for line in data:
        if not line:
            matrices.append(current_matrix)
            current_matrix = []
        else:
            current_matrix.append(line)
    matrices.append(current_matrix)
    return matrices


def part_one(data):
    patterns = parse_patterns(data)
    columns = [find_dividing_line(transpose(mat)) for mat in patterns]
    rows = [100 * find_dividing_line(mat) for mat in patterns]
    assert (a > 0 ^ b > 0 for a, b in zip(columns, rows))
    print(sum(columns) + sum(rows))


def off_by_one(row, row2):
    return sum(1 if a != b else 0 for a, b in zip(row, row2)) == 1


def is_almost_reflection(matrix, row_num):
    chance = True
    i, j = row_num - 1, row_num + 2
    try:
        while True:
            assert 0 <= i < j < len(matrix)
            if matrix[i] != matrix[j]:
                if off_by_one(matrix[i], matrix[j]) and chance:
                    chance = False
                else:
                    return False
            i -= 1
            j += 1
    except (AssertionError, IndexError):
        return not chance


def find_dividing_line2(matrix):
    for i, row in enumerate(matrix[:-1]):
        if off_by_one(row, matrix[i + 1]) and is_full_reflection(matrix, i):
            return i + 1
        elif row == matrix[i + 1] and is_almost_reflection(matrix, i):
            return i + 1
    return 0


def part_two(data):
    patterns = parse_patterns(data)
    columns = [find_dividing_line2(transpose(mat)) for mat in patterns]
    rows = [100 * find_dividing_line2(mat) for mat in patterns]
    assert (a > 0 ^ b > 0 for a, b in zip(columns, rows))
    print(sum(columns) + sum(rows))


def main():
    data = read_text("input.txt")
    part_one(data)
    part_two(data)


if __name__ == "__main__":
    main()
