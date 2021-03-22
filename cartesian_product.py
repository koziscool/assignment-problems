
def cartesian_product(arrays):
    points = [[]]
    for arr in arrays:
        new_points = []
        for elt in arr:
            for p in points:
                new_points.append( p + [elt] )
        points = new_points
    return points

arrays = [['a'], [1,2,3], ['Y','Z']]
cp_results = [['a', 1, 'Y'], ['a', 2, 'Y'], ['a', 3, 'Y'], ['a', 1, 'Z'], ['a', 2, 'Z'], ['a', 3, 'Z']]

assert( cartesian_product(arrays) == cp_results )
