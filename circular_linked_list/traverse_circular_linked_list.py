class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_circular_linked_list(head):
    if head == None:
        return None
    print(head.data)

    curr = head.next

    while curr != head:
        print(curr.data)
        curr = curr.next

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = head  # Circular linked list

print_circular_linked_list(head)
