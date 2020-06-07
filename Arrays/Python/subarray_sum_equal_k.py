'''
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
'''

class Solution:

# method -1 Cumulative sum method - O(n^2) approach
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        cs = []
        cs.append(nums[0])
        n = len(nums)
        count = 0
        
        for i in range(1, n):
            cs.append(cs[i-1] + nums[i])
        
        for i in range(0, n):
            for j in range(i, n):
                
                if i-1<0 and cs[j] == k:
                    count += 1
                elif i > 0 and cs[j] - cs[i-1] == k:
                    count += 1

        return count
		
# method - 2 creating subarrays by keeping 2 pointers - O(n^2) approach
	def subarraySum(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        count = 0
       
        for i in range(0, n):
            sum = 0
            for j in range(i, n):
                
                sum = sum + nums[j]
                if sum == k:
                    count += 1

        return count

#method - 3 - O(n) approach and O(n) space
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        count = 0
        currsum = 0
        
        h = defaultdict(lambda:0)
        
        for i in range(0, n):
            
            currsum += nums[i]
            
            if currsum == k:
                count += 1
            
            if currsum-k in h:
                count += h[currsum-k]
            
            h[currsum] += 1
            

        return count
		
# method -1 (if all elements are positive) --> two pointer approach

	def subarraySum(self, nums: List[int], k: int) -> int:
		
		n = len(nums)
		curr_sum = nums[0] 
		start = 0
    	i = 1
		
		while i <= n: 
			  
			while curr_sum > k and start < i-1: 
				curr_sum = curr_sum - nums[start] 
				start += 1
				   
			if curr_sum == k: 
				count += 1
	   
			if i < n: 
				curr_sum = curr_sum + nums[i] 
			i += 1
		return count
 
  