

def identity_matrix_elements(n):
    return [[ 1 if j == i else 0 for j in range(n)] for i in range(n)]

ref_elts = [[1, 0, 0, 0],
 [0, 1, 0, 0],
 [0, 0, 1, 0],
 [0, 0, 0, 1]]

assert(identity_matrix_elements(4) == ref_elts)

def counting_across_rows_matrix_elements(m,n):
    return [[ 1 + i * n + j for j in range(n)] for i in range(m)]

ref_elts = [[1, 2, 3, 4],
 [5, 6, 7, 8],
 [9, 10, 11, 12]]
assert(counting_across_rows_matrix_elements(3,4) == ref_elts)


