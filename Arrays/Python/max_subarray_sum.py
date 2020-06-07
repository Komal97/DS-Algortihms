'''
Input array and find maximum subarray sum
method 1 - by generating subarray in O(n^3) complexity
method 2 - by preprocessing array - create cumulative array - O(n^2) complexity
method 3 - using kadane's algorithm in O(n) complexity
'''

# method 1  
def maxsum(arr, n):
    currsum = 0
    maxsum = 0
    left = -1
    right = -1
    for i in range(n):
        for j in range(i, n):
            currsum = 0
            for k in range(i, j+1):
                currsum = currsum + arr[k]
            if currsum > maxsum:
                maxsum = currsum
                left = i
                right = j
    
    for index in range(left, right+1):
        print(arr[index], end = " ")
    print("\nMaximum sum in O(n^3): ", maxsum)

#method 2
def cs_method(arr, n):
    currsum = 0
    maxsum = 0
    left = -1
    right = -1
    cs = []
    cs.append(arr[0])

    for i in range(1, n):
        cs.append(cs[i-1] + arr[i])
    
    for i in range(n):
        for j in range(i, n):
            currsum = 0
            currsum = cs[j] - cs[i-1]
            if currsum > maxsum:
                maxsum = currsum
                left = i
                right = j
    for index in range(left, right+1):
        print(arr[index], end = " ")
    print("\nMaximum sum in O(n^2): ", maxsum)

# method 3
def kadane_method(arr, n):
    currsum = 0
    maxsum = min(arr)

    for i in range(n):
        currsum = currsum + arr[i]
        maxsum = max(maxsum, currsum)
        if currsum < 0:
            currsum = 0
    print("\nMaximum sum in O(n): ", maxsum)

arr = list(map(int, input().split()))
n = len(arr)
maxsum(arr, n)
cs_method(arr, n)
kadane_method(arr, n)



