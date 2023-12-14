def read_text(filename):
    """
    Reads a .txt file with the given filename and returns a list of newline-separated entries
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f]


def transpose(matrix):
    return list(map(list, zip(*matrix)))


def reverse(matrix):
    return [list(reversed(row)) for row in matrix]


def shift_north(mat):
    return transpose(shift_west(transpose(mat)))


def shift_south(mat):
    return transpose(reverse(transpose(shift_north(transpose(reverse(transpose(mat)))))))


def shift_east(mat):
    return reverse(shift_west(reverse(mat)))


def shift_west(mat):
    def helper(row):
        for i, rock in enumerate(row):
            if rock == 'O':
                j = i
                while j > 0 and row[j - 1] == '.':
                    j -= 1
                row[i], row[j] = row[j], row[i]
        return row
    return [helper(x) for x in mat]


def part_one(data):
    rocks = shift_north(data)
    print(sum(row.count('O') * weight for row, weight in zip(rocks, range(len(rocks), 0, -1))))


def same(curr_state, state):
    return all(row1 == row2 for row1, row2 in zip(curr_state, state))


def same_state(past_states, curr_state):
    j, current = curr_state
    for i, state in reversed(past_states):
        if same(current, state):
            return j - i


def test(data, times):
    for i in range(times):
        data = shift_north(data)
        data = shift_west(data)
        data = shift_south(data)
        data = shift_east(data)
    return data


def part_two(data):
    orig_data = data

    TIMES = 1_000_000_000
    past_cycles = []
    for i in range(TIMES):
        data = shift_north(data)
        data = shift_west(data)
        data = shift_south(data)
        data = shift_east(data)
        if (loop_size := same_state(past_cycles, (i, data))) is not None:
            past_cycles = past_cycles[-loop_size:]
            offset = past_cycles[0][0]
            break
        past_cycles.append((i, data))

    index = (TIMES - 1 - offset) % loop_size
    final_rocks = past_cycles[index][1]

    assert same(final_rocks, test(orig_data, offset + index + 1))

    print(sum(row.count('O') * weight for row, weight in zip(final_rocks, range(len(final_rocks), 0, -1))))


def main():
    data = read_text("input.txt")
    part_one(data)
    part_two(data)


if __name__ == "__main__":
    main()
