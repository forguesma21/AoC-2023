from input_2 import puzzle2


def find_id(to_find: str):
    first_split = to_find.find(':')
    split_one = to_find[:first_split]
    found_id = ''
    for character in split_one:
        if character.isdigit():
            found_id += character
        else:
            continue
    return int(found_id)


test_games = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''


def format_input(game_list):
    formated_list = []
    lines = game_list.split('\n')
    # print(lines)
    for line in lines:

        game_set = []
        first_split = line.find(':')
        color_set = line[first_split+2:]
        # print(color_set)

        # set le game_id
        game_id = find_id(line)
        game_set.append(game_id)

        separator = color_set.split(';')
        # print(separator)

        for colors in separator:
            game = {}
            elements = colors.split(', ')

            for element in elements:
                qty, color = element.split()
                game[color] = int(qty)
            game_set.append(game)

        formated_list.append(game_set)

    return formated_list


# fonction qui mets dans une liste les id des game qui respectent les limites
def get_id_limits(game_lists, qty_red, qty_green, qty_blue):
    total_ids = 0
    game_list = format_input(game_lists)

    for games in game_list:

        add_validation = True
        for game_dict in games[1:]:
            if 'blue' in game_dict and game_dict['blue'] > qty_blue:
                add_validation = False
                break
            if 'green' in game_dict and game_dict['green'] > qty_green:
                add_validation = False
                break
            if 'red' in game_dict and game_dict['red'] > qty_red:
                add_validation = False
                break

        if add_validation:
            total_ids += int(games[0])

    return total_ids


print(get_id_limits(puzzle2, 12, 13, 14))

# Essai 1 : 2176
