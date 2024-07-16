class Node:
    def __init__(self, k):
        self.data = k
        self.next = None

def insert_an_item(head, pos, data):
    # first create the temp node with data
    temp_node = Node(data)
    # handle if insert at the begining
    if pos == 1:
        temp_node.next = head
        return temp_node
    
    # iterate loop to find elements before the pos
    curr = head
    for i in range(pos - 2):
        if curr == None:
            # return head if pos is > size + 1
            return head
        curr = curr.next
    
    # we have got the just before node of pos
    if curr != None: # useful when pos is size +2
        temp_node.next = curr.next
        curr.next = temp_node

    return head


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
# insert at begin
head = insert_an_item(head, 1, 4)

# insert in middle
head = insert_an_item(head, 4, 25)
# insert at the end
head = insert_an_item(head, 7, 250)
head = insert_an_item(head, 8, 150)
# insert at out of range pos

head = insert_an_item(head, 11, 250) # work on this condition
print_linked_list(head)