
def unlist_nonrecursive(x):
    while type(x) is list and len(x) == 1:
        x = x[0]
    return x


def unlist_nonrecursive_test(x, value):
    return unlist_nonrecursive(x) == value


def unlist_recursive(x):
    if type(x) is not list or len(x) > 1:
        return x
    return unlist_recursive(x[0])

def unlist_recursive_test(x, value):
    return unlist_recursive(x) == value

assert unlist_nonrecursive_test([[[[1], [2,3], 4]]], [[1], [2, 3], 4])
assert unlist_nonrecursive_test([[[[1]]]], 1)
