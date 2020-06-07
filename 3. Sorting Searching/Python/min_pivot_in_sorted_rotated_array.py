'''
Input an array
Array is sorted but rotated (example: 7, 8, 1, 2, 3, 4, 5)
Find minimum element about which element is rotated (Here answer is 1)
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        start = 0
        n = len(nums)
        end = n - 1
        
        if n == 0:
            return -1
        elif n == 1:
            return nums[0]
        elif nums[start] < nums[end]:
            return nums[start]
        
        
        while(start <= end):
            mid = int((start + end)/2)
            
            if (mid-1) >= 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif mid+1 < n and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[start] > nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        
                
                