
def card_sort(num_list):
    ret_arr = []

    for n in num_list:
        insert_index = 0
        while insert_index < len(ret_arr):
            if n < ret_arr[insert_index]:
                break
            insert_index += 1
        
        ret_arr = ret_arr[:insert_index] + [n] + ret_arr[insert_index:]

    return ret_arr

num_list, sorted = [12, 11, 13, 5, 6], [5, 6, 11, 12, 13]
assert( card_sort(num_list) == sorted )

num_list, sorted = [5, 7, 3, 5, 1, 3, -1, 1, -3, -1, -3, -1], [-3, -3, -1, -1, -1, 1, 1, 3, 3, 5, 5, 7]
assert( card_sort(num_list) == sorted )
