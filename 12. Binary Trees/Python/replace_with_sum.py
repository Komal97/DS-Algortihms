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

# replace sum of node with sum of child nodes + node.data
def replaceWithSum(root):
    if root == None:
        return 0

    lsum = replaceWithSum(root.left)
    rsum = replaceWithSum(root.right)
    root.data += lsum + rsum
    return root.data

# replace sum of node with sum of child nodes exclusing node.data
def replaceWithChildSum(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return root.data

    lsum = replaceWithSum(root.left)
    rsum = replaceWithSum(root.right)
    temp = root.data
    root.data = lsum + rsum
    return temp + root.data

root = buildTree()
printLevelOrder(root)
print('sum:', replaceWithSum(root))
printLevelOrder(root)