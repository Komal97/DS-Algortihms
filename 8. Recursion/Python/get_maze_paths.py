'''
The task is to print all the possible paths from top left to bottom right of a mXn matrix with the constraints that from each cell you can either move only to right or down.
'''

def getMazePaths(x, y, n, output):
    if x == n and y == n:                       # bottom right reached
        print(output)
        return

    if x < n:                                   
        getMazePaths(x+1, y, n, 'h'+output)     # right call
    if y<n:
        getMazePaths(x, y+1, n, 'v'+output)     # down call


getMazePaths(1, 1, 3, '')