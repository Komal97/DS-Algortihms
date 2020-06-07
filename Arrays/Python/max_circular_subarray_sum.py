'''
Given n numbers (both +ve and -ve), arranged in a circle, fnd the maximum sum of consecutive number.
Examples:

Input: a[] = {8, -8, 9, -9, 10, -11, 12}
Output: 22 (12 + 8 - 8 + 9 - 9 + 10)

Input: a[] = {10, -3, -4, 7, 6, 5, -4, -1} 
Output:  23 (7 + 6 + 5 - 4 -1 + 10) 
'''

def max_circular_subarray(arr, n):

    max_val = arr[0]
    min_val = arr[0]
    cur_sum_max = 0
    cur_sum_min = 0
    total = 0
    
    for val in arr:
        total = total + val
        cur_sum_max = max(cur_sum_max+val, val)
        cur_sum_min = min(cur_sum_min+val, val)
        max_val = max(max_val, cur_sum_max)
        min_val = min(min_val, cur_sum_min)
    
    return max(total - min_val, max_val) if max_val >=0 else max_val
        
    
def main():
    t = int(input())
    while(t):
        n = int(input())
        arr = input().split()
        for i in range(n):
            arr[i] = int(arr[i])
        print(max_circular_subarray(arr, n))
        t -= 1
    
main()