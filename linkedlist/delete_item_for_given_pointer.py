# Create a  linked list node class

class Node:
    def __init__(self, k):
        self.data = k
        self.next = None

def delete_item_by_pointer(ptr):
    # one assumption pointer is not of last node
    # retain ref of next node
    temp = ptr.next
    # copy data in current ptr node
    ptr.data = temp.data
    # point to temp.next node (Next)
    ptr.next = temp.next
    return ptr

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
head = delete_item_by_pointer(head.next)
print_linked_list(head)