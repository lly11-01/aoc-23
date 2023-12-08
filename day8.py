import math


def read_text(filename):
    """
    Reads a .txt file with the given filename and returns a list of newline-separated entries
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f]


def parse_graph(data):
    graph = {}
    for line in data:
        node, tmp = line.split(" = ")
        left, right = tmp.replace('(', '').replace(')', '').split(", ")
        graph[node] = {'L': left, 'R': right}
    return graph


def part_one(data):
    sequence = data[0]
    graph = parse_graph(data[2:])
    node = 'AAA'
    steps = 0
    while node != 'ZZZ':
        for direction in sequence:
            steps += 1
            node = graph[node][direction]
            if node == 'ZZZ':
                break
    print(steps)


# Do not use: hilariously inefficient first attempt
# def part_two(data):
#     sequence = data[0]
#     graph = parse_graph(data[2:])
#     nodes = [x for x in graph if x[-1] == 'A']
#     steps = 0
#     while not all(x[-1] == 'Z' for x in nodes):
#         for direction in sequence:
#             steps += 1
#             for i, node in enumerate(nodes):
#                 nodes[i] = graph[node][direction]
#             print(steps, nodes)
#             if all(x[-1] == 'Z' for x in nodes):
#                 break
#     print(steps)


def calculate_steps(graph, sequence, node):
    steps = 0
    while node[-1] != 'Z':
        for direction in sequence:
            steps += 1
            node = graph[node][direction]
            if node[-1] == 'Z':
                break
    return steps


def part_two(data):
    sequence = data[0]
    graph = parse_graph(data[2:])
    steps = []
    start_nodes = [x for x in graph if x[-1] == 'A']
    for start_node in start_nodes:
        steps.append(calculate_steps(graph, sequence, start_node))
    print(math.lcm(*steps))


def main():
    data = read_text("input.txt")
    part_one(data)
    part_two(data)


if __name__ == "__main__":
    main()
