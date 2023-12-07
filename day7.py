def read_text(filename):
    """
    Reads a .txt file with the given filename and returns a list of newline-separated entries
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f]


def get_hand_type(hand):
    sorted_hand = sorted(hand)
    sorted_hand = sorted(sorted_hand, key=lambda x: hand.count(x), reverse=True)
    if sorted_hand[0] == sorted_hand[4]:
        return '7'  # Five of a kind
    elif sorted_hand[0] == sorted_hand[3]:
        return '6'  # Four of a kind
    elif sorted_hand[0] == sorted_hand[2]:
        if sorted_hand[3] == sorted_hand[4]:
            return '5'  # Full house
        else:
            return '4'  # Three of a kind
    elif sorted_hand[0] == sorted_hand[1]:
        if sorted_hand[2] == sorted_hand[3]:
            return '3'  # Two pair
        else:
            return '2'  # One pair
    else:
        return '1'  # High card


def get_hand_score(hand):
    hand, _ = hand
    order, score = "AKQJT98765432", "FEDCB98765432"
    score_table = dict(zip(order, score))
    type = get_hand_type(hand)
    hand_score = "".join([score_table[x] for x in hand])
    return int(f"0x{type}{hand_score}", 16)


def part_one(data):
    hands = dict(line.split() for line in data)
    hands = {k: int(v) for k, v in hands.items()}
    hands = dict(sorted(hands.items(), key=get_hand_score))
    total = sum(x * y for x, y in zip(hands.values(), range(1, len(hands) + 1)))
    print(total)


def convert_jokers(hand):
    if hand[0] == hand[-1] == 'J' or 'J' not in hand:
        return hand
    for num in hand:
        if num != 'J':
            break
    return [num if x == 'J' else x for x in hand]


def get_hand_type2(hand):
    sorted_hand = sorted(hand)
    sorted_hand = sorted(sorted_hand, key=lambda x: hand.count(x), reverse=True)
    sorted_hand = sorted(sorted_hand, key=lambda x: 1 if x == 'J' else 0, reverse=True)
    sorted_hand = convert_jokers(sorted_hand)
    if sorted_hand[0] == sorted_hand[4]:
        return '7'  # Five of a kind
    elif sorted_hand[0] == sorted_hand[3]:
        return '6'  # Four of a kind
    elif sorted_hand[0] == sorted_hand[2]:
        if sorted_hand[3] == sorted_hand[4]:
            return '5'  # Full house
        else:
            return '4'  # Three of a kind
    elif sorted_hand[0] == sorted_hand[1]:
        if sorted_hand[2] == sorted_hand[3]:
            return '3'  # Two pair
        else:
            return '2'  # One pair
    else:
        return '1'  # High card


def get_hand_score2(hand):
    hand, _ = hand
    order, score = "AKQT98765432J", "FEDCB98765432"
    score_table = dict(zip(order, score))
    type = get_hand_type2(hand)
    hand_score = "".join([score_table[x] for x in hand])
    return int(f"0x{type}{hand_score}", 16)


def part_two(data):
    hands = dict(line.split() for line in data)
    hands = {k: int(v) for k, v in hands.items()}
    hands = dict(sorted(hands.items(), key=get_hand_score2))
    total = sum(x * y for x, y in zip(hands.values(), range(1, len(hands) + 1)))
    print(total)


def main():
    data = read_text("input.txt")
    part_one(data)
    part_two(data)


if __name__ == "__main__":
    main()
