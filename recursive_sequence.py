
def first_n_terms(n):
    ret_arr = [5]
    while len(ret_arr) < n:
        ret_arr.append(ret_arr[-1] * 3 - 4)
    return ret_arr


def first_n_terms_test(n, reference_arr):
    function_arr = first_n_terms(n)
    for i in range(len(function_arr)):
        if function_arr[i] != reference_arr[i]:
            return False
    return True


def nth_term(n):
    if n == 1:
        return 5
    return 3 * nth_term(n - 1) - 4 


def nth_term_test(n, value):
    return nth_term(n) == value

assert nth_term_test(10, 59051)

print(nth_term(10))

reference_array = [5, 11, 29, 83, 245, 731, 2189, 6563, 19685, 59051]
assert first_n_terms_test(10, reference_array)

print(first_n_terms(10))
