class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_kth_node(head, k):
    if head == None:
        return None
    if k == 1:
        if head.next == head:
            return None
        
        head.data = head.next.data
        head.next = head.next.next
        return head
    
    curr = head
    for _ in range(k - 2):
        if curr.next == head:
            return head
        curr = curr.next
    
    curr.next = curr.next.next

    return head


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
head = delete_kth_node(head, 4)
print_circular_linked_list(head)
