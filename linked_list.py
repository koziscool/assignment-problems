
class Node:
    def __init__(self, data, index):
        self.data = data
        self.index = index
        self.next = None

class LinkedList:
    def __init__(self, data):
        self.head = Node(data, 0)

    def print_data(self):
        this = self.head
        while True:
            print(this.data)
            if this.next  == None:
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
        new_node = Node(data, this.index + 1)
        this.next = new_node

    def get_node(self, index):
        this = self.head 
        while True:
            if this.index == index:
                return this
            if not this.next:
                break
            this = this.next
        return None

    def push(self, new_data):
        temp = self.head
        self.head = Node(new_data, 0)
        self.head.next = temp
        this = self.head 
        while True:
            if not this.next:
                break
            this = this.next
            this.index += 1
        


linked_list = LinkedList('b')
linked_list.append('e')
linked_list.append('f')
linked_list.push('a')

assert(linked_list.length() == 4)

assert(linked_list.head.index==0)
assert(linked_list.head.next.index==1)
assert(linked_list.head.next.next.index==2)
assert(linked_list.head.next.next.next.index==3)

assert(linked_list.get_node(0).data=='a')
assert(linked_list.get_node(1).data=='b')
assert(linked_list.get_node(2).data=='e')
assert( linked_list.get_node(3).data=='f')
