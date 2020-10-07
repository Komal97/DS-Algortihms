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
    def singleNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        ans = 0
        
        for i in range(32):
            count = 0
            for j in range(n):
                count += (nums[j]>>i)&1
                
            rem = count%3
            # For a 32 bit number, if i == 31, we are on the bit telling us whether the number is negative or not. 
            # The statement 'if i == 31 and rem' turns that into, "if we are on the bit that tells us the sign, 
            # and the number that appears not three times has a 1 here", then take the largest 32 bit integer and 
            # subtract it from ans. If the number that we are looking for is negative, 
            # this will give the correct answer.
            if i == 31 and rem:
                ans -= (1<<31)
            else:
                ans |= (rem<<i)

        return ans