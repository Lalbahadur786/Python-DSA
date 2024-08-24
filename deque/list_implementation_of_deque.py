# List implementation of deque

class MyDeque:
    def __init__(self, capacity):
        self.c = capacity
        self.l = [None] * capacity
        self.front = 0
        self.sz = 0
    
    def insert_front(self, x):
        # check if deque is full
        if self.sz == self.c:
            return
        else:
            self.front = (self.front - 1) % self.c
            self.l[self.front] = x
            self.sz += 1
    
    def delete_front(self):
        if self.sz == 0:
            return
        else:
            self.front = (self.front + 1) % self.c
            self.sz -= 1
    
    def insert_rear(self, x):
        if self.sz == self.c:
            return
        else:
            new_rear = (self.front + self.sz) % self.c
            self.l[new_rear] = x
            self.sz += 1
    
    def delete_rear(self):
        if self.sz == 0:
            return
        else:
            rear = (self.front + self.sz - 1) % self.c
            self.sz -= 1
            return self.l[rear]
    
    def get_size(self):
        return self.sz
    
    def get_front_elem(self):
        return self.l[self.front]
    
    def get_rear_elem(self):
        if self.sz > 0:
            rear = (self.front + self.sz -1) % self.c
            return self.l[rear]
    
    def print_deque(self):
        print(self.l)

dq = MyDeque(7)
dq.insert_front(5)
dq.insert_front(7)
dq.insert_front(8)
dq.print_deque()
dq.insert_rear(21)
dq.insert_rear(29)
dq.insert_rear(25)
dq.print_deque()
dq.delete_front()
dq.delete_rear()
dq.print_deque()
print(dq.get_front_elem())
print(dq.get_rear_elem())
