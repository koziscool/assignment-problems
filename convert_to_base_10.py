
def convert_to_base_10(binum):
    s_binum_reversed = str(binum)[::-1]
    binary_exponent = 0
    ret_int = 0
    for c in s_binum_reversed:
        ret_int += int(c) * (2 ** binary_exponent)
        binary_exponent += 1
    return ret_int


def convert_to_base_10_test(n, value):
    return convert_to_base_10(n) == value


assert convert_to_base_10_test(10011, 19)
print(convert_to_base_10(10011))
