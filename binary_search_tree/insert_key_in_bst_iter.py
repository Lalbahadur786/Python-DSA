class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert_into_b_tree_iter(root, key):
    parent = None
    curr = root
    while curr != None:
        parent = curr
        if curr.data == key:
            return root
        elif curr.data > key:
            curr = curr.left
        else:
            curr = curr.right
    if parent == None:
        return Node(key)
    elif parent.data > key:
        parent.left = Node(key)
    else:
        parent.right = Node(key)
    return root

root = insert_into_b_tree_iter(Node(10), 15)
root = insert_into_b_tree_iter(root, 7)
root = insert_into_b_tree_iter(root, 18)
print(root.right.data)