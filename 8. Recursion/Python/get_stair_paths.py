'''
Find paths to reach ground(0) from nth stair. We can take jump of 1,2,3.

Input:
n=4
Output: 
['1111', '112', '121', '13', '211', '22', '31']
'''

# maintain arr to maintain path
def getStairPath(n):
    if n==0:
        arr = ['']
        return arr
    elif n<0:
        return []
    
    path1 = getStairPath(n-1)   # take 1 jump
    path2 = getStairPath(n-2)   # take 2 jumps
    path3 = getStairPath(n-3)   # take 3 jumps

    path = []
    for ch in path1:
        path.append('1'+ch)     # append 1 at paths which we found after taking 1 jump
    for ch in path2:
        path.append('2'+ch)     # append 2 at paths which we found after taking 2 jumps
    for ch in path3:
        path.append('3'+ch)     # append 3 at paths which we found after taking 3 jumps

    return path
print(getStairPath(4))

# print path as soon as we reach 0th level
def getStairPath(n, output):
    if n<0:
        return
    if n==0:
        print(output)
        return 
    
    getStairPath(n-1, output + '1')
    getStairPath(n-2, output + '2')
    getStairPath(n-3, output + '3')

getStairPath(4, '')