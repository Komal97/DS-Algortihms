'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
Find the minimum element.The array may contain duplicates.

Example 1:
Input: [3,1,3]
Output: 1

Example 2:
Input: [2,2,2,0,1]
Output: 0
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
		start = 0
		n = len(nums)
		end = n - 1
		
		if n==0:
			return -1
		elif n==1:
			return nums[0]
		elif nums[start] < nums[end]:
			return nums[0]
		
		while start <= end:
			
			while(start < end and nums[start] == nums[end]):
				start += 1
			
			mid = int((start + end)/2)
			
			if mid+1 <n and nums[mid] > nums[mid + 1]:
				return nums[mid+1]
			elif mid-1>=0 and nums[mid] < nums[mid - 1]:
				return nums[mid]
			elif nums[end] < nums[mid]:
				start = mid + 1
			else:
				end = mid - 1
				
				
		return nums[end]