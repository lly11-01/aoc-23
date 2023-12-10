def read_text(filename):
    """
    Reads a .txt file with the given filename and returns a list of newline-separated entries
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f]


class Pipe:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.visited = True if direction == 'S' else False
        self.distance = 0 if direction == 'S' else -1
        self.loop = True if direction == 'S' else False
        self.outside = False
        # East =  x, y+1
        # West =  x, y-1
        # North = x-1, y
        # South = x+1, y
        if direction == '|':
            self.dests = (x - 1, y), (x + 1, y)
        elif direction == '-':
            self.dests = (x, y + 1), (x, y - 1)
        elif direction == 'L':
            self.dests = (x - 1, y), (x, y + 1)
        elif direction == 'J':
            self.dests = (x - 1, y), (x, y - 1)
        elif direction == '7':
            self.dests = (x + 1, y), (x, y - 1)
        elif direction == 'F':
            self.dests = (x + 1, y), (x, y + 1)
        elif direction == 'S':
            self.dests = "Start"
        else:
            self.dests = None

    def __repr__(self):
        return f"{self.direction} Pipe @ {self.coords}"

    @property
    def coords(self):
        return self.x, self.y


def get_start_coords(matrix):
    for row in matrix:
        for pipe in row:
            if pipe.dests == "Start":
                return pipe.coords


def access_coord(matrix, coords):
    x, y = coords
    if x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]):
        return Pipe(x, y, '.')
    return matrix[x][y]


def all_explored(matrix):
    return all(all(p.visited for p in row) for row in matrix)


def part_one(data):
    matrix = [[*line] for line in data]
    pipe_matrix = [[Pipe(x, y, c) for y, c in enumerate(row)] for x, row in enumerate(matrix)]
    start_coords_x, start_coords_y = get_start_coords(pipe_matrix)
    next_pipes = (access_coord(pipe_matrix, (start_coords_x - 1, start_coords_y)),
                  access_coord(pipe_matrix, (start_coords_x + 1, start_coords_y)),
                  access_coord(pipe_matrix, (start_coords_x, start_coords_y - 1)),
                  access_coord(pipe_matrix, (start_coords_x, start_coords_y + 1)))
    next_pipes = [pipe for pipe in next_pipes if pipe.dests is not None]
    next_pipes = [pipe for pipe in next_pipes if (start_coords_x, start_coords_y) in pipe.dests]
    # print(next_pipes)
    current_distance = 0
    while not all_explored(pipe_matrix) and next_pipes:
        # print("Hello")
        current_distance += 1
        exploring_pipes = next_pipes
        next_pipes = []
        for pipe in exploring_pipes:
            # print(f"Exploring {pipe}")
            pipe.visited = True
            pipe.distance = current_distance
            next_pipes += [next_pipe for coord in pipe.dests if
                           not (next_pipe := access_coord(pipe_matrix, coord)).visited]
        next_pipes = list(set(next_pipes))
        # print(next_pipes)
    print(max(max(pipe.distance for pipe in row) for row in pipe_matrix))


def part_two(data):
    matrix = [[*line] for line in data]
    pipe_matrix = [[Pipe(x, y, c) for y, c in enumerate(row)] for x, row in enumerate(matrix)]
    start_coords_x, start_coords_y = get_start_coords(pipe_matrix)
    next_pipes = (access_coord(pipe_matrix, (start_coords_x - 1, start_coords_y)),
                  access_coord(pipe_matrix, (start_coords_x + 1, start_coords_y)),
                  access_coord(pipe_matrix, (start_coords_x, start_coords_y - 1)),
                  access_coord(pipe_matrix, (start_coords_x, start_coords_y + 1)))
    next_pipes = [pipe for pipe in next_pipes if pipe.dests is not None]
    next_pipes = [pipe for pipe in next_pipes if (start_coords_x, start_coords_y) in pipe.dests]
    # print(next_pipes)
    current_distance = 0
    while not all_explored(pipe_matrix) and next_pipes:
        # print("Hello")
        current_distance += 1
        exploring_pipes = next_pipes
        next_pipes = []
        for pipe in exploring_pipes:
            # print(f"Exploring {pipe}")
            pipe.visited = True
            pipe.loop = True
            pipe.distance = current_distance
            next_pipes += [next_pipe for coord in pipe.dests if
                           not (next_pipe := access_coord(pipe_matrix, coord)).visited]
        next_pipes = list(set(next_pipes))
    flood_fill(pipe_matrix)
    for row in pipe_matrix:
        for y, pipe in enumerate(row):
            if pipe.loop or pipe.outside:
                continue
            num_walls_left, num_walls_right = count_walls_left(row, y), count_walls_right(row, y)
            assert num_walls_left % 2 == num_walls_right % 2, f"{row[y]} Error: {(num_walls_left, num_walls_right)}"
            row[y].outside = not num_walls_left % 2
    for row in pipe_matrix:
        print(['.' if pipe.loop else 'O' if pipe.outside else 'X' for pipe in row])
    print(sum(sum(int(not pipe.loop and not pipe.outside) for pipe in row) for row in pipe_matrix))


def count_walls_left(row, idx):
    prev = None
    walls = 0
    # str = ""
    for pipe in row[:idx]:
        if not pipe.loop:
            continue
        # str += pipe.direction
        if pipe.direction == '|':
            prev = None
            walls += 1
        elif pipe.direction == '-':
            continue
        elif pipe.direction == 'L' or pipe.direction == 'F':
            prev = pipe.direction
            walls += 1
        elif pipe.direction == '7':
            walls += 1 if prev != 'L' else 0
            prev = None
        elif pipe.direction == 'J':
            walls += 1 if prev != 'F' else 0
            prev = None
        elif pipe.direction == 'S':
            prev = None
            walls += 1

    # print(str)
    return walls


def count_walls_right(row, idx):
    prev = None
    walls = 0
    # str = ""
    for pipe in row[idx + 1:]:
        if not pipe.loop:
            continue
        # str += pipe.direction
        if pipe.direction == '|':
            prev = None
            walls += 1
        elif pipe.direction == '-':
            continue
        elif pipe.direction == 'L' or pipe.direction == 'F':
            prev = pipe.direction
            walls += 1
        elif pipe.direction == '7':
            walls += 1 if prev != 'L' else 0
            prev = None
        elif pipe.direction == 'J':
            walls += 1 if prev != 'F' else 0
            prev = None
        elif pipe.direction == 'S':
            prev = None
            walls += 1

    # print(str)
    return walls


def flood_fill(matrix):
    for y, pipe in enumerate(matrix[0]):
        if not pipe.loop:
            matrix[0][y].outside = True
            spread(matrix, (0, y))
    for y, pipe in enumerate(matrix[-1]):
        if not pipe.loop:
            matrix[-1][y].outside = True
            spread(matrix, (len(matrix) - 1, y))
    for x, pipe in enumerate(matrix):
        if not pipe[0].loop:
            matrix[x][0].outside = True
            spread(matrix, (x, 0))
    for x, pipe in enumerate(matrix):
        if not pipe[-1].loop:
            matrix[x][-1].outside = True
            spread(matrix, (x, len(matrix[0]) - 1))


def spread_next(matrix, coords):
    x, y = coords
    to_spread = []
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]):
                continue
            if (i, j) == (x, y):
                continue
            if matrix[i][j].loop:
                continue
            if matrix[i][j].outside:
                continue
            to_spread.append((i, j))
    return to_spread


def spread(matrix, coords):
    to_spread = spread_next(matrix, coords)
    # print(to_spread)
    while to_spread:
        coord = to_spread.pop()
        access_coord(matrix, coord).outside = True
        to_spread += spread_next(matrix, coord)


def main():
    data = read_text("input.txt")
    part_one(data)
    part_two(data)


if __name__ == "__main__":
    main()
