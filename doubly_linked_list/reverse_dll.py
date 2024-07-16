class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.prev = None
        self.next = None

def reverse_dll(head):
    if head == None:
        return
    if head.next == None:
        return
    prev = None
    curr = head
    while curr != None:
        prev = curr
        curr.next , curr.prev = curr.prev, curr.next
        curr = curr.prev
    
    return prev

def print_dll_items(head):
    if head == None:
        print()
    else:
        curr = head
        while curr != None:
            print(curr.data)
            curr = curr.next

head = Node(10)
temp1 = Node(20)
temp2 = Node(30)
temp3 = Node(40)
head.next = temp1
temp1.prev = head
temp1.next = temp2
temp2.prev = temp1
temp2.next = temp3
temp3.prev = temp2

head = reverse_dll(head)
print_dll_items(head)