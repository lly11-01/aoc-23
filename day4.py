from collections import deque


def read_text(filename):
    """
    Reads a .txt file with the given filename and returns a list of newline-separated entries
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f]


def part_one(data):
    total = 0
    for line in data:
        _, numbers = line.split(": ")
        winning_numbers, possessed_numbers = numbers.split(" | ")
        winning_numbers = list(map(int, winning_numbers.split()))
        possessed_numbers = list(map(int, possessed_numbers.split()))
        num_winners = count_winners(possessed_numbers, winning_numbers)
        if num_winners > 0:
            total += 2 ** (num_winners - 1)
    print(total)


def count_winners(numbers, winners):
    count = 0
    for number in numbers:
        if number in winners:
            count += 1
    return count


def part_two(data):
    total = 0
    queue = deque()
    total_cards = len(data)
    winning_numbers, possessed_numbers = [], []
    for line in data:
        _, numbers = line.split(": ")
        w, p = numbers.split(" | ")
        winning_numbers.append(list(map(int, w.split())))
        possessed_numbers.append(list(map(int, p.split())))
        queue.append(0)

    for i in range(total_cards):
        assert len(queue) == total_cards - i
        num_cards_in_play = queue.popleft() + 1
        total += num_cards_in_play
        num_winners = count_winners(possessed_numbers[i], winning_numbers[i])
        if num_winners > 0:
            queue = duplicate_cards(queue, num_winners, num_cards_in_play)
    print(total)


def duplicate_cards(queue, times_to_copy, num_to_copy):
    stack = []
    while queue and times_to_copy > 0:
        stack.append(queue.popleft() + num_to_copy)
        times_to_copy -= 1
    while stack:
        queue.appendleft(stack.pop())
    return queue


# Alternative solution using only a regular queue instead of a deque
# i.e. no appendleft allowed
def duplicate_cards(queue, times_to_copy, num_to_copy):
    new_queue = deque()
    while queue and times_to_copy > 0:
        new_queue.append(queue.popleft() + num_to_copy)
        times_to_copy -= 1
    while queue:
        new_queue.append(queue.popleft())
    return new_queue


def main():
    data = read_text("input.txt")
    part_one(data)
    part_two(data)


if __name__ == "__main__":
    main()
