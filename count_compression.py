
def count_compression(string):
    current_char, current_char_count = string[0],  1
    ret_arr = []
    for c in string[1:]:
        if c == current_char:
            current_char_count += 1
        else:
            ret_arr.append((current_char, current_char_count))
            current_char, current_char_count = c, 1
    if current_char_count > 1:
        ret_arr.append((current_char, current_char_count))

    return ret_arr

def count_decompression(compressed_string):
    ret_s = ""
    for t in compressed_string:
        for _ in range(t[1]):
            ret_s += t[0]
    return ret_s

print(count_compression('aaabbcaaaa'))
# [('a',3), ('b',2), ('c',1), ('a',4)]

print(count_compression('22344444'))
# [('2',2), ('3',1), ('4',5)]

print(count_decompression([('a',3), ('b',2), ('c',1), ('a',4)]))
# 'aaabbcaaaa'

print(count_decompression([('2',2), ('3',1), ('4',5)]))
# '22344444'
