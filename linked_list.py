
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
        
    def delete(self, index):
        previous, this, decrement_index = None, self.head, False
        while True:
            if decrement_index:
                this.index -= 1
            if this.index == index:
                if previous:
                    previous.next = this.next
                else:
                    this.next = self.head
                decrement_index = True
            if not this.next:
                break
            previous = this
            this = this.next

    def insert(self, new_data, index):
        previous, this, increment_index = None, self.head, False
        while True:
            if this.index == index:
                new_node = Node(new_data, index)
                if previous:
                    previous.next = new_node 
                else:
                    self.head = new_node
                new_node.next = this
                increment_index = True
            if increment_index:
                this.index += 1
            if not this.next:
                break
            previous = this
            this = this.next


linked_list = LinkedList('a')
linked_list.append('b')
linked_list.append('c')
linked_list.append('d')
linked_list.append('e')
print(linked_list.length())
print()

linked_list.print_data()
print()

print(linked_list.get_node(2).data)
print()

linked_list.delete(2)
print(linked_list.length())
print()

print(linked_list.get_node(2).data)
print()

linked_list.print_data()
print()

linked_list.insert('f', 2)
print(linked_list.length())
print()

print(linked_list.get_node(2).data)
print()

linked_list.print_data()
