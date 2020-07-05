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

# preorder traversal of binary tree
def preorderTraversal(root):
    if root == None:
        return 
    print(root.data, end = ' -> ')
    preorderTraversal(root.left)
    preorderTraversal(root.right)

# postorder traversal of binary tree
def postorderTraversal(root):
    if root == None:
        return 
    postorderTraversal(root.left)
    postorderTraversal(root.right)
    print(root.data, end = ' -> ')

# inorder traversal of binary tree
def inorderTraversal(root):
    if root == None:
        return 
    inorderTraversal(root.left)
    print(root.data, end = ' -> ')
    inorderTraversal(root.right)

root = buildTree()
preorderTraversal(root)
print()
postorderTraversal(root)
print()
inorderTraversal(root)
print()