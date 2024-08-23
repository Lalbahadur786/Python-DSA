from collections import deque

# Doubly ended queue
# insert front, insert rear, delete front, delete rear

d = deque()
d.append(10)
d.append(10)
d.append(30)
d.extend([25,32])
print(d) # deque[10, 10, 30, 25, 32]
d.extendleft([5, 6])
print(d) # deque[6, 5, 10, 10, 30, 25, 32]

d.rotate(2)
print(d) # deque([25, 32, 6, 5, 10, 10, 30])
d.popleft()
print(d) # deque([32, 6, 5, 10, 10, 30])