class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
    

class AVL_tree:
    # Start with normal BST insert
    # update the height of nodes
    # Get the balance of node
    # cases
    # if balance < -1:
        # if key < root.right.val:
        # rotateright + rotateleft
        #else:
        # rotate left
    # if balance > 1:
        # if key < root.left.val
        # rotate right
    # if balance > 1:
        # if key > root.left.val
        # left rotate + right rotate
    def insert(self, root, key):
        # Start with normal insertion
        if not root:
            return Node(key)
        elif root.val < key:
            root.right = self.insert(root.right, key)
        else:
            root.left = self.insert(root.left, key)
        
        # Update the height of root
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # check balance
        balance = self.get_balance(root)

        # First take left casees with balance > 1 and key varies
        if balance > 1: # left subtree cases
            # two cases
            if key > root.left.val:
                # first left rotate
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
            else:
                return self.right_rotate(root)
        if balance < -1:
            # two cases
            if key > root.right.val:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
        return root

    def get_height(self, root):
        if root == None:
            return 0
        return root.height
    
    def get_balance(self, root):
        if root == None:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def left_rotate(self, root):
        y = root.right
        t2 = y.left
        # Now rotate nodes
        y.left = root
        root.right = t2

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y
    
    def right_rotate(self, root):
        y = root.left
        t3 = y.right
        # now rotate nodes
        y.right = root
        root.left = t3

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y
    
    def preorder(self, root):
        if root == None:
            return
        print(root.val, end= " ")
        self.preorder(root.left)
        self.preorder(root.right)

myTree = AVL_tree()
root = None

root = myTree.insert(root, 10)
root = myTree.insert(root, 20)
root = myTree.insert(root, 30)
root = myTree.insert(root, 40)
root = myTree.insert(root, 50)
root = myTree.insert(root, 25)

myTree.preorder(root)
print()


