class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def preorder_traversal(root):
    if root != None:
        print(root.key)
        preorder_traversal(root.left)
        preorder_traversal(root.right)

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)
preorder_traversal(root)