'''
converted sorted array to BST which should be a balanced BST
'''

# mid node will be root node
# mid-1 nodes will be attached on root left
# mid+1 nodes will be attached on root right
from collections import deque
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None 
        self.right = None

def arrayToBST(root, arr, s, e):
    if s>e:
        return None 
    
    mid = (s+e)//2

    root = Node(arr[mid])
    root.left = arrayToBST(root.left, arr, s, mid-1)
    root.right = arrayToBST(root.right, arr, mid+1, e)
    return root 

def buildTree():
    root = None
    arr = [1, 2, 4, 5, 6, 8, 9, 10]
    root = arrayToBST(root, arr, 0, len(arr)-1)
    return root 

def printLevelOrder(root):

    q = deque()
    q.append(root)

    while len(q)>0:
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