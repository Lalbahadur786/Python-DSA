class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def getsuccessor(curr):
    while curr.left != None:
        curr = curr.left
    return curr.data

def delete_key_from_bst(root, key):
    if root == None:
        return root
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
            print(succ)
            root.data = succ
            root.right = delete_key_from_bst(root.right, succ)
    return root

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

root = Node(50)
root.left = Node(30)
root.left.right = Node(40)
root.right = Node(70)
root.right.left = Node(60)
root.right.right = Node(80)
root = delete_key_from_bst(root, 50)
print(inorder(root))