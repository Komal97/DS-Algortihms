'''
Given an unsorted array of integers, sort the array into a wave like array. An array ‘arr[0..n-1]’ is sorted in wave form if arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= …..
Examples:
Input:  arr[] = {10, 5, 6, 3, 2, 20, 100, 80}
Output: arr[] = {10, 5, 6, 2, 20, 3, 100, 80} OR
                {20, 5, 10, 2, 80, 6, 100, 3} OR
                any other array that is in wave form
'''

def wave_array(arr, n):

    for i in range(0, n, 2):
        if i > 0 and arr[i] < arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
        
        if i+1<n and arr[i] < arr[i+1]:
          arr[i], arr[i+1] = arr[i+1], arr[i]
    
    for num in arr:
        print(num, end = " ")
          
    
def main():
    t = int(input())
    while(t):
        n = int(input())
        arr = input().split()
        for i in range(n):
            arr[i] = int(arr[i])
        wave_array(arr, n)
        print()
        t -= 1
    
main()