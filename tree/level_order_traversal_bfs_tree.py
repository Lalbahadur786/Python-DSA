class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def level_order_traversal(root):
    if root == None:
        return
    q = []
    q.append(root)
    while q:
        print(q[0].key, end=" ")
        node = q.pop(0)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
level_order_traversal(root)