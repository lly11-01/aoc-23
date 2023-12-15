def read_text(filename):
    """
    Reads a .txt file with the given filename and returns a list of newline-separated entries
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f]


def HASH(s):
    total = 0
    for c in s:
        total += ord(c)
        total *= 17
        total %= 256
    return total


def part_one(data):
    steps, = data
    steps = steps.split(',')
    print(sum(HASH(s) for s in steps))


class Lens:
    def __init__(self, s):
        self.operator = '=' if '=' in s else '-'
        self.label, length = s.split(self.operator)
        if not length:
            assert self.operator == '-'
        self.focal_length = int(length) if length else None
        self.hash = HASH(self.label) + 1

    def __eq__(self, other):
        return self.label == other.label

    def __repr__(self):
        return f"{self.label}{self.operator}{self.focal_length if self.focal_length is not None else ''}"


def part_two(data):
    steps, = data
    steps = steps.split(',')
    steps = [Lens(s) for s in steps]
    boxes = {}
    for lens in steps:
        box_num = lens.hash
        if box_num not in boxes:
            boxes[box_num] = []
        try:
            i = boxes[box_num].index(lens)
            if lens.operator == '=':
                boxes[box_num][i] = lens
            else:
                boxes[box_num].pop(i)
        except ValueError:
            if lens.operator == '=':
                boxes[box_num].append(lens)
    print(sum(sum(k * i * l.focal_length for i, l in zip(range(1, len(v) + 1), v)) for k, v in boxes.items() if v))


def main():
    data = read_text("input.txt")
    part_one(data)
    part_two(data)


if __name__ == "__main__":
    main()
