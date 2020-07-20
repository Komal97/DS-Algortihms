'''
convert a binary search tree to a sorted linked list
'''
from collections import deque
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None 
        self.right = None

class LLPair:
    def __init__(self):
        self.head = None
        self.tail = None
        
def convertBSTtoLL(root):
    
    pair = LLPair()

    if root == None:
        return pair

    # if only root Node
    if root.left == None and root.right == None:
        pair.head = root
        pair.tail = root
    
    # if ll from left subtree
    elif root.left != None and root.right == None:
        leftPair = convertBSTtoLL(root.left)
        leftPair.tail.right = root
        pair.head = leftPair.head
        pair.tail = root
    
    # if ll from right subtree
    elif root.left == None and root.right != None:
        rightPair = convertBSTtoLL(root.right)
        root.right = rightPair.head
        pair.head = root
        pair.tail = rightPair.tail
    
    # if ll from both subtree
    else:
        leftPair = convertBSTtoLL(root.left)
        rightPair = convertBSTtoLL(root.right)
        leftPair.tail.right = root
        root.right = rightPair.head
        pair.head = leftPair.head
        pair.tail = rightPair.tail
    return pair

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

def printLL(head):
    while head != None:
        print(head.data, end="->")
        head = head.right
        
root = buildTree()
printLevelOrder(root)
pair = convertBSTtoLL(root)
printLL(pair.head)
