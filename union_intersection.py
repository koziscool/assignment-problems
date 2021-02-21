
def intersection(arr1, arr2):
    first_set, ret_set = set(arr1), set()
    for elt in arr2:
        if elt in first_set:
            ret_set.add(elt)
    return ret_set


def union(arr1, arr2):
    ret_set = set()
    for elt in arr1:
        ret_set.add(elt)
    for elt in arr2:
        ret_set.add(elt)
    return ret_set

print(intersection([1, 2],  [2, 3]))
print(union([1, 2], [2, 3]))
