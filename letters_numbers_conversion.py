
def convert_to_numbers(s):
    letter_dict = {
        ' ': 0, 'a': 1, 'b': 2, 'c': 3, 'd': 4,
        'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
        'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14,
        'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
        't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24,
        'y': 25, 'z': 26
    }
    ret_arr = []
    for c in s:
        ret_arr.append(letter_dict[c])
    return ret_arr


def convert_to_letters(arr):
    number_dict = {
        0: ' ', 1: 'a', 2: 'b', 3: 'c', 4: 'd',
        5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i',
        10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n',
        15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's',
        20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x',
        25: 'y', 26: 'z'
    }
    ret_s = ""
    for elt in arr:
        ret_s += number_dict[elt]
    return ret_s


def letters_to_numbers_unit_test(s, arr):
    print("testing convert_to_numbers on input '", s, "'", sep='')
    assert convert_to_numbers(s) == arr
    print("PASSED")


def numbers_to_letters_unit_test(arr, s):
    print('testing convert_to_letters on input', arr)
    assert convert_to_letters(arr) == s
    print("PASSED")


print()
numbers_to_letters_unit_test([1, 0, 3, 1, 20], 'a cat')
print()
letters_to_numbers_unit_test('batman', [2, 1, 20, 13, 1, 14])
