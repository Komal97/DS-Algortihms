'''
https://www.interviewbit.com/problems/paint-house/
You are given a number n, representing the number of houses.
In the next n rows, you are given 3 space separated numbers representing the cost of painting nth house with red or blue or green color.
You are required to calculate and print the minimum cost of painting all houses without painting any consecutive house with same color.
Input:
4
1 5 7
5 8 4
3 2 9
1 2 4
Output:
8
'''

# based on max sum non-adjacent elements
# can create 2-D dp also
n = int(input())
house = []
for i in range(n):
    r, g, b = list(map(int, input().split()))
    house.append([r, g, b])
    
r = house[0][0]                                     # store min cost if current red is included
g = house[0][1]                                     # store min cost if current green is included
b = house[0][2]                                     # store min cost if current blue is included
for i in range(1, n):
    nr = min(g, b) + house[i][0]                    # new red is prev min cost among blue and green and add current red cost
    ng = min(r, b) + house[i][1]
    nb = min(r, g) + house[i][2]
    r = nr
    g = ng
    b = nb

print(min(r, min(b, g)))