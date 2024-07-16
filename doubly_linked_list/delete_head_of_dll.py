class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def delete_head_of_dll(head):
    if head == None:
        return
    if head.next == None:
        return
    else:
        head = head.next
        head.next.prev = None

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
temp1 = Node(20)
temp2 = Node(30)
temp3 = Node(40)
head.next = temp1
temp1.prev = head
temp1.next = temp2
temp2.prev = temp1
temp2.next = temp3
temp3.prev = temp2

head = delete_head_of_dll(head)
print_dll_items(head)