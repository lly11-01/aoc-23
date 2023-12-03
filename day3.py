from pprint import pprint


def read_text(filename):
    """
    Reads a .txt file with the given filename and returns a list of newline-separated entries
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f]


def write_to_file(matrix, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for row in matrix:
            f.write(''.join(row) + '\n')


def grow(matrix):
    matrix_copy = [row.copy() for row in matrix]
    for row_idx, row in enumerate(matrix_copy):
        for col_idx, entry in enumerate(row):
            if entry:
                row_idx_min = max(0, row_idx - 1)
                row_idx_max = min(len(row) - 1, row_idx + 1)
                col_idx_min = max(0, col_idx - 1)
                col_idx_max = min(len(matrix) - 1, col_idx + 1)
                for i in range(row_idx_min, row_idx_max + 1):
                    for j in range(col_idx_min, col_idx_max + 1):
                        matrix[i][j] = True


def part_one(data):
    matrix = [[x.strip() for x in line] for line in data]
    # print(matrix)
    not_symbols = '1234567890.'
    digits = '1234567890'
    symbol_matrix = [[c not in not_symbols for c in row] for row in matrix]
    # pprint(symbol_matrix)
    grow(symbol_matrix)
    digits_matrix = [[c in digits for c in row] for row in matrix]
    # pprint(symbol_matrix)
    # print(digits_matrix)
    adj_matrix = [[None] * len(digits_matrix[0]) for _ in range(len(digits_matrix))]
    adj_matrix2 = [[None] * len(digits_matrix[0]) for _ in range(len(digits_matrix))]
    for i in range(len(digits_matrix)):
        for j in range(len(digits_matrix[0])):
            adj_matrix[i][j] = digits_matrix[i][j] & symbol_matrix[i][j]
            adj_matrix2[i][j] = ('T' if adj_matrix[i][j] else 'F') if digits_matrix[i][j] else matrix[i][j]
    # pprint(adj_matrix)
    # write_to_file(adj_matrix2, 'day3_output.txt')
    numbers = get_adj_numbers(matrix, adj_matrix)
    print(sum(numbers))


def get_adj_numbers(digits, adjacency):
    numbers = []
    current_number = ''
    for row_idx, row in enumerate(digits):
        for col_idx, entry in enumerate(row):
            if entry in '1234567890':
                current_number += entry
            elif current_number:
                # print(current_number)
                max_col_idx = col_idx
                min_col_idx = max_col_idx - len(current_number)
                is_adjacent = adjacency[row_idx][min_col_idx:max_col_idx]
                if any(is_adjacent):
                    numbers.append(int(current_number))
                # print(is_adjacent)
                current_number = ''
        if current_number:
            max_col_idx = col_idx
            min_col_idx = max_col_idx - len(current_number)
            is_adjacent = adjacency[row_idx][min_col_idx:max_col_idx]
            if any(is_adjacent):
                numbers.append(int(current_number))
            # print(is_adjacent)
            current_number = ''
    return numbers


class Gear:
    def __init__(self, symbol):
        self.symbol = symbol
        self.numbers = []

    def __repr__(self):
        return "G" + self.symbol + str(len(self.numbers))

    def isdigit(self):
        return False


def part_two(data):
    matrix = [[x.strip() for x in line] for line in data]
    gears = []
    not_symbols = '1234567890.'
    for row_idx, row in enumerate(matrix):
        for col_idx, entry in enumerate(row):
            if entry not in not_symbols:
                gear = Gear(entry)
                matrix[row_idx][col_idx] = gear
                gears.append(gear)

    # pprint(matrix)
    add_adj_numbers_to_gears(matrix)
    # pprint(matrix)
    valid_gears = [gear for gear in gears if len(gear.numbers) == 2]
    valid_gears = [gear.numbers[0] * gear.numbers[1] for gear in valid_gears]
    print(sum(valid_gears))

def add_adj_numbers_to_gears(matrix):
    current_number = ''
    for row_idx, row in enumerate(matrix):
        for col_idx, entry in enumerate(row):
            if entry.isdigit():
                current_number += entry
            elif current_number:
                row_idx_min = max(0, row_idx - 1)
                row_idx_max = min(len(row) - 1, row_idx + 1)

                max_col_idx = col_idx
                min_col_idx = max_col_idx - len(current_number)

                max_col_idx = min(len(row) - 1, max_col_idx)
                min_col_idx = max(0, min_col_idx - 1)

                add_adj_gears(int(current_number), matrix, row_idx_min, row_idx_max, min_col_idx, max_col_idx)
                current_number = ''
        if current_number:
            row_idx_min = max(0, row_idx - 1)
            row_idx_max = min(len(row) - 1, row_idx + 1)

            max_col_idx = col_idx
            min_col_idx = max_col_idx - len(current_number)

            max_col_idx = min(len(row) - 1, max_col_idx)
            min_col_idx = max(0, min_col_idx - 1)

            add_adj_gears(int(current_number), matrix, row_idx_min, row_idx_max, min_col_idx, max_col_idx)
            current_number = ''

def add_adj_gears(number, matrix, row_min, row_max, col_min, col_max):
    for row in range(row_min, row_max+1):
        for col in range(col_min, col_max+1):
            entry = matrix[row][col]
            if isinstance(entry, Gear):
                # print(entry, "is next to", str(number))
                entry.numbers.append(number)

def main():
    data = read_text("input.txt")
    part_one(data)
    part_two(data)


if __name__ == "__main__":
    main()
