def insertionsort(arr, n):

    for i in range(1, n):
        temp = arr[i]
        j = i-1
        while(j>=0 and arr[j]>temp):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp

    print(arr)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    insertionsort(arr, n)