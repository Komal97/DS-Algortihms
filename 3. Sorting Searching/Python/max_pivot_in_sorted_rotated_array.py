'''
Input an array
Array is sorted but rotated (example: 7, 8, 1, 2, 3, 4, 5)
Find pivot element about which element is rotated (Here answer is 8)
'''

def find_pivot(arr, n):
    start = 0
    end = n-1

    while(start <= end):
        mid = int((start + end)/2)

        if mid+1 < n and arr[mid] > arr[mid + 1]:
            return mid
        elif mid-1 >= 0 and arr[mid] < arr[mid - 1]:
            return mid - 1
        elif arr[mid] < arr[start]:
            end = mid - 1
        else:
            start = mid + 1
 
    return -1

def main():
    
    arr = list(map(int, input().split()))
    n = len(arr)
    index = find_pivot(arr, n)
    if index == -1:
        print("No index found")
    else:
        print("Pivot element is found at index", index)

main()