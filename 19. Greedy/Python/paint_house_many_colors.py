'''
You are given a number n and a number k separated by a space, representing the number of houses and number of colors.
In the next n rows, you are given k space separated numbers representing the cost of painting nth house with one of the k colors.
You are required to calculate and print the minimum cost of painting all houses without painting any consecutive house with same color.
Input:
4 3
1 5 7
5 8 4
3 2 9
1 2 4
Output:
8
'''

# method - 1 => O(n^3)
# same as paint house -> add current + min from prv all colors except current color
h, c = list(map(int, input().split()))
house = []
for i in range(h):
    colors = list(map(int, input().split()))
    house.append(colors)

dp = [[0]*c for _ in range(h)]

for i in range(c):
    dp[0][i] = house[0][i]
    
for i in range(1, h):
    for j in range(c):
        min_val = float('inf')
        for k in range(c):
            if k != j:
                min_val = min(min_val, dp[i-1][k])
        dp[i][j] = house[i][j] + min_val

min_val = float('inf')
for i in range(c):
    min_val = min(min_val, dp[h-1][i])
print(min_val)

# method - 2 => O(n^2)
# instead of finding min every time, keep min and sec min
# if prv row of same color = min then add sec min to current value else add min
h, c = list(map(int, input().split()))
house = []
for i in range(h):
    colors = list(map(int, input().split()))
    house.append(colors)

dp = [[0]*c for _ in range(h)]

least = float('inf')
sleast = float('inf')
for i in range(c):
    dp[0][i] = house[0][i]
    if dp[0][i] <= least:
        sleast = least
        least = dp[0][i]
    elif dp[0][i] <= sleast:
        sleast = dp[0][i]
    
for i in range(1, h):
    nleast = float('inf')
    nsleast = float('inf') 
    for j in range(c):
        if least == dp[i-1][j]:
            dp[i][j] = house[i][j] + sleast
        else:
            dp[i][j] = house[i][j] + least
        if dp[i][j] <= nleast:
            nsleast = nleast
            nleast = dp[i][j]
        elif dp[i][j] <= nsleast:
            nsleast = dp[i][j]
    least = nleast
    sleast = nsleast
print(least)