class Node:
    def __init__(self, k):
        self.data = k
        self.next = None

def recu_reverse_list(head):
    if head == None:
        return head
    if head.next == None:
        return head
    rest_head = recu_reverse_list(head.next)
    rest_tail = head.next
    rest_tail.next = head
    head.next = None
    return rest_head
    
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
prev = recu_reverse_list(head)
print_linked_list(prev)