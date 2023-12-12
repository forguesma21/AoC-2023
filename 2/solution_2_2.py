from input_2 import puzzle2
from functools import reduce
from solution_2 import find_id, format_input

test_games = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''


def get_min(game_lists):
    total_ids = 0
    game_list = format_input(game_lists)

    for games in game_list:
        format_game = games[1:]

        # get min values for each keys
        keys_game = set().union(*(x.keys() for x in format_game))
        min_keys = {key: max(x[key] for x in format_game if key in x)
                    for key in keys_game}
        power_number = reduce(lambda x, y: x*y, min_keys.values())
        total_ids += power_number

    return total_ids


if __name__ == "__main__":
    print(get_min(puzzle2))

    # Essai 1 : 63700
