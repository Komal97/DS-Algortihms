from collections import deque

class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None

# insert node in BST
def insertInBst(root, data):
    if root == None:
        n = Node(data)
        return n 

    if data <= root.data:
        root.left = insertInBst(root.left, data)
    else:
        root.right = insertInBst(root.right, data)
    return root         

# take input to insert node in BST
def takeInput():
    
    root = None
    data = int(input())
    while data != -1:
        root = insertInBst(root, data)
        data = int(input())
    return root

# search key in tree
def search(root, data):
    if root == None:
        return False 
    
    if root.data == data:
        return True 
    
    if data < root.data:
        return search(root.left, data)
    return search(root.right, data)

# print BST in level order
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

root = takeInput()
printLevelOrder(root)

key = int(input('Enter key to search: '))
if search(root, key):
    print(key, 'found in tree')
else:
    print(key, 'not found in tree')