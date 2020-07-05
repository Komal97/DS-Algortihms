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

# count nodes in tree
def countNode(root):
    if root == None:
        return 0
    lc = countNode(root.left)
    rc = countNode(root.right)
    return 1 + lc + rc 

# height of tree
def height(root):
    if root == None:
        return 0
    
    lh = height(root.left)
    rh = height(root.right)
    return max(lh, rh) + 1

# print a level of tree
def printLevel(root, level):
    if root == None or level<0:
        return 
    if level == 0:
        print(root.data, end = ', ')
        return
    printLevel(root.left, level-1)
    printLevel(root.right, level-1)

# print level order recursively
def printLevelOrder(root):
    n = height(root)
    for level in range(n):
        printLevel(root, level)
        print()

root = buildTree()
print('total nodes in tree: ', countNode(root))
print('height of tree: ', height(root))
printLevelOrder(root)