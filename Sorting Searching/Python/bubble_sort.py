def bubblesort(arr, n):

    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    print(arr)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    bubblesort(arr, n)