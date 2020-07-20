'''
Delete nodes from BST
'''
from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# insert a node in BST
def insertInBst(root, data):
    if root == None:
        root = Node(data)
        return root
    
    if root.data > data:
        root.left = insertInBst(root.left, data)
    else:
        root.right = insertInBst(root.right, data)
    
    return root

# take input data 
def buildTree():
    
    root = None
    data = [5, 3, 4, 2, 1, 8, 9, 7]
    
    for num in data:
        root = insertInBst(root, num)
        
    return root 

# find min node which is always in left tree
def minNode(root):
    while root.left != None:
        root = root.left 
    return root 

# delete a node from BST
# if 0 child - direct delete node and return null
# if 1 child - delete node and return child
# if 2 children - replace node with min in right
def deleteNode(root, key):
    if root == None:
        return None 
    
    # key to be deleted matches
    if root.data == key:
        # node with single child
        if root.left == None and root.right == None:
            del root
            return None
        # node with 1 child
        if root.left != None and root.right == None:
            temp = root.left
            del root
            return temp
        if root.left == None and root.right != None:
            temp = root.right
            del root
            return temp
        # node with 2 children
        replacement = minNode(root.right)                      # find min node from right tree
        root.data = replacement.data                           # copy min node data to root
        root.right = deleteNode(root.right, replacement.data)  # delete the replacement node
        return root
        
    elif root.data > key:
        root.left =  deleteNode(root.left, key)
        return root
    else:
        root.right =  deleteNode(root.right, key)
        return root

# print level order
def printLevelOrder(root):
    
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
    
    
root = buildTree()
printLevelOrder(root)
print()
key = int(input())
root = deleteNode(root, key)
printLevelOrder(root)