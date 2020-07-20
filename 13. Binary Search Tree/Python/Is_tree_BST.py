'''
https://practice.geeksforgeeks.org/problems/check-for-bst/1
check Tree is balanced or not
'''
class Node:
    
    def __init__(self, data):
        self.data = data
        self.left = None 
        self.right = None

class Pair:
    def __init__(self):
        self.isBal = True
        self.min_val = float('inf')
        self.max_val = float('-inf')

def arrayToBST(root, arr, s, e):
    if s>e:
        return None 
    
    mid = (s+e)//2

    root = Node(arr[mid])
    root.left = arrayToBST(root.left, arr, s, mid-1)
    root.right = arrayToBST(root.right, arr, mid+1, e)
    return root 

def isBalanced(root):

    if root == None:
        basepair = Pair()
        return basepair
    
    lpair = isBalanced(root.left)
    rpair = isBalanced(root.right)
    
    mypair = Pair()
    # check if left subtree is balanced, right subtree is balanced and current node lies b/w max from left tree and min from right tree
    mypair.isBal = lpair.isBal and rpair.isBal and root.data >= lpair.max_val and root.data < rpair.min_val
    # compute min and max for current node, because we don't know whether current node is at left or right of its parent node
    mypair.min_val = min(root.data, min(lpair.min_val, rpair.min_val))
    mypair.max_val = max(root.data, max(lpair.max_val, rpair.max_val))
    return mypair

arr = [1, 2, 4, 5, 6, 8, 9]

root = None
root = arrayToBST(root, arr, 0, len(arr)-1)
print(isBalanced(root).isBal)