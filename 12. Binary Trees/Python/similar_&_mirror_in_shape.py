'''
1) check whether 2 trees are similar in shape
2) check whether 2 trees are mirror of each other
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

# check if a root is None and other is not then return False 
# else check for both sides
def areSimilar(root1, root2):
    
    if root1 == None and root2 == None:
        return True 
    if (root1 != None and root2 == None) or (root1 == None and root2 != None):
        return False

    left = areSimilar(root1.left, root2.left)
    if not left:
        return False
    right = areSimilar(root1.right, root2.right)
    if not right:
        return False
    return True

# check if a root is None and other is not then return False 
# else call on left side for root1 and right side for root2 and vice versa
def areMirror(root1, root2):
    if root1 == None and root2 == None:
        return True
    if (root1 != None and root2 == None) or (root1 == None and root2 != None):
        return False
    
    first = areMirror(root1.left, root2.right)
    if not first:
        return False
    second = areMirror(root1.right, root2.left)
    if not second:
        return False
    return True

root1= buildTree()
printLevelOrder(root1)
print()
root2= buildTree()
printLevelOrder(root2)

print(areSimilar(root1, root2))
print(areMirror(root1, root2))
