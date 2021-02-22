
class Stack:
    def __init__(self):
        self.data = []

    def push(self, elt):
        self.data.append(elt)

    def pop(self):
        return self.data.pop()

    def peek(self):
        ret_elt = self.data.pop()
        self.data.append(ret_elt)
        return ret_elt


def stack_test(data, reference_arr):
    index = 0
    while index < len(data):
        if data[index] != reference_arr[index]:
            return False
        index += 1
    return True

s = Stack()
assert(stack_test(s.data, []))
print(s.data)

s.push('a')
s.push('b')
s.push('c')

assert(stack_test(s.data, ['a', 'b', 'c']))
print(s.data)

s.pop()

assert(stack_test(s.data, ['a', 'b']))
print(s.data)

print(s.peek())

assert(stack_test(s.data, ['a', 'b']))
print(s.data)
