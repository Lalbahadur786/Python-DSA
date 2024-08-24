class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Mydeque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.sz = 0
    
    def insert_front(self, data):
        temp_node = Node(data)
        if self.rear == None:
            self.front = temp_node
        else:
            self.rear.next = temp_node
            temp_node.prev = self.rear
        self.rear = temp_node
        self.sz += 1
    
    def delete_front(self):
        if self.is_empty():
            print("No elemnet to delete from front.")
        else:
            res = self.front.data
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            else:
                self.front.prev = None
            self.sz -= 1
            return res
    
    def insert_rear(self, data):
        temp_node = Node(data)
        if self.rear == None:
            self.front = temp_node
        else:
            self.rear.next = temp_node
            temp_node.prev = self.rear
        self.rear = temp_node
        self.sz += 1
        
    def delete_rear(self):
        if self.is_empty():
            print("Nothing to delete")
        else:
            res = self.rear.data
            self.rear = self.rear.prev
            if self.rear == None:
                self.front = None
            else:
                self.rear.next = None
            self.sz -= 1
            return res
    
    def get_front(self):
        if not self.is_empty():
            return self.front.data
    
    def get_rear(self):
        if not self.is_empty():
            return self.rear.data

    def get_size(self):
        if not self.is_empty():
            return self.sz
    def is_empty(self):
        if self.front == None:
            return True
        return False
    
    def print_deque_data(self):
        if self.is_empty():
            print("Deque is empty")
        else:
            curr = self.front
            while curr != None:
                print(curr.data)
                curr = curr.next


dq = Mydeque()
dq.insert_front(10)
dq.insert_front(20)
dq.insert_front(30)
dq.insert_front(40)
dq.insert_front(50)
dq.print_deque_data()
print(f"delete front: {dq.delete_front()}")
dq.print_deque_data()
dq.insert_rear(-50)
dq.insert_rear(-40)
dq.insert_rear(-30)
dq.print_deque_data()
print(f"delete rear: {dq.delete_rear()}")
print(f"get front: {dq.get_front()}")
print(f"get rear: {dq.get_rear()}")
print(f"get size: {dq.get_size()}")