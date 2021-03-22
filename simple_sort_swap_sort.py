
def simple_sort(arr):

    def minimum(arr):
        min_index, min_value = 0, arr[0]
        for i in range(1, len(arr)):
            if arr[i] < min_value:
                min_index, min_value = i, arr[i]
        return min_value, min_index

    ret_arr, working_arr = [], arr.copy()
    while len(working_arr) > 0:
        min_value, min_index = minimum(working_arr)
        ret_arr.append(min_value)
        working_arr = working_arr[:min_index] + working_arr[min_index +1:]
    return ret_arr

def swap_sort(arr):
    num_swaps = 1
    while num_swaps > 0:
        num_swaps = 0
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                num_swaps += 1
    return arr

numbers = [5,8,2,2,4,3,0,2,-5,3.14,2]
results_arr = [-5, 0, 2, 2, 2, 2, 3, 3.14, 4, 5, 8]
assert(simple_sort(numbers) == results_arr)
assert(swap_sort(numbers) == results_arr)
