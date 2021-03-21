

letter_dict = {
    ' ': 0, 'a': 1, 'b': 2, 'c': 3, 'd': 4,
    'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
    'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14,
    'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
    't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24,
    'y': 25, 'z': 26
    }
letter_values = set(letter_dict.values())
reverse_letter_dict = {
    0: ' ', 1: 'a', 2: 'b', 3: 'c', 4: 'd',
    5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i',
    10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n',
    15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's',
    20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x',
    25: 'y', 26: 'z'
}

def encode(string, a, b):
    ret_arr = []
    for c in string:
        ret_arr.append(a * letter_dict[c] + 3)
    return ret_arr

def decode(numbers, a, b):
    ret_s = ""
    for n in numbers:
        n_decoded = (n - b) / a 
        if n_decoded not in letter_values:
            return False
        ret_s += reverse_letter_dict[n_decoded]
    return ret_s

result_arr = [5, 3, 9, 5, 43]
assert(encode("a cat", 2, 3) == result_arr)

message = [377,
 717,
 71,
 513,
 105,
 921,
 581,
 547,
 547,
 105,
 377,
 717,
 241,
 71,
 105,
 547,
 71,
 377,
 547,
 717,
 751,
 683,
 785,
 513,
 241,
 547,
 751]

for a in range(1, 101):
    for b in range(101):
        if decode(message, a, b):
            print( decode(message, a, b))



