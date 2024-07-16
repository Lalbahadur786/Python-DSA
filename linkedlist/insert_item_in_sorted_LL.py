class Node:
    def __init__(self, k):
        self.data = k
        self.next = None

def insert_an_item_in_sorted_ll(head,data):
    # first create the temp node with data
    temp_node = Node(data)

    # if head is null retun temp node
    if head == None:
        return temp_node
    # if data is less than head data (insert at begining)
    if head.data > data:
        temp_node.next = head
        return temp_node
    # if data to be inserted in between
    curr = head
    while curr.next != None and  curr.next.data < data:
        curr = curr.next
    # Now the curr node is just before node > data
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


head = insert_an_item_in_sorted_ll(head, 20)
print_linked_list(head)