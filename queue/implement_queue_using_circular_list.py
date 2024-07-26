class Myqueue:
    def __init__(self, capacity):
        self.c = capacity
        self.l = [None] * capacity
        self.size = 0
        self.front = 0
    
    def enque(self, data):
        if self.size == self.c:
            return
        else:
            rear = (self.front + self.size-1) % self.c
            rear = (rear + 1) % self.c
            self.l[rear] = data
            self.size += 1
    
    def deque(self):
        if self.size == 0:
            return None
        res = self.l[self.front]
        self.front = (self.front + 1) % self.c
        self.size -= 1
        return res
    
    def getfront(self):
        if self.size == 0:
            return
        else:
            return self.l[self.front]
    
    def getrear(self):
        if self.size == 0:
            return
        else:
            rear = (self.front + self.size -1) % self.c
            return self.l[rear]

q = Myqueue(5)
q.enque(10)
q.enque(20)
q.enque(30)
q.enque(40)
q.enque(50)
print(q.l)
q.deque()
q.deque()
q.deque()
print(q.l)
print(q.getfront())
print(q.getrear())