from input_1 import calibration_doc

# one number string
test_input = '''1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet'''

calibration = '''nkzjrdqrmpztpqninetwofour1znnkd
s5sevenxrdfr4mhpstgbjcfqckronesix
3four4
sfdrtpvspsixsn5zbqmggb8vgkjseight
'''


def get_numerics(calib):
    calib_format = calib.split('\n')
    result = []
    for item in calib_format:
        numeric_chars = ''.join(filter(str.isdigit, item))
        result.append(numeric_chars)
    return result


def calib_value(calib: list) -> list:
    result = []
    for item in calib:
        number_len = len(item)
        match number_len:
            case 2:
                result.append(int(item))
            case 1:
                result.append(int(item*2))
            case other:
                result.append(int(item[0]+item[-1]))
    return result


def total_value(raw_values: list) -> int:
    number = 0
    values = calib_value(raw_values)
    for item in values:
        number += item
    return number


if __name__ == "__main__":
    test1 = get_numerics(calibration_doc)
    print(total_value(test1))

# Essai 1 : 56506
