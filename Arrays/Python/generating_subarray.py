'''
input an array
generata and print all subarray
'''

arr = list(map(int, input().split()))
n = len(arr)

for i in range(n):
    for j in range(i, n):
        for k in range(i, j+1):
            print(arr[k], end = " ")
        print()