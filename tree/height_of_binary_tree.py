class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def height(root):
    if root == None:
        return 0 # if to count edges then return -1
    else:
        lh = height(root.left)
        rh = height(root.right)
        return max(lh, rh) + 1
    
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
print(height(root))