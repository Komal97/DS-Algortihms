'''
https://www.interviewbit.com/problems/aggressive-cows/
Farmer John has built a new long barn, with N stalls.
Given an array of integers A of size N where each element of the array represents the location of the stall,
and an integer B which represent the number of cows.

His cows don’t like this barn layout and become aggressive towards each other once put
into a stall. To prevent the cows from hurting each other, John wants to assign the cows to the stalls,
such that the minimum distance between any two of them is as large as possible. What is the largest minimum distance?
Input 1:
    A = [1, 2, 3, 4, 5]
    B = 3
Output 1:
    2

Input 2:
    A = [5, 17, 100, 11]
    B = 2
Output 2:
    95
'''

# similar to book allocation problem with little twist
# search space is from 0 to max value because max dist between 2 cow can be only between 0 and max value
# using binary search, we find what can be max dist between 2 cows, if satisfies then we move right and check that
# can we make more dist between them
class Solution:
    def isValid(self, A, max_dist, no_of_cows):
        cow = 1
        dist = A[0]
        for num in A:
            if num-dist >= max_dist:
                dist = num
                cow += 1
            if cow >= no_of_cows:
                return True
        return False
                
        
    def solve(self, A, B):
        A.sort()
        s = 0
        e = A[len(A)-1] - s
        ans = -1
       
        while s<=e:
            mid = s + (e-s)//2
            if self.isValid(A, mid, B):
                ans = mid
                s = mid+1
            else:
                e = mid-1
        return ans
                
        