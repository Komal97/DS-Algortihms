'''
find predecessor and successor of a node in preorder manner

Input: 10 20 50 -1 -1 60 -1 -1 30 80 110 -1 -1 120 -1 -1 -1
       Element: 110
Output: Predecessor - 80
        Successor - 120
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

# if state = 0, update predecessor and check root.data = element, if yes then state = 1
# if state = 1 and root.data != element, then update successor and change state = 2
predecessor = -1
successor = -1
state = 0
def predAndSucc(root, element):
    global predecessor
    global successor
    global state

    if root == None:
        return 

    if state == 0:
        if root.data == element:
            state = 1
        else:
            predecessor = root.data
    elif state == 1:
        successor = root.data
        state = 2
        
root= buildTree()
printLevelOrder(root)
element = int(input())
predAndSucc(root, element)
print()
print(predecessor)
print(successor)
