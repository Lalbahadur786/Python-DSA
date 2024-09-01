import math
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


def get_max(root):
    if root == None:
        return -math.inf
    else:
        lm = get_max(root.left)
        rm = get_max(root.right)
        return max(root.key, lm, rm)


root = Node(10)

root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(25)
print(get_max(root))