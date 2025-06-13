"""
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 
"""
from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # first we check the two variable length
        if len(s) != len(t):
            return False
        
        countS = {}
        countT = {}

        # cause two varible length are equal
        # we iterate S str
        for i in range(len(s)):
            countS[s[i]] = 1+countS.get(s[i],0)
            countT[t[i]] = 1+countT.get(t[i],0)
        # Time complexity: O(n+m) 
        # Space complexity: O(1)
        return countS == countT