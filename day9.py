def read_text(filename):
    """
    Reads a .txt file with the given filename and returns a list of newline-separated entries
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f]


def calculate_diffs(arr):
    return [arr[i] - arr[i - 1] for i in range(1, len(arr))]


def extrapolate_values(line):
    nums = list(map(int, line.split()))
    steps = [nums]
    while not all(x == 0 for x in steps[-1]):
        steps.append(calculate_diffs(steps[-1]))
    return sum(row[-1] for row in steps)


def part_one(data):
    values = [extrapolate_values(line) for line in data]
    print(sum(values))


def extrapolate_front(line):
    nums = list(map(int, line.split()))
    steps = [nums]
    while not all(x == 0 for x in steps[-1]):
        steps.append(calculate_diffs(steps[-1]))
    return accumulate(0, lambda x, y: x - y, [row[0] for row in steps])


def accumulate(val, fn, seq):
    if not seq:
        return val
    return accumulate(fn(seq[-1], val), fn, seq[:-1])


def part_two(data):
    values = [extrapolate_front(line) for line in data]
    print(sum(values))


def main():
    data = read_text("input.txt")
    part_one(data)
    part_two(data)


if __name__ == "__main__":
    main()
