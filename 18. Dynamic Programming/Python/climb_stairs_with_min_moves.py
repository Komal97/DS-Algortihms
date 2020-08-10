'''
You are given a number n, representing the number of stairs in a staircase.
You are on the 0th step and are required to climb to the top.
You are given n numbers, where ith element's value represents - till how far from the step you could jump to in a single move.  You can of-course fewer number of steps in the move.
You are required to print the number of minimum moves in which you can reach the top of staircase.
Input:
10
3 3 0 2 1 2 4 2 0 0
Output:
4
'''

def climbStairWithMinMoves(arr, n):
    
    dp = [-1]*(n+1)
    dp[n] = 0                                                       # n to n is 1 path but 0 move
    
    for i in range(n-1, -1, -1):
        if arr[i] > 0:                                              # if there is path
            minval = float('inf')
            for j in range(1, arr[i]+1):                            # find min value of path from j 
                if i + j < len(dp) and dp[i+j] != -1:
                    minval = min(minval, dp[i+j])
            if minval != float('inf'):                              # if there is a path, means min != inf
                dp[i] = minval + 1
    return dp[0]

if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    print(climbStairWithMinMoves(arr, n))