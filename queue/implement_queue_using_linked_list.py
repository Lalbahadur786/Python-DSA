class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Myqueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    
    def enque(self, data):
        temp_node = Node(data)
        if self.rear == None:
            self.rear = temp_node
            self.front = temp_node
            self.size += 1
        else:
            self.rear.next = temp_node
            self.rear = temp_node
            self.size += 1
    def deque(self):
        if self.front == None:
            return None
        else:
            res = self.front.data
            self.front = self.front.next
            self.size -= 1
            if self.front == None:
                self.rear = None
        return res

    
    def get_size(self):
        return self.size
    
    def get_front_elem(self):
        return self.front.data  # handle for None front
    
    def get_rear_elem(self):
        return self.rear.data # handle for None rear
    
    def display_queue(self):
        if self.front == None:
            return
        else:
            curr = self.front
            while curr:
                print(curr.data, sep="|")
                curr = curr.next
    
q = Myqueue()
q.enque(10)
q.enque(20)
q.enque(30)
q.enque(40)
q.display_queue()
print("deque items")
print(q.deque())
print(q.deque())
print(q.deque())
print(q.get_front_elem())
print(q.get_rear_elem())
print(q.get_size())