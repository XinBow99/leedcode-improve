"""
Products of Array Except Self
Solved
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in
O
(
n
)
O(n) time without using the division operation?

Example 1:

Input: nums = [1,2,4,6]

Output: [48,24,12,8]
Example 2:

Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]
Constraints:

2 <= nums.length <= 1000
-20 <= nums[i] <= 20
"""

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """Returns an array where each element is the product of all 
        other elements except itself.

        This solution avoids using division and runs in O(n) time.

        Args:
            nums: A list of integers.

        Returns:
            A list where each element is the product of all other elements.
        """
        nums_len = len(nums)
        res = [0] * nums_len

        # Step 1: Left prefix pass
        # Initialize first value as 1, since there's no element before index 0
        res[0] = 1
        curr = nums[0]

        # Build prefix products from left to right
        # res[i] stores the product of all elements before index i
        for i in range(1, nums_len):
            res[i] = curr
            curr *= nums[i]

        # Step 2: Right suffix pass
        # Use a running product from the right side
        curr = nums[-1]

        # Multiply the suffix into the result array (which already has prefix values)
        for i in range(nums_len - 2, -1, -1):
            res[i] *= curr
            curr *= nums[i]
        # time complexity is O(n)
        # space complexity O(1) ---- curr
        # ans  (The output array does not count as extra space for space complexity analysis.)
        return res

