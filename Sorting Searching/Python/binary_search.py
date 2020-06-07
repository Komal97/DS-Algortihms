'''
Input an array
Search an element using binary search 
Complexity - O(log n)
'''
def main():
    arr = list(map(int, input().split()))
    n = len(arr)
    start = 0
    end = n-1
    key = int(input())

    while(start <= end):
        mid = int((start + end)/2)
        if arr[mid] == key:
            print("Element found at index: ", mid)
            break
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1

main()