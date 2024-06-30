# radix sort based on count sort keeping original order instact


def countsort(arr, n, exp):
    #minVal = min(arr)
    #maxVal = max(arr)

    rangeVal = 10

    freq = [0 for _ in range (rangeVal)]

    for num in arr:
        #idx = num - minVal
        idx = num//exp % 10         # idx = (534 % 100 // 10) = 5 (value at handredth place)
        freq[idx] += 1

    for i in range(1, rangeVal):
        freq[i] += freq[i-1]

    ans = [0 for _ in range (n)] 

    for i in range(n-1, -1, -1):
        #idx = arr[i] - minVal
        idx = arr[i]//exp % 10
        ans[freq[idx] - 1] = arr[i]
        freq[idx] -= 1

    for i in range(n):
        arr[i] = ans[i]

def radixSort(arr, n):
    maxVal = max(arr)

    # looping over each number from ones < tens < hundred < thousands < ....
    exp = 1
    while exp <= maxVal:
        countsort(arr, n, exp)
        exp *= 10

arr = [5, 12, 234, 7, 9875, 62]
n = len(arr)

radixSort(arr, n)