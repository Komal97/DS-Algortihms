'''
Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.

Example 1:
Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
 
Note:
1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000
'''

class Solution:
# method 1
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        
        n = len(A)
        sum = 0
        h = {}
        h[0] = 1
        
        for i in range(n):
            sum += A[i]
            sum %= K
            sum = (sum+K) % K
            if sum not in h:
                h[sum] = 1
            else:
                h[sum] += 1
            
        ans = 0
        for key in h:
            val = h[key]
            val = val *(val-1)
            ans = ans + int(val/2)
        return ans

# method 2 - above code in less number of lines
	def subarraysDivByK(self, A, K):
			P = [0]
			for x in A:
				P.append((P[-1] + x) % K)

			count = collections.Counter(P)
			return sum(int(v*(v-1)/2) for v in count.values())