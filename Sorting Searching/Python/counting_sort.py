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

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    countsort(arr, n)