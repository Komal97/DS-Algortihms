'''
find floor and ceil element in binary tree
Input: 10 20 50 -1 -1 60 -1 -1 30 70 -1 -1 80 -1 -1
        Element: 65
Output: Floor - 60
        Ceil - 70
'''

from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# build binary tree
def buildTree():
    data = int(input())
    if data == -1:
        return None
    n = Node(data)
    n.left = buildTree()
    n.right = buildTree()
    return n 

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

# if root.data is greater than element, then keep min of greater elements
# if root.data is smaller than element, then keep max of smaller elements
floor = float('-inf')
ceil = float('inf')
def floor_ceil(root, element):
    global floor
    global ceil

    if root == None:
        return 
    
    if root.data < element:
        floor = max(floor, root.data)
    elif root.data > element:
        ceil = min(ceil, root.data)
    floor_ceil(root.left, element)
    floor_ceil(root.right, element)

root= buildTree()
printLevelOrder(root)
element = int(input())
floor_ceil(root, element)
print(floor)
print(ceil)


