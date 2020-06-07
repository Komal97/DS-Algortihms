def shell_sort(arr, n):
    gap = n//2

    while(gap > 0):
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while(j >= gap and arr[j-gap] > temp):
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap = gap//2

arr = [14, 18, 19, 37, 23, 40, 29, 30, 11]
n = len(arr)
shell_sort(arr, n)
print(arr)