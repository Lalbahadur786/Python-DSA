# count the nodes of a tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def get_tree_size(root):
    if root == None:
        return 0
    else:
        ls = get_tree_size(root.left)
        rs = get_tree_size(root.right)
        return ls + 1 + rs

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
print(get_tree_size(root))