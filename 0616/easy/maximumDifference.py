"""
2016. Maximum Difference Between Increasing Elements
Easy
Topics
premium lock icon
Companies
Hint
Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].

Return the maximum difference. If no such i and j exists, return -1.

 

Example 1:

Input: nums = [7,1,5,4]
Output: 4
Explanation:
The maximum difference occurs with i = 1 and j = 2, nums[j] - nums[i] = 5 - 1 = 4.
Note that with i = 1 and j = 0, the difference nums[j] - nums[i] = 7 - 1 = 6, but i > j, so it is not valid.
Example 2:

Input: nums = [9,4,3,2]
Output: -1
Explanation:
There is no i and j such that i < j and nums[i] < nums[j].
Example 3:

Input: nums = [1,5,2,10]
Output: 9
Explanation:
The maximum difference occurs with i = 0 and j = 3, nums[j] - nums[i] = 10 - 1 = 9.
 

Constraints:

n == nums.length
2 <= n <= 1000
1 <= nums[i] <= 109
"""
from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        """Returns the maximum difference nums[j] - nums[i] 
        where j > i and nums[j] > nums[i].

        If no such pair exists, return -1.

        Args:
            nums: List of integers.

        Returns:
            Maximum difference or -1 if condition not met.
        """
        min_val = nums[0]  # Track the minimum value so far
        result = -1

        for i in range(1, len(nums)):
            if nums[i] > min_val:
                # Found a larger number after a smaller one
                result = max(result, nums[i] - min_val)
            else:
                # Update min_val if current value is smaller
                min_val = nums[i]

        return result


# Call the method using an instance of Solution
if __name__ == "__main__":
    sol = Solution()
    print(sol.maximumDifference(
        [999, 997, 980, 976, 948, 940, 938, 928, 924, 917, 907, 907, 881, 878, 864, 862, 859, 857, 848, 840, 824, 824, 824, 805, 802, 798, 788, 777, 775, 766, 755, 748, 735, 732, 727, 705, 700, 697, 693, 679, 676, 644, 634, 624, 599, 596, 588, 583, 562,
            558, 553, 539, 537, 536, 509, 491, 485, 483, 454, 449, 438, 425, 403, 368, 345, 327, 287, 285, 270, 263, 255, 248, 235, 234, 224, 221, 201, 189, 187, 183, 179, 168, 155, 153, 150, 144, 107, 102, 102, 87, 80, 57, 55, 49, 48, 45, 26, 26, 23, 15]
    ))
