class Node:
    def __init__(self, k):
        self.data = k
        self.next = None

def print_linked_list(head):
    if head == None:
        print(None)
    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next

def print_middle_item_of_ll(head):
    if head == None:
        return None
    slow = head
    fast = head.next
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    print(slow.data) # this would be middle item

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
print_middle_item_of_ll(head)