class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def print_kth_node(root, k):
    if root == None:
        return
    if k == 0:
        print(root.key, end=" ")
    else:
        print_kth_node(root.left, k-1)
        print_kth_node(root.right, k-1)

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
print_kth_node(root, 1)