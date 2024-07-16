class Node:
    def __init__(self, k):
        self.data = k
        self.next = None

def insert_item_at_begin(head, k):
    temp_node = Node(k)
    temp_node.next = head
    return temp_node

def print_linked_list(head):
    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next

head = None
head = insert_item_at_begin(head, 10)
head = insert_item_at_begin(head, 20)
head = insert_item_at_begin(head, 30)
print_linked_list(head)