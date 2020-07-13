class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Pair:
    def __init__(self, node, state):
        self.node = node
        self.state = state

def buildTree():

    arr = [50, 25, 12, None, None, 37, 30, None, None, None, 75, 62, None, 70, None, None, 87, None, None]
    n = len(arr)
    stack = []
    root = Node(arr[0])
    pair = Pair(root, 1)
    stack.append(pair)

    # if state = 1, means first time encountered, state++ and move to left
    # if state = 2, means second time encountered, state++ and move to right
    # if state = 3, means third time encountered, pop from stack
    i = 0
    while len(stack) > 0:
        top = stack[-1]
        if top.state == 1:
            i += 1
            if i<n and arr[i] != None:
                top.node.left = Node(arr[i])
                left_pair = Pair(top.node.left, 1)
                stack.append(left_pair) 
            top.state += 1
        elif top.state == 2:
            i +=  1
            if i<n and arr[i] != None:
                top.node.right = Node(arr[i])
                right_pair = Pair(top.node.right, 1)
                stack.append(right_pair)
            top.state += 1
        else:
            stack.pop()
    return root

def printIterative(root):
    preorder = ''
    inorder = ''
    postorder = ''
    stack = []
    pair = Pair(root, 1)
    stack.append(pair)

    # if state = 1, means first time encountered, add in pre, state++ and move to left
    # if state = 2, means second time encountered, add in in, state++ and move to right
    # if state = 3, means third time encountered, add in post, and pop from stack
    while len(stack) > 0:
        top = stack[-1]
        if top.state == 1:
            preorder += str(top.node.data) + ' '
            top.state += 1
            if top.node.left != None:
                left_pair = Pair(top.node.left, 1)
                stack.append(left_pair)
        elif top.state == 2:
            inorder += str(top.node.data) + ' '
            top.state += 1
            if top.node.right != None:
                right_pair = Pair(top.node.right, 1)
                stack.append(right_pair)
        else:
            postorder += str(top.node.data) + ' '
            stack.pop()
    print(preorder)
    print(inorder)
    print(postorder)
            
root = buildTree()
printIterative(root)