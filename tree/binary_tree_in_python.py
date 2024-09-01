class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


root = None
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)

"""
10
/ \
20 30
/
40
"""