
from collections import defaultdict

def count_characters(s):
    char_dict = defaultdict(int)
    for c in s:
        char_dict[c.lower()] += 1
    return dict(char_dict)


def count_characters_test(s, reference_dict):
    func_dict = count_characters(s)
    for c in s:
        if func_dict[c.lower()] != reference_dict[c.lower()]:
            return False
    return True

s = "A cat!!!"
cat_dict = {'a': 2, 'c': 1, 't': 1, ' ': 1, '!': 3}

assert count_characters_test( s, cat_dict)
print(count_characters(s))
