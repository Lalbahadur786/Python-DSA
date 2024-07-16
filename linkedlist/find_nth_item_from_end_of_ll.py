class Node:
    def __init__(self, k):
        self.data = k
        self.next = None

def print_linked_list(head):
    if head == None:
        print(None)
    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next
def find_nth_item_from_end_of_ll(head, item_from_last):
    #  Check for head == NULL
    if head == None:
        return None
    # using two pointer method
    # first point will set to item_from_last position 
    # if item_from_last > len(LL) then retun None
    # second pointer will start from head pointer
    first = head
    # first will set to nth index otherwise return None if n > than LL
    for i in range(item_from_last):
        if first == None:
            return
        first = first.next
    second = head

    while first != None:
        first = first.next
        second = second.next
    
    # print where second is pointing currently
    print(second.data)

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
find_nth_item_from_end_of_ll(head, 2)