class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_item_at_begin_traverse_method(head, data):
    temp_node = Node(data)
    if head == None:
        # Make circular first Node only
        temp_node.next = temp_node
        return temp_node
    curr = head

    # Get the last tail Node
    while curr.next != head:
        curr = curr.next
    
    # Point tail node to new Node
    temp_node.next = head
    curr.next = temp_node
    return temp_node


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
head = insert_item_at_begin_traverse_method(head, 60)
print_circular_linked_list(head)
