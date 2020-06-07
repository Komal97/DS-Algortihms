'''
Given an array of positive integers. The task is to find inversion count of array.
Inversion Count : For an array, inversion count indicates how far (or close) the array is from being sorted. 
If array is already sorted then inversion count is 0. If array is sorted in reverse order that inversion count is the maximum. 
Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
Input:
5
2 4 1 3 5
Output: 3
Explanation:
Testcase 1: The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).
'''
def _mergeSort(arr, n): 
    temp = [0]*n 
    return mergeSort(arr, temp, 0, n-1) 
    
def merge(arr, temp, s, e, mid):
    count = 0
    i = s
    j = mid + 1
    k = s

    while(i <= mid and j <= e):
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
            k += 1
        else:
            temp[k] = arr[j]
            count += (mid-i+1)
            j += 1
            k += 1
    while(i <= mid):
        temp[k] = arr[i]
        i += 1
        k += 1
    while(j <= e):
        temp[k] = arr[j]
        j += 1
        k += 1
    
    for i in range(s, e+1):
        arr[i] = temp[i]
    
    return count
        
def mergeSort(arr, temp, s, e):
    count = 0
    if s < e:
        mid = (s+e)//2
        count += mergeSort(arr, temp, s, mid)
        count += mergeSort(arr, temp, mid+1, e)
        count += merge(arr, temp, s, e, mid)
    return count
    
if __name__ =='__main__':
    t = int(input())
    while(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(_mergeSort(arr, n))
        t -= 1
