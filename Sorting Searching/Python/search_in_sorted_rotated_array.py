'''
Input an array
Array is sorted but rotated (example: 7, 8, 1, 2, 3, 4, 5)
Find an element in this array using binary search 
'''

def search_in_rotated_array(arr, key, start, end):
    
    if start > end:
        return -1
    
    mid = int((start + end)/2)

    if arr[mid] == key:
        return mid
    # check if left part of mid is sorted and after that whether key lies on first part
    if arr[start] <= arr[mid]:
        if arr[start] <= key and key <= arr[mid]:
            return search_in_rotated_array(arr, key, start, mid - 1)
        else:
            return search_in_rotated_array(arr, key, mid + 1, end)
    # means second part is sorted and check whether key lies in second part or first part
    if arr[mid] <= key and key <= arr[end]:
         return search_in_rotated_array(arr, key, mid + 1, end)
    return search_in_rotated_array(arr, key, start, mid - 1)


def main():
    
    arr = list(map(int, input().split()))
    n = len(arr)
    key = int(input())
    print(search_in_rotated_array(arr, key, 0, n-1))

main()