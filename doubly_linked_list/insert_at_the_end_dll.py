class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def insert_at_the_end_dll(head, data):
    temp_node = Node(data)
    # if head is none:
    if head == None:
        return temp_node
    else:
        # Now if some items in the dll now search for end
        curr = head
        while curr.next != None:
            curr = curr.next
        
        # you are the end of list
        curr.next = temp_node
        temp_node.prev = curr
    return head

def print_dll_items(head):
    if head == None:
        print()
    else:
        curr = head
        while curr != None:
            print(curr.data)
            curr = curr.next

head = Node(10)
head = insert_at_the_end_dll(head, 20)
head = insert_at_the_end_dll(head, 30)
head = insert_at_the_end_dll(head, 40)
print_dll_items(head)