class Node:
    def __init__(self, k):
        self.data = k
        self.next = None

def recu_reverse_list_by_reverse_first(curr, prev=None):
    if curr == None:
        return prev
    next = curr.next
    curr.next = prev
    return recu_reverse_list_by_reverse_first(next, curr)
    
    
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
prev = recu_reverse_list_by_reverse_first(head)
print_linked_list(prev)