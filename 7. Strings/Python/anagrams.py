'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        h = {}
        
        for ch in s:
            if ch not in h:
                h[ch] = 1 
            else:
                h[ch] += 1
        
        print(h)
        for ch in t:
            if ch not in h:
                return False
            h[ch] -= 1
            if h[ch] < 0:
                return False
        
        return True