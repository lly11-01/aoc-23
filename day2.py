def read_text(filename):
    """
    Reads a .txt file with the given filename and returns a list of newline-separated entries
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f]


MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


def invalid_state(state_str):
    cubes = state_str.split(', ')
    for cube in cubes:
        count, colour = cube.split(' ')
        count = int(count)
        if colour == 'red' and count > MAX_RED:
            return True
        elif colour == 'green' and count > MAX_GREEN:
            return True
        elif colour == 'blue' and count > MAX_BLUE:
            return True
    return False


def invalid_game(states):
    states = states.split('; ')
    states = [invalid_state(s) for s in states]
    return any(states)


def part_one(data):
    total = 0
    for entry in data:
        game, states = entry.split(': ')
        game_number = int(game.split(" ")[-1])
        total += 0 if invalid_game(states) else game_number
    print(total)


def parse_colours(state_str):
    cubes = state_str.split(', ')
    counts = [0, 0, 0]
    for cube in cubes:
        count, colour = cube.split(' ')
        count = int(count)
        if colour == 'red':
            counts[0] += count
        elif colour == 'green':
            counts[1] += count
        elif colour == 'blue':
            counts[2] += count
    return tuple(counts)


def part_two(data):
    total = 0
    for entry in data:
        _, states = entry.split(': ')
        states = states.split('; ')
        cubes = [parse_colours(state) for state in states]
        cubes = list(map(max, zip(*cubes)))
        total += cubes[0] * cubes[1] * cubes[2]
    print(total)


def main():
    data = read_text("input.txt")
    part_one(data)
    part_two(data)


if __name__ == "__main__":
    main()
