from pprint import pprint


def read_text(filename):
    """
    Reads a .txt file with the given filename and returns a list of newline-separated entries
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f]

def find_start(mat):
    for i, row in enumerate(mat):
        for j, val in enumerate(row):
            if val == 'S':
                return i, j

def out_of_bounds(coords, matrix):
    x, y = coords
    return (not (0 <= x < len(matrix))) or (not (0 <= y < len(matrix[0])))

def access_cell(coords, matrix):
    x, y = coords
    return matrix[x][y]

def walk(tiles, positions):
    new_positions = []
    for pos in positions:
        x, y = pos
        new_tiles = [(x-1, y), (x+1, y), (x, y-1), (x,y+1)]
        new_tiles = [tile for tile in new_tiles if not out_of_bounds(tile, tiles) and access_cell(tile, tiles) != '#']
        new_positions += new_tiles
    return list(set(new_positions))

def visualize_grid(matrix, coords_set):
    new_mat = [row.copy() for row in matrix]
    for coord in coords_set:
        x, y = coord
        assert new_mat[x][y] == '.'
        new_mat[x][y] = 'O'
    new_mat = [''.join(row) for row in new_mat]
    pprint(new_mat)

def part_one(data):
    tiles = [[*line] for line in data]
    # pprint(tiles)

    positions = [find_start(tiles)]
    tiles = [['.' if c == 'S' else c for c in line] for line in tiles]

    # print(positions)
    STEPS = 6

    for _ in range(STEPS):
        positions = walk(tiles, positions)
        # print(positions)
        # visualize_grid(tiles, positions)
    print(len(positions))


def part_two(data):
    pass


def main():
    data = read_text("day21_test.txt")
    part_one(data)
    part_two(data)


if __name__ == "__main__":
    main()
