'''
1. You are given a number n, representing the count of coins.
2. You are given n numbers, representing the denominations of n coins.
3. You are given a number "amt".
4. You are required to calculate and print the number of permutations of the n coins using which the amount "amt" can be paid.
Note1 -> You have an infinite supply of each coin denomination.
Note2 -> You are required to find the count of permutations and not combinations i.e.
2 + 2 + 3 = 7 and 2 + 3 + 2 = 7 and 3 + 2 + 2 = 7 are different permutations of same combination. You should treat them as 3 and not 1.
'''

# same as coin change 1 
def coinChange(coins, n, totalamount):
    
    dp = [0]*(totalamount+1)
    dp[0] = 1
    
    for amt in range(1, totalamount+1):                 # for each amount
        for coin in coins:                              # check for each coin value
            if coin <= amt:
                dp[amt] += dp[amt-coin]
                
    return dp[totalamount]
    
if __name__ == '__main__':
    n = int(input())
    coins = []
    for i in range(n):
        coins.append(int(input()))
    amt = int(input())
    print(coinChange(coins, n, amt))