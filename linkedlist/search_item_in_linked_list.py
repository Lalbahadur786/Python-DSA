class Node:
    def __init__(self, k):
        self.data = k
        self.next = None


def search_item(head, item):
    pos = 1
    curr = head
    while curr != None:
        if curr.data == item:
            return pos
        pos += 1
        curr = curr.next
    return -1


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
print(search_item(head, 40))