class Node:
    def __init__(self, k):
        self.data = k
        self.next = None

def reverse_linked_list(head):
    curr = head
    prev = None
    while curr != None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

    
def print_linked_list(head):
    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next

# Create linked list by inserting some elements
head = Node(10)
head.next = Node(30)
head.next.next = Node(30)
head.next.next.next = Node(40)
prev = reverse_linked_list(head)
print_linked_list(prev)