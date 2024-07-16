class Node:
    def __init__(self, k):
        self.data = k
        self.next = None

def remove_duplicate_item_in_sorted_ll(head):
    if head == None:
        return 
    curr = head
    while curr != None and curr.next != None:
        # if duplicate found
        if curr.data == curr.next.data:
            # just update curr.next with next nodes next
            curr.next = curr.next.next
        else:
            curr = curr.next
    
    
def print_linked_list(head):
    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next

# Create linked list by inserting some elements
head = Node(10)
head.next = Node(30)
head.next.next = Node(30)
head.next.next.next = Node(40)
remove_duplicate_item_in_sorted_ll(head)
print_linked_list(head)