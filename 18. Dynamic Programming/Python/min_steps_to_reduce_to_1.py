'''
Reduce a number to 1 in minimum steps with 3 operations allowed:
1) divisible by 2
2) divisible by 3
3) subtract 1

'''

# memoization
def min_steps(n, memo):
    
    if n <= 1:
        return 0

    if memo[n] != -1:
        return memo[n]

    val1 = float('inf')
    if n%2 == 0:
        val1 = min_steps(n//2, memo)

    val2 = float('inf')
    if n%3 == 0:
        val2 = min_steps(n//3, memo)
    
    val3 = min_steps(n-1, memo)

    memo[n] = min(val1, min(val2, val3)) + 1
    return memo[n]

# i-D DP
def min_steps(n):
    dp = [0]*(n+1)
    
    for i in range(2, n+1):
        val1 = dp[i//2] if (i%2==0) else float('inf')
        val2 = dp[i//3] if (i%3==0) else float('inf')
        val3 = dp[i-1]
        dp[i] =  min(val1, min(val2, val3)) + 1

    return dp[n]

n = int(input())
memo = [-1]*(n+1)
ans = min_steps(n, memo)
print(ans)