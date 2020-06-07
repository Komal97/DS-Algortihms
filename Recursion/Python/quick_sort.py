'''
input a unsorted array
output is sorted array

to avoid worst case scenario - which is sorted array, shuffling of array is done
'''
import random

def partition(arr, s, e):
    
    i = s-1           # denote left part of pivot
    j = s             # denote right part of pivot
    pivot = arr[e]
    while(j <= e-1):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1
        
    arr[i+1], arr[e] = arr[e], arr[i+1]
    return i+1

def quicksort(arr, s, e):
    if s >= e:
        return
    p = partition(arr, s, e)
    quicksort(arr, s, p-1)
    quicksort(arr, p+1, e)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    random.shuffle(arr)	
    print(arr)
    quicksort(arr, 0, n-1)
    print(arr)