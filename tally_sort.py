
def tally_sort(num_list):
    minimum = 999999
    for n in num_list:
        if n < minimum:
            minimum = n

    new_arr = [0] * len(num_list)
    
    for n in num_list:
        new_arr[n - minimum] += 1

    ret_arr = []
    for i in range(len(new_arr)):
        for _ in range(new_arr[i]):
            ret_arr.append(i)

    for i in range(len(ret_arr)):
        ret_arr[i] += minimum

    return ret_arr


num_list, sorted = [2, 5, 2, 3, 8, 6, 3 ], [2, 2, 3, 3, 5, 6, 8]
assert( tally_sort(num_list) == sorted )
