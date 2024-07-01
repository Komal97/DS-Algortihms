'''
input a unsorted array
output is sorted array

to avoid worst case scenario - which is sorted array, shuffling of array is done
'''
import random

def partition(arr, s, e):
    i = s     # denotes left side of pivot which is lesser than pivot
    j = s     # denotes right side of pivot which is greater than pivot

    pivot = arr[e]
    while j <= e:
        if arr[j] <= pivot:        # if current value is smaller, means move it to left side (denoted by i)
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        else:
            j += 1
    return i-1

def quickSort(arr, s, e):
    if s >= e:
        return

    pi = partition(arr, s, e)    # pi is the index which is at sorted place
    quickSort(arr, s, pi-1)
    quickSort(arr, pi+1, e)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    random.shuffle(arr)	
    print(arr)
    quicksort(arr, 0, n-1)
    print(arr)