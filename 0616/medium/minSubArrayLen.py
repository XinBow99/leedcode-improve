"""
209. Minimum Size Subarray Sum
Medium
Topics
premium lock icon
Companies
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
"""
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """Finds the minimal length of a contiguous subarray of which 
        the sum is at least target.

        Uses sliding window approach to maintain current subarray.

        Args:
            target: Target sum.
            nums: List of positive integers.

        Returns:
            The minimal length of the subarray; 0 if no valid subarray exists.
        """
        l = 0  # Left boundary of sliding window
        total = 0  # Current window sum
        res = float('inf')  # Result placeholder

        for r in range(len(nums)):
            # Expand window by adding nums[r]
            total += nums[r]

            # Contract window while the sum is enough
            while total >= target:
                # Update result with smaller window
                res = min(res, r - l + 1)
                # Shrink window from the left
                total -= nums[l]
                l += 1

        return 0 if res == float('inf') else res

print(Solution.minSubArrayLen(None, 7, [2,3,1,2,4,3]))