# method -1 
def countsort(arr, n):
    freq = [0]*10
    
    for i in range(n):
        freq[arr[i]] += 1
    i = 0
    j = 0
    while(i<len(arr) and j<len(freq)):
        while(freq[j] != 0):
            arr[i] = j
            i += 1
            freq[j] -= 1
        j += 1

    print(arr)


# method - 2 --> if we want to keep sequence intact (stable sort)
def countsort(arr, n):
    # arr = [9, 6, 3, 5, 3, 4, 3, 9, 6, 4, 6, 5, 8, 9, 9]
    
    minVal = min(arr)      # min = 3
    maxVal = max(arr)      # max = 9 

    rangeVal = maxVal - minVal + 1      # range = 7

    freq = [0 for _ in range (rangeVal)]

    # find frequency  - [3, 2, 2, 3, 0, 1, 4]
    for num in arr:
        idx = num - minVal
        freq[idx] += 1

    # find cumulative sum of frequencies to keep next index  - [3, 5, 7, 10, 10, 11, 15] - indicating indexes starting from 1, not 0
    for i in range(1, rangeVal):
        freq[i] += freq[i-1]               

    ans = [0 for _ in range (n)] 

    for i in range(n-1, -1, -1):
        idx = arr[i] - minVal              # find index where freq of value is being kep
        ans[freq[idx] - 1] = arr[i]        # put current value into ans array at index represented by fre
        freq[idx] -= 1                 
    
    # fill original array
    for i in range(n):
        arr[i] = ans[i]
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    countsort(arr, n)