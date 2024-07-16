# Create a  linked list node class

class Node:
    def __init__(self, k):
        self.data = k
        self.next = None

def delete_end_elem(head):
    # Handle if head is None
    if head == None:
        return None
    # Handle if only one item in LL
    if head.next == None:
        return None
    # Now delete end item in the list
    curr = head
    while curr.next.next != None:
        curr = curr.next
    # detach last node by delete pointer from previous
    curr.next = None
    return head

def print_linked_list(head):
    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next

# Create linked list by inserting some elements
head = Node(10)
head.next = Node(20)
# head.next.next = Node(30)
# head.next.next.next = Node(40)
head = delete_end_elem(head)
print_linked_list(head)