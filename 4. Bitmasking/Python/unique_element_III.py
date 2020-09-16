'''
https://www.interviewbit.com/problems/single-number-ii/
Given an array of integers, every element appears thrice except for one which occurs once.
Find that element which does not appear thrice. 
Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
Input:
A = [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
Output:
4
Explanation:
4 occur exactly once

Input:
A = [0, 0, 0, 1]
Output:
1
'''

def find_3_unique_elements(arr, n):
    
    cnt = [0 for _ in range(64)]
    
    for i in range(n):
        j = 0
        val = arr[i]
        while(val):
            cnt[j] += (val&1)
            val = val>>1
            j += 1

    p = 1
    ans = 0    
    for i in range(64):
        cnt[i] %= 3
        ans += (p*cnt[i])
        p = p<<1
    print(ans)

arr = list(map(int, input().split()))
n = len(arr)
find_3_unique_elements(arr, n)




class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        
        A = list(A)
        res = 0
        for i in range(64):
            j = 0
            cnt = 0
            while j < len(A):
                cnt += (A[j]&1)
                val = A[j]>>1
                A[j] = int(val)
                j += 1
            res |= ((cnt%3)<<i)
            
            
        return res
                