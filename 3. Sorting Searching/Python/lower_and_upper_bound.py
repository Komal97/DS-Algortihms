'''
Input an array
Find Lower bound (first occurance) of a number
Find Upper bound (last occurance) of a number
'''

def first_occ(arr, n, key):
    start = 0
    end = n-1
    ans = -1
    
    while(start <= end):
        mid = int((start + end)/2)
        if arr[mid] == key:
            ans = mid
            end = mid - 1
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return ans

def last_occ(arr, n, key):
    start = 0
    end = n-1
    ans = -1
    
    while(start <= end):
        mid = int((start + end)/2)
        if arr[mid] == key:
            ans = mid
            start = mid + 1
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return ans

def main():
    arr = list(map(int, input().split()))
    n = len(arr)
    key = int(input())
    print(first_occ(arr, n, key))
    print(last_occ(arr, n, key))

main()