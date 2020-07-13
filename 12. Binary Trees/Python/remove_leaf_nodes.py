'''
Remove leaf nodes from binary tree
              20
           /     \
          10      30
         /  \    /  \
       5     15 25   35 

      After deleting the leaf node
              20
           /     \
          10      30
     
'''

# when we reach to leaf node, then return None instead of node and attach that None to left or right
def removeLeaf(root):
    if root == None:
        return
    if root.left == None and root.right == None:
        return None
    
    root.left = removeLeaf(root.left)
    root.right = removeLeaf(root.right)
    return root