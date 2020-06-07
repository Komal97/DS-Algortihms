def merge(arr, s, e):

    mid = s + ((e-s)//2)
    i = s 
    j = mid + 1
    k = s

    temp = [0] * e+1
    while(i <= mid and j<=e):
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            k += 1
            i += 1
        else:
            temp[k] = arr[j]
            k += 1
            j += 1
    
    while(i <= mid):
        temp[k] = arr[i]
        k += 1
        i += 1
    while(j <= e):
        temp[k] = arr[j]
        k += 1
        j += 1
    
    for i in range(s, e+1):
        arr[i] = temp[i]

def mergesort(arr, s, e):
    # if 0 or 1 element then return because it is already sorted
    if s>=e:
        return

    mid = s + ((e-s)//2)
    mergesort(arr, s, mid)
    mergesort(arr, mid + 1, e)
    merge(arr, s, e)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    mergesort(arr, 0, n-1)
    print(arr)