
def merge(x, y):
    x_index, y_index = 0, 0
    ret_arr = []
    while x_index < len(x) or y_index < len(y):
        if x_index == len(x):
            ret_arr.append(y[y_index])
            y_index += 1
            continue
        if y_index == len(y):
            ret_arr.append(x[x_index])
            x_index += 1
            continue
        if x[x_index] < y[y_index]:
            ret_arr.append(x[x_index])
            x_index += 1
        else:
            ret_arr.append(y[y_index])
            y_index += 1

    return ret_arr

print(merge([-2,1,4,4,4,5,7],[-1,6,6]))

