'''
The task is to reach nth stair from 0th position. Number of steps to be taken from a stair is given in form of array.
Find number of paths to reach from 0th to nth stair
Input:
arr = [3, 3, 0, 2, 2, 3]
Output:
8
'''

# recursive
def climbStairWithVarJumps(arr, i, n):
    
    if i == n:
        return 1
    elif i > n:
        return 0
        
    jumps = 0
    for j in range(1, arr[i]+1):
        jumps += climbStairWithVarJumps(arr, i+j, n)
    return jumps

# we have smallest problem at nth position
# so direction of small to big is from n to 0
def climbStairWithVarJumps(arr, n):
    
    dp = [0]*(n+1)
    dp[n] = 1
    for i in range(n-1, -1, -1):
        for j in range(1, arr[i]+1):         # take jumps given at a position
            if i+j < len(dp):
                dp[i] += dp[i+j]
    
    return dp[0]

if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    print(climbStairWithVarJumps(arr, n))