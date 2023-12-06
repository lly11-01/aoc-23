def read_text(filename):
    """
    Reads a .txt file with the given filename and returns a list of newline-separated entries
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f]


def part_one(data):
    race_durations = map(int, data[0].split()[1:])
    record_distances = map(int, data[1].split()[1:])
    margin_of_error = 1
    for duration, best_dist in zip(race_durations, record_distances):
        beating_distances = [t for t in range(1, duration) if t * (duration - t) > best_dist]
        margin_of_error *= len(beating_distances)
    print(margin_of_error)


def part_two(data):
    race_duration = int("".join(data[0].split()[1:]))
    record_distance = int("".join(data[1].split()[1:]))
    beating_distances = [t for t in range(1, race_duration) if t * (race_duration - t) > record_distance]
    print(len(beating_distances))

def main():
    data = read_text("day6_input.txt")
    part_one(data)
    part_two(data)


if __name__ == "__main__":
    main()
