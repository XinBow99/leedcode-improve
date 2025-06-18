"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:

Input: nums = [0,1,1]

Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]

Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:

3 <= nums.length <= 1000
-10^5 <= nums[i] <= 10^5
"""

from typing import List


class Solution:
    def threeSumBrute(self, nums: List[int]) -> List[List[int]]:
        """Brute-force solution. Time: O(n^3)

        Try every combination of triplets (i, j, k), check if sum == 0.
        Use a set to avoid duplicates.

        Args:
            nums: List of integers.

        Returns:
            List of unique triplets that sum to 0.
        """
        res = set()
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                        res.add(triplet)

        return [list(t) for t in res]

    def threeSumTwoPoint(self, nums: List[int]) -> List[List[int]]:
        """Optimal solution using sorting + two pointers. Time: O(n^2)

        For each number in sorted array, use two pointers to find two other numbers
        such that the sum is zero. Skip duplicates carefully.

        Args:
            nums: List of integers.

        Returns:
            List of unique triplets that sum to 0.
        """
        nums.sort()
        res = []

        for i in range(len(nums)):
            # If the number is > 0, no point in continuing (since all are >= this)
            if nums[i] > 0:
                break

            # Skip duplicate base number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # Skip duplicate values after moving the pointers
                    # tip: 
                    #    do l < r first
                    #    do not nums[l] == nums[l - 1] first
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return res


if __name__ == "__main__":
    sol = Solution()
    test = [-1, 0, 1, 2, -1, -4]
    print("Two Pointer Solution:", sol.threeSumTwoPoint(test))
    print("Brute Force Solution:", sol.threeSumBrute(test))
