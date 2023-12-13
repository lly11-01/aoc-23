def read_text(filename):
    """
    Reads a .txt file with the given filename and returns a list of newline-separated entries
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f]


def part_one(data):
    nums = []
    for i, line in enumerate(data):
        num = ''.join(x for x in line if x.isdigit())
        nums.append(int(num[0]) * 10 + int(num[-1]))
    print(sum(nums))


# def convert_to_digit(num):
#     digit_strs = {'one': '1', 'two': '2', 'three': '3',
#                   'four': '4', 'five': '5', 'six': '6',
#                   'seven': '7', 'eight': '8', 'nine': '9'}
#     occurrences = {index: digit for digit in reversed(digit_strs) if (index := num.find(digit)) > -1}
#     if not occurrences:
#         return num
#     # print(occurrences)
#     first_to_remove = occurrences[min(occurrences)]
#     num = num.replace(first_to_remove, digit_strs[first_to_remove], 1)
#     return convert_to_digit(num)

def parse_first_digit(num):
    digit_strs = {'one': '1', 'two': '2', 'three': '3',
                  'four': '4', 'five': '5', 'six': '6',
                  'seven': '7', 'eight': '8', 'nine': '9'}
    occurrences = {index: digit for digit in reversed(digit_strs) if (index := num.find(digit)) > -1}
    return digit_strs.get(occurrences.get(0, None), None)


def convert_to_digit(num):
    digits = []
    for i, char in enumerate(num):
        if char.isdigit():
            digits.append(char)
            continue
        digit = parse_first_digit(num[i:])
        if digit is None:
            continue
        digits.append(digit)
    return ''.join(digits)


def part_two(data):
    nums = []
    for i, line in enumerate(data):
        num = convert_to_digit(line)
        nums.append(int(num[0]) * 10 + int(num[-1]))
    print(sum(nums))


def main():
    data = read_text("input.txt")
    part_one(data)
    part_two(data)


if __name__ == "__main__":
    main()
