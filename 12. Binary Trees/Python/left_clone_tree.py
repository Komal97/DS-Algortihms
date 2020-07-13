'''
from a binary tree, create its left clone
'''

from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
def buildTree():

    n = input()
    if n == 'N':
        return None
    
    node = Node(n)
    node.left = buildTree()
    node.right = buildTree()
    return node

def levelOrder(root):
    q = deque()
    q.append(root)

    while len(q) > 0:
        size = len(q)
        for i in range(size):
            node = q.popleft()
            print(node.data, end = " ")
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        print()
        

def transform_to_left_clone(root):
    if root == None:
        return None
    
    # create left clone
    left_clone = transform_to_left_clone(root.left)
    # create right clone
    right_clone = transform_to_left_clone(root.right)
    # create a new node between root and left clone and attach all 3
    new_node = Node(root.data)
    new_node.left = left_clone
    root.left = new_node
    # attach right clone directly to root
    root.right = right_clone
    return root

def transform_from_left_clone(root):
    if root == None:
        return None

    # call on left by skipping one node which is duplicated
    left = transform_from_left_clone(root.left.left)
    # call on right
    right = transform_from_left_clone(root.right)
    # attach the returned nodes
    root.left = left
    root.right = right
    return root 

root = buildTree()
levelOrder(root)
print()
transform_to_left_clone(root)
levelOrder(root)
print()
transform_from_left_clone(root)
levelOrder(root)

