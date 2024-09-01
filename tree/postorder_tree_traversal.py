class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def postorder_traversal(root):
    if root != None:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.key)

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)
postorder_traversal(root)