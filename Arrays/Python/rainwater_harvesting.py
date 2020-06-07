'''
Input - an array containing height of a building at each index
output - calculate total amount of water accumulated between those buidings

Soln - max(height of building on left of current building - right) - height of current building
'''

arr = list(map(int, input().split()))
n = len(arr)

left = [0 for _ in range(n)]
right = [0 for _ in range(n)]

left[0] = arr[0]
right[n-1] = arr[n-1]
for i in range(1, n):
    left[i] = max(left[i-1], arr[i])

for i in range(n-2, -1, -1):
    right[i] = max(right[i+1], arr[i])

count = 0
for i in range(n):
    count += (min(left[i], right[i]) - arr[i])

print(count)

