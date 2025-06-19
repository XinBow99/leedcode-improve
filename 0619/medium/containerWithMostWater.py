"""
Container With Most Water
You are given an integer array heights where heights[i] represents the height of the 
i
t
h
i 
th
  bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.


Input: height = [1,7,2,5,4,7,3,6]
Output: 36
"""
from typing import List
class Solution:
    def maxAreaBrute(self, heights: List[int]) -> int:
        res = float('-inf')
        for l in range(len(heights)):
            for r in range(l+1, len(heights)):
                # res is the max value of min height multiply dist(r - l)
                # time: O(n^2)
                # space: O(1)
                res = max(min(heights[l], heights[r]) * (r - l) , res)
        return res
    def maxAreaTwoPointer(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = 0
        while l < r:
            area = min(heights[r], heights[l]) * (r-l)
            res = max(res, area)
            # this is greedy for find higher height
            if heights[l] <= heights[r]:
                l += 1# move shorter one
            else:
                r -= 1# move shorter one
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxAreaTwoPointer([1,7,2,5,4,7,3,6]))