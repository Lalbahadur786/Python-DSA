class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def find_floor_in_bst(root, key):
    res = None
    while root != None:
        if root.data == key:
            return key
        elif root.data > key:
            root = root.left
        else:
            res = root.data
            root = root.right
    return res



root = Node(10)
root.left = Node(5)
root.left.left = Node(3)
root.left.right = Node(7)
root.right = Node(20)
root.right.left = Node(17)
root.right.left.right = Node(25)
print(find_floor_in_bst(root, 4))