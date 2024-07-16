# Create a  linked list node class

class Node:
    def __init__(self, k):
        self.data = k
        self.next = None

def print_linked_list(head):
    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next

# Create linked list by inserting some elements
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

print_linked_list(head)