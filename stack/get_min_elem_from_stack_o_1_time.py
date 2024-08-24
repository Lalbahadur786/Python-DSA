# Stack using linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        self.minimum = None

    def push(self, data):
        temp_node = Node(data)
        if self.head == None:
            self.minimum = data
        else:
            if data < self.head.data:
                temp_node.data = (2 * data) - self.minimum
                self.minimum = data
        temp_node.next = self.head
        self.head = temp_node
        self.size += 1
    
    def pop(self):
        if self.head != None:
            if self.head.data < self.minimum:
                self.minimum = (2 * self.minimum) - self.head.data
            res = self.head.data
            self.head = self.head.next
            self.size -= 1
            return res
    
    def stack_size(self):
        return self.size
    
    def get_min_elem(self):
        return self.minimum
    def peek(self):
        if self.head != None:
            if self.head.data < self.minimum:
                return self.minimum
            return self.head.data
     
    def display_stack(self):
        if self.head == None:
            return "stack is empty"
        curr = self.head
        while curr != None:
            print(curr.data)
            curr = curr.next

s = LinkedList()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.push(5)
print(f"minimum elem: {s.get_min_elem()}")
# s.display_stack()
# print(s.stack_size())
print(s.pop())
print(s.pop())
print(f"minimum elem: {s.get_min_elem()}")
s.display_stack()
print(s.peek())
# print(s.stack_size())