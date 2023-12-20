from input_4 import cards

test_cards = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''


def remove_items(test_list, item):

    # using list comprehension to perform the task
    res = [i for i in test_list if i != item]
    return res


def format_cards(cards: str):
    ind_cards = cards.split('\n')
    # print(ind_cards)

    all_set = []

    for card in ind_cards:

        remov_title = card.find(':')
        all_cards = card[remov_title+2:]

        # set_cards[0] : winning cards, set_cards[1]: ur cards
        set_cards = all_cards.split('|')
        all_set.append(set_cards)

    return all_set


def total_points(cards):
    pts = 0

    for all_set in cards:
        all_set[0] = (all_set[0].strip()).split(' ')
        ur_cards = (all_set[1].strip()).split(' ')
        ur_cards = remove_items(ur_cards, '')
        cards_values = 0
       # print((ur_cards))
        # print(all_set)

        for win_cards in all_set[0]:
            cnt = ur_cards.count(win_cards)
            cards_values += cnt
        print(cards_values)

        if cards_values > 0:
            pts += (2 ** (cards_values-1))

    return pts


liste_test = format_cards(test_cards)

# print(liste_test)
print(total_points(liste_test))


def compter_occurrences(liste, chaine):
    count_total = 0
    for nombre in liste:
        count_nombre = chaine.count(nombre)
        count_total += count_nombre
    return count_total


# Exemple d'utilisation
# liste_nombres = ['13', '32', '20', '16', '61']
# chaine = '61 30 68 82 17 32 24 19'

# resultat = compter_occurrences(liste_nombres, chaine)
# print(resultat)


# Essai 1 : 604 387 193 --> too high
# Essai 2 : 234 496 -> too high
