class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def search_key_in_bst_iter(root, key):
    while root != None:
        if root.data == key:
            return True
        elif root.data > key:
            root = root.left
        elif root.data < key:
            root = root.right
    return False

root = Node(10)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(5)
root.right = Node(15)
root.right.left = Node(12)
root.right.left.left = Node(11)
root.right.left.right = Node(13)
root.right.right = Node(20)
print(search_key_in_bst_iter(root, 5))