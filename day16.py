def read_text(filename):
    """
    Reads a .txt file with the given filename and returns a list of newline-separated entries
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f]


def parse_direction(d):
    table = {(0, 1): 'right', (0, -1): 'left', (1, 0): 'down', (-1, 0): 'up'}
    return table[d]


class Beam:
    i = 1

    def __init__(self, location=None, direction=None):
        location = location if location is not None else (0, 0)
        direction = direction if direction is not None else (0, 1)

        self.id = Beam.i
        Beam.i += 1

        self.location = location
        self.direction = direction

    def __str__(self):
        return f"Beam {self.id} is at {self.location} going {parse_direction(self.direction)}"

    def __repr__(self):
        return f"Beam {self.id}"


def out_of_bounds(coords, matrix):
    x, y = coords
    return (not (0 <= x < len(matrix))) or (not (0 <= y < len(matrix[0])))


def part_one(data):
    tiles = [['!' if char == '\\' else char for char in line] for line in data]
    print(traverse(tiles, start_tile=(0, 0), start_direction=(0, 1)))


def traverse(tiles, start_tile, start_direction):
    lit = [[False] * len(tiles[0]) for _ in range(len(tiles))]
    beams = [Beam(location=start_tile, direction=start_direction)]
    past_visited = []
    while beams:
        beam = beams.pop()
        if out_of_bounds(beam.location, tiles) or (beam.location, beam.direction) in past_visited:
            continue
        # beam visits location
        x, y = beam.location
        lit[x][y] = True
        past_visited.append((beam.location, beam.direction))
        if tiles[x][y] == '!':
            # right mirror;
            # right (0, 1) beam goes down (1, 0), left beam (0, -1) goes up (-1, 0),
            # up beam (-1, 0) goes left (0, -1), down beam (1, 0) goes right (0, 1)
            a, b = beam.direction
            beam.direction = b, a
        elif tiles[x][y] == '/':
            # left mirror;
            # right (0, 1) beam goes up (-1, 0), left beam (0, -1) goes down (1, 0),
            # up beam (-1, 0) goes right (0, 1), down beam (1, 0) goes left (0, -1)
            a, b = beam.direction
            beam.direction = -b, -a
        elif tiles[x][y] == '|' and beam.direction[1] != 0:
            # split beams; new beam always goes up, old beam always goes down
            new_beam_loc = beam.location[0] - 1, beam.location[1]
            beams.append(Beam(location=new_beam_loc, direction=(-1, 0)))
            beam.direction = (1, 0)
        elif tiles[x][y] == '-' and beam.direction[0] != 0:
            # split beams; new beam always goes left, old beam always goes right
            new_beam_loc = beam.location[0], beam.location[1] - 1
            beams.append(Beam(location=new_beam_loc, direction=(0, -1)))
            beam.direction = (0, 1)
        # move beam
        beam.location = tuple(l + d for l, d in zip(beam.location, beam.direction))
        beams.append(beam)
    return sum(line.count(True) for line in lit)


def debug_print(position, direction):
    print(f"Starting at {position} and going {parse_direction(direction)}...")


def part_two(data):
    tiles = [['!' if char == '\\' else char for char in line] for line in data]

    n_rows, n_cols = len(tiles), len(tiles[0])
    possible_configs = [((0, i), (1, 0)) for i in range(1, n_cols - 1)]
    possible_configs += [((i, 0), (0, 1)) for i in range(1, n_rows - 1)]
    possible_configs += [((n_rows - 1, i), (-1, 0)) for i in range(1, n_cols - 1)]
    possible_configs += [((i, n_cols - 1), (0, -1)) for i in range(1, n_rows - 1)]
    possible_configs += [((0, 0), direction) for direction in ((0, 1), (1, 0))]
    possible_configs += [((n_rows - 1, 0), direction) for direction in ((0, 1), (-1, 0))]
    possible_configs += [((0, n_cols - 1), direction) for direction in ((0, -1), (1, 0))]
    possible_configs += [((n_rows - 1, n_cols - 1), direction) for direction in ((0, -1), (-1, 0))]

    most_energized = -1
    for j, config in enumerate(possible_configs):
        # print(f"Progress: {j+1} / {len(possible_configs)}")
        # debug_print(*config)
        num_tiles = traverse(tiles, *config)
        most_energized = num_tiles if num_tiles > most_energized else most_energized
        # print(f"{num_tiles}, current highest = {most_energized} \n")
    print(most_energized)


def main():
    data = read_text("input.txt")
    part_one(data)
    part_two(data)


if __name__ == "__main__":
    main()
