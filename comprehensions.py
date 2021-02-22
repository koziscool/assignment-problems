
def even_odd_tuples(numbers):
    return [ (n, 'even') if n % 2 == 0  else (n, 'odd') for n in numbers ]


def even_odd_tuples_test(numbers, reference_arr):
    results, index = even_odd_tuples(numbers), 0
    while index < len(numbers):
        if results[index] != reference_arr[index]:
            return False
        index += 1
    return True


def even_odd_dict(numbers):
    return { n: ('even' if n % 2 == 0  else 'odd') for n in numbers }


def even_odd_dict_test(numbers, reference_dict):
    results, index = even_odd_dict(numbers), 0
    for key in results.keys():
        if results[key] != reference_dict[key]:
            return False
        index += 1
    return True

numbers  = [1, 2, 3, 5, 8, 11]
n_tuples = [(1, 'odd'), (2, 'even'), (3, 'odd'), (5, 'odd'), (8, 'even'), (11, 'odd')]
n_dict = {1: 'odd', 2: 'even', 3: 'odd', 5: 'odd', 8: 'even', 11: 'odd'}
assert even_odd_tuples_test((numbers), n_tuples)
print(even_odd_tuples(numbers))

assert even_odd_dict_test((numbers), n_dict)
print(even_odd_dict(numbers))
