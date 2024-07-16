class Node:
    def __init__(self, k):
        self.data = k
        self.next = None

def insert_item_at_end(head, k):
    if head == None:
        return Node(k)
    curr = head
    while curr.next != None:
        curr = curr.next
    curr.next = Node(k)
    return head

def print_linked_list(head):
    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next

head = None
head = insert_item_at_end(head, 10)
head = insert_item_at_end(head, 20)
head = insert_item_at_end(head, 30)
print_linked_list(head)