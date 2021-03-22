
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def print_data(self):
        this = self.head
        while True:
            print(this.data)
            if not this.next:
                break
            this = this.next

    def length(self):
        this, counter = self.head, 1
        while True:
            if not this.next:
                break
            this, counter = this.next, counter + 1
        return counter

    def append(self, data):
        this = self.head
        while True:
            if not this.next:
                break
            this = this.next
        new_node = Node(data)
        this.next = new_node
        


A = Node(4)
assert(A.data == 4)
assert(A.next == None)

B = Node(8)
A.next = B
assert(A.next.data == 8)

linked_list = LinkedList(4)
assert(linked_list.head.data == 4)
linked_list.append(8)
assert(linked_list.head.next.data == 8)
linked_list.append(9)
# linked_list.print_data()  prints 4, 8, 9 correctly
assert(linked_list.length() == 3)
