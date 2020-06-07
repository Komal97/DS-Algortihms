'''
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
'''

class Solution:
    def countBits(self, num: int):
        count = -1
        while(num):
            num = num >> 1
            count += 1
        return count
        
    def findComplement(self, num: int) -> int:
        
        c = self.countBits(num)
        mask = 0
        while(c>=0):
            mask = mask | (1<<c)
            c -= 1
        
        num = num ^ mask
        
        return num