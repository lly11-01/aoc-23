import re
from functools import cache


def read_text(filename):
    """
    Reads a .txt file with the given filename and returns a list of newline-separated entries
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f]


@cache
def get_all_combinations(str_to_match, regex):
    if '?' not in str_to_match:
        return 1 if re.match(pattern=regex, string=str_to_match) else 0
    return get_all_combinations(str_to_match.replace('?', '#', 1), regex) \
        + get_all_combinations(str_to_match.replace('?', '.', 1), regex)


def make_regex(nums):
    return ''.join(["^[.]*", "[.]+".join(f"[#]{{{i}}}" for i in nums), "[.]*$"])


# Original, slower brute force solution
def part_one(data):
    records = [line.split(" ") for line in data]
    records = [(line[0], list(map(int, line[1].split(',')))) for line in records]
    records = [(line[0], make_regex(line[1])) for line in records]
    print(sum(get_all_combinations(*line) for line in records))


# Faster version using memoization technique from part_two
# def part_one(data):
#     records = [line.split(" ") for line in data]
#     records = [(line[0] + '.', tuple(map(int, line[1].split(',')))) for line in records]
#     print(sum(num_combinations(record, nums) for record, nums in records))


@cache
def num_combinations(str_to_match, blocks_left):
    # print(f"num_combinations({str_to_match=}, {blocks_left=})")
    if not str_to_match:
        return 1 if not blocks_left else 0
    if not blocks_left:
        return 1 if '#' not in str_to_match else 0
    char = str_to_match[0]
    current_block = blocks_left[0]
    if char == '.':
        return num_combinations(str_to_match[1:], blocks_left)
    if char == '#':
        n = current_block
        # next n characters must not be .
        next_n_chars = str_to_match[:n]
        if '.' in next_n_chars:
            return 0
        # after the n characters, it must be a . or $
        if str_to_match[n] == '#':
            return 0
        return num_combinations(str_to_match[n+1:], blocks_left[1:])
    # try to replace ? with a . or a #
    return num_combinations('.' + str_to_match[1:], blocks_left) + \
        num_combinations('#' + str_to_match[1:], blocks_left)


def part_two(data):
    records = [line.split(" ") for line in data]
    records = [('?'.join([line[0]] * 5) + '.', 5 * tuple(map(int, line[1].split(',')))) for line in records]
    print(sum(num_combinations(record, nums) for record, nums in records))


def main():
    data = read_text("input.txt")
    part_one(data)
    part_two(data)


if __name__ == "__main__":
    main()
