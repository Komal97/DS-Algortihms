'''
Output:
['h1h1v1v1', 'h1h1v2', 'h1v1h1v1', 'h1v1v1h1', 'h1v1d1', 'h1v2h1', 'h1d1v1', 'h2v1v1', 'h2v2', 'v1h1h1v1', 'v1h1v1h1', 'v1h1d1', 'v1h2v1', 'v1v1h1h1', 'v1v1h2', 'v1d1h1', 'v2h1h1', 'v2h2', 'd1h1v1', 'd1v1h1', 'd1d1', 'd2']
'''

# store paths in arr
def getMazePathsWithJumps(x, y, m, n):
    
    if x==m and y == n:
        return ['']

    paths = []
    # horizontal moves
    for h in range(1, n-y+1):                           # control column
        hpaths = getMazePathsWithJumps(x, y+h, m, n)
        for path in hpaths:
            paths.append('h' + str(h) + path)
    
    # vertical moves
    for v in range(1, m-x+1):                           # control row
        vpaths = getMazePathsWithJumps(x+v, y, m, n)
        for path in vpaths:
            paths.append('v' + str(v) + path)

    # diagonal moves
    for d in range(1, n-y+1 and m-x+1):                  # control row and col
        dpaths = getMazePathsWithJumps(x+d, y+d, m, n)
        for path in dpaths:
            paths.append('d' + str(d) + path)

    return paths

arr = getMazePathsWithJumps(1, 1, 3, 3)
print(len(arr))
print(arr)

# print paths without storing
def getMazePathsWithJumps(x, y, m, n, output):
    
    if x==m and y == n:
        print(output)
        return

    # horizontal moves
    for h in range(1, n-y+1):                           # control column
        getMazePathsWithJumps(x, y+h, m, n, output + 'h' + str(h))

    # vertical moves
    for v in range(1, m-x+1):                           # control row
        getMazePathsWithJumps(x+v, y, m, n, output + 'v' + str(v))
        
    # diagonal moves
    for d in range(1, n-y+1 and m-x+1):                  # control row and col
        getMazePathsWithJumps(x+d, y+d, m, n, output + 'd' + str(d))
        

getMazePathsWithJumps(1, 1, 3, 3, '')

