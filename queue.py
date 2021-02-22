
class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, elt):
        self.data.append(elt)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]


def queue_test(data, reference_arr):
    index = 0
    while index < len(data):
        if data[index] != reference_arr[index]:
            return False
        index += 1
    return True

q = Queue()
assert(queue_test(q.data, []))
print(q.data)

q.enqueue('a')
q.enqueue('b')
q.enqueue('c')

assert(queue_test(q.data, ['a', 'b', 'c']))
print(q.data)

q.dequeue()

assert(queue_test(q.data, ['b', 'c']))
print(q.data)

print(q.peek())

assert(queue_test(q.data, ['b', 'c']))
print(q.data)
