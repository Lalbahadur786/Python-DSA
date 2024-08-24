from collections import deque

class MyStackfromqueue:
    def __init__(self) -> None:
        self.q1 = deque()
        self.q2 = deque()

    def push(self, data):
        # first move to q2
        self.q2.append(data)
        while self.q1:
            # append items from q1 to q2
            self.q2.append(self.q1.popleft())
        # swap variables name
        self.q1, self.q2 = self.q2, self.q1
    
    def pop(self):
        if self.q1:
            return self.q1.popleft()
    
    def top(self):
        if self.q1:
            return self.q1[0]
        
    def size(self):
        return len(self.q1)

myq = MyStackfromqueue()
myq.push(10)
myq.push(20)
myq.push(30)
myq.push(40)
myq.push(50)
myq.pop()
print(myq.top())
print(myq.q1)
print(myq.top())
print(myq.size())