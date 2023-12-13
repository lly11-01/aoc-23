import math


def read_text(filename):
    """
    Reads a .txt file with the given filename and returns a list of newline-separated entries
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f]


def parse_mappings(data):
    conversions = []
    header = False
    data.append("")
    maps = []
    for line in data:
        # print(line)
        if not line:
            if maps:
                conversions.append(maps)
                maps = []
            header = True
            continue
        if header:
            header = False
            continue
        maps.append(tuple(map(int, line.split())))
    return conversions


def map_seed(input, mappings):
    for mapping in mappings:
        dest, src, step = mapping
        if src <= input < src + step:
            return dest + (input - src)
    return input


def seed_to_location(seed, conversions):
    for mappings in conversions:
        seed = map_seed(seed, mappings)
    return seed


def part_one(data):
    seeds = list(map(int, data[0].split()[1:]))
    # print(seeds)
    conversions = parse_mappings(data[1:])
    locations = list(map(lambda x: seed_to_location(x, conversions), seeds))
    print(min(locations))


def part_two(data):
    seeds = list(map(int, data[0].split()[1:]))
    assert len(seeds) % 2 == 0
    seeds = list(zip(seeds[0::2], seeds[1::2], strict=True))
    conversions = parse_mappings(data[1:])
    lowest_location = math.inf
    for i, (start, step) in enumerate(seeds):
        # print(f"Processing {i+1} out of {len(seeds)}")
        total_seeds = range(start, start + step)
        locations = map(lambda x: seed_to_location(x, conversions), total_seeds)
        lowest_candidate = min(locations)
        if lowest_candidate < lowest_location:
            lowest_location = lowest_candidate
    print(lowest_location)


def main():
    data = read_text("input.txt")
    part_one(data)
    # part_two(data) # Run this at your own risk!


if __name__ == "__main__":
    main()
