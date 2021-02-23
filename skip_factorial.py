
from functools import reduce

def skip_factorial_nonrecursive(n):
    arr = list(range(2,n+1, 2)) if n % 2 == 0 else list(range(1,n+1, 2))
    return reduce( lambda m, n: m * n, arr, 1)


def skip_factorial_test(n, value):
    return skip_factorial_nonrecursive(n) == value


def skip_factorial_recursive(n):
    if n < 2:
        return 1
    return n * skip_factorial_recursive(n - 2)


def skip_factorial_recursive_test(n, value):
    return skip_factorial_recursive(n) == value

assert skip_factorial_test(6, 48)
print(skip_factorial_nonrecursive(6))

assert skip_factorial_test(7, 105)
print(skip_factorial_nonrecursive(7))

assert skip_factorial_recursive_test(6, 48)
print(skip_factorial_recursive(6))

assert skip_factorial_recursive_test(7, 105)
print(skip_factorial_recursive(7))
