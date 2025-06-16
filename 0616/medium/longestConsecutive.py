"""
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [2,20,4,10,3,4,5]
Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:
Input: nums = [0,3,2,5,4,6,1,1]
Output: 7
Constraints:

0 <= nums.length <= 1000
-10^9 <= nums[i] <= 10^9
"""
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """Finds the length of the longest consecutive sequence in an unsorted array.

        Uses a hash set to check for sequence starts and expands them.
        Time complexity is O(n).

        Args:
            nums: List of unsorted integers.

        Returns:
            Length of the longest consecutive elements sequence.
        """
        nums_set = set(nums)
        res = 0

        for num in nums_set:
            # Only start counting when this num is the beginning of a sequence
            if (num - 1) not in nums_set:
                length = 1
                while (num + length) in nums_set:
                    length += 1
                res = max(res, length)

        return res