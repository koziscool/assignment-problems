
import math


def is_prime(n):
    for i in range(2, math.floor(n/2)):
        if n % i == 0:
            return False
    return True


def is_prime_unit_test(n, b):
    print("testing is_prime on input", n)
    assert is_prime(n) == b
    print("PASSED")

print()
is_prime_unit_test(59, True)
print()
is_prime_unit_test(51, False)
