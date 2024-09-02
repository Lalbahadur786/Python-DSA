class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def getsuccessor(curr):
    while curr.left != None:
        curr = curr.left
    return curr.key

def delete_key_from_bst(root, key):
    if root == None:
        return None
    if root.data > key:
        root.left = delete_key_from_bst(root.left, key)
    elif root.data < key:
        root.right = delete_key_from_bst(root.right, key)
    else:
        if root.left == None: # if left child  is None
            return root.right # return right child
        elif root.right == None: # if right child  is None
            return root.left # return left
        else:
            # both child is present
            # find first closest inorder traversal element in right subtree
            succ = getsuccessor(root.right)
            root.key = succ
            root.right = delete_key_from_bst(root, succ)
    return root

root = Node(10)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(5)
root.right = Node(15)
root.right.left = Node(12)
root.right.left.left = Node(11)
root.right.left.right = Node(13)
root.right.right = Node(20)
root = delete_key_from_bst(root, 5)
print(root.left.right.data)