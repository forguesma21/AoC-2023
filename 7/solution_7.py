from puzzle_input import p_input, cards_values, type_values, input2

hands_order = '''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483'''

hands_test = "KK9KK 831"


def find_type(hand: str):
    hand_values = {}
    for card in hand[0:5]:
        if card in hand_values:
            hand_values[card] += 1
        else:
            hand_values[card] = 1
    print(hand_values)
    # find the type of hand by hand_values
    count_keys = len(hand_values.keys())
    match count_keys:
        case 1:
            return 'Five of a kind'
        case 2:
            if any(value == 4 for value in hand_values.values()):
                return 'Four of a kind'
            else:
                return 'Full house'
        case 3 if any(value == 3 for value in hand_values.values()):
            return 'Three of a kind'
        case 3:
            return 'Two pairs'
        case 4:
            return 'One pair'
        case 5:
            return 'High card'


def format_input(puzzle: str) -> list:
    basic_list = []
    lines = puzzle.split('\n')
    for line in lines:
        sequence = [part.strip() for part in line.split(' ') if part.strip()]
        type = find_type(line)
        hand = sequence[0]
        hand_value = type_values.get(type)
        amount = int(sequence[1])
        basic_list.append({'type': find_type(line), 'hand': hand,
                           'hand_value': hand_value, 'amount': amount})
    # sorted_list = sorted(basic_list, key=lambda x: x['hand_value'])
    return basic_list


def get_rank(hands: str) -> list:
    sorted_hand_value_num = []
    hand = format_input(hands)
    # print(hand)
    for value in range(1, 8):
        # print(value)
        hand_value_num = [d for d in hand if d['hand_value'] == value]
        # print(hand_value_num)
        sorted_hand_value_num += sorted(hand_value_num, key=lambda hand: [
            cards_values[card] for card in hand['hand']], reverse=False)
    # print(sorted_hand_value_num)
    return sorted_hand_value_num


def total_winnings(final_rank):
    amount = 0
    for hand in final_rank:
        bid = hand.get('amount')
        rank = final_rank.index(hand) + 1
        amount += bid*rank
    return amount


if __name__ == "__main__":

    test = get_rank(p_input)
    print(total_winnings(test))
    # 247815719
