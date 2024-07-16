class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def insert_into_begin_dll(head, data):
    temp_node = Node(data)
    if head == None:
        return temp_node
    # Now insert  new node at the begin
    temp_node.next = head
    head.prev = temp_node

    return temp_node

def print_dll_items(head):
    if head == None:
        print()
    else:
        curr = head
        while curr != None:
            print(curr.data)
            curr = curr.next

head = Node(10)
head = insert_into_begin_dll(head, 20)
head = insert_into_begin_dll(head, 30)
head = insert_into_begin_dll(head, 40)
print_dll_items(head)