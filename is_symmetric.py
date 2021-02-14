
def is_symmetric(s):
    return s == s[::-1]


def is_symmetric_unit_test(s, value):
    print("testing is_symmetric on input '", s, "'", sep='')
    assert is_symmetric(s) == value
    print("PASSED")

print()
is_symmetric_unit_test('racecar', True)
print()
is_symmetric_unit_test('batman', False)
