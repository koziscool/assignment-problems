
def convert_to_base_2(decnum):
    remainder = decnum
    s_binary = ""
    while remainder > 0:
        s_binary += str(remainder % 2)
        remainder //= 2
    return int(s_binary[::-1])


def convert_to_base_2_test(n, value):
    return convert_to_base_2(n) == value

assert convert_to_base_2(19) == 10011
