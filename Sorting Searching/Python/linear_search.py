def linear_search(arr, key, n):

    for i in range(n):
        if arr[i] == key:
            return i
    return -1

def main():    
    arr = list(map(int, input().split()))
    n = len(arr)
    key = int(input())
    index = linear_search(arr, key, n)
    
    if index == -1:
        print("Element not found")
    else:
        print("Element found at index: ", index)

main()