from input_1 import calibration_doc

str_digit = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'

}

real_test = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen'''

str_test = '''eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
six92onesix
fivefivefourfour8four3
three3ninefive
'''

str_test2 = '''nkzjrdqrmpztpqninetwofour1znnkd
s5sevenxrdfr4mhpstgbjcfqckronesix
3four4
sfdrtpvspsixsn5zbqmggb8vgkjseight
three3ninefive'''

test_case = '''fnm3oneightsdn
'''


def replace_words(calib, replacements):
    calib_format = calib.split('\n')
    for key, value in replacements.items():
        for i, string in enumerate(calib_format):
            index = string.find(key)
            updated_index = index + len(key)
            while index != -1:  # cherche toutes les occ. de key de la boucle
                updated_index = index + len(key)
                # print(updated_index)
                # print(string[updated_index])
                if updated_index < len(string) and string[updated_index].isdigit():
                    number_d = string[updated_index]
                    calib_format[i] = string[:updated_index] + \
                        value + number_d + string[updated_index+1:]
                else:
                    calib_format[i] = string[:updated_index] + \
                        value + string[updated_index-1] + \
                        string[updated_index:]
                # print(calib_format)
                index = string.find(key, updated_index)
    return calib_format


def replace_words2(calib, replacements):
    for key, value in replacements.items():
        index = calib.find(key)
        # print(index)
        while index != -1:
            updated_index = index + len(key)
            if updated_index < len(calib) and calib[updated_index].isalpha():
                calib = calib[:updated_index] + value + calib[updated_index -
                                                              1] + calib[updated_index:]
            else:
                calib = calib[:updated_index] + value + calib[updated_index -
                                                              1:] if updated_index > 0 else value + calib[updated_index:]
                # calib = calib[:updated_index] + value + calib[updated_index -
                # 1] + calib[updated_index:]
            index = calib.find(key, updated_index)
    return calib


def get_numerics(calib_to_format):
    calib = replace_words2(calib_to_format, str_digit)
    calib = calib.split('\n')
    # print(calib)
    result = []
    for item in calib:
        numeric_chars = ''.join(filter(str.isdigit, item))
        result.append(numeric_chars)
    # print(result)
    return result


def calib_value(calib: list) -> list:
    result = []
    for item in calib:
        number_len = len(item)
        match number_len:
            case 2:
                result.append(item)
            case 1:
                result.append(item*2)
            case _:
                result.append(item[0]+item[-1])
    return result


def total_value(raw_values: list) -> int:
    number = 0
    values = calib_value(raw_values)
    for item in values:
        number += int(item)
    return number


if __name__ == "__main__":
    # utiliser get_numerics sur l'input
    # ensuite total_value

    # res2 = replace_words2(real_test, str_digit)
    res2 = get_numerics(calibration_doc)
    # res2 = calib_value(res2)
    print(total_value(res2))

    # print(replace_words2(calibration_doc, str_digit))

    # te = get_numerics(str_test)


# Essai 1 : 56727 --> too high
# Essai 2 : 57015 --> too high .. again
# Essai 3 : 56727 -- > too high
# Essai 4 : 55954 -- > too low
# Essai 5 : 56017
