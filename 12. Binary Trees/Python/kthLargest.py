'''
find kth largest element from binary tree
Input: 10 20 50 -1 -1 60 -1 -1 30 70 -1 -1 80 -1 -1
       k = 3 (means 3rd largest element)
Output: 60
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

floor = float('-inf')
def find_floor(root, element):
    global floor

    if root == None:
        return 
    
    if root.data < element:
        floor = max(floor, root.data)

    find_floor(root.left, element)
    find_floor(root.right, element)

# each time we get largest element from smaller than current largest element
# floor(inf) - 80
# floor(80) - 70
# floor(70) - 60
def kthLargest(root, k):
    global floor
    factor = float('inf')
    for i in range(k):
        find_floor(root, factor)
        factor = floor
        floor = float('-inf')
    print(factor)

root= buildTree()
printLevelOrder(root)
k = int(input())
kthLargest(root, k)


