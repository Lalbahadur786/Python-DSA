class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert_into_b_tree(root, key):
    if root == None:
        return Node(key)
    elif root.data == key:
        return root
    elif root.data > key:
        root.left = insert_into_b_tree(root.left, key)
    else:
        root.right = insert_into_b_tree(root.right, key)
    return root

root = insert_into_b_tree(Node(10), 15)
root = insert_into_b_tree(root, 7)
root = insert_into_b_tree(root, 18)
print(root.left.data)