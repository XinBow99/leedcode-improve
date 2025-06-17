"""
Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use
O(1) additional space.

Example 1:

Input: numbers = [1,2,3,4], target = 3

Output: [1,2]
Explanation:
The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1, index2 = 2. We return [1, 2].

Constraints:

2 <= numbers.length <= 1000
-1000 <= numbers[i] <= 1000
-1000 <= target <= 1000

"""

from typing import List


class Solution:
    def twoSum_n2(self, numbers: List[int], target: int) -> List[int]:
        """Brute-force solution. Time: O(n^2)

        Try every pair (l, r) and check if their sum matches the target.

        Args:
            numbers: Sorted list of integers.
            target: The target sum.

        Returns:
            0-based indices of the two numbers adding up to target.
        """
        ans = [0, 0]
        for l in range(len(numbers) - 1):
            ans[0] = l
            r = len(numbers) - 1
            while l < r:
                if numbers[l] + numbers[r] == target:
                    return [l, r]
                r -= 1
        return []

    def twoSum_nlogn(self, numbers: List[int], target: int) -> List[int]:
        """Binary search solution. Time: O(n log n)

        For each number, use binary search to find its complement (target - num).

        Args:
            numbers: Sorted list of integers.
            target: The target sum.

        Returns:
            1-based indices of the two numbers adding up to target.
        """
        for i in range(len(numbers)):
            l = i + 1
            r = len(numbers) - 1
            tmp = target - numbers[i]

            while l <= r:
                mid = (r + l) // 2
                if numbers[mid] == tmp:
                    return [i + 1, mid + 1]  # Return 1-based index
                elif tmp > numbers[mid]:
                    l = mid + 1  # Move right
                else:
                    r = mid - 1  # Move left
        return []

    def twoSumTwoPointer_n(self, numbers: List[int], target: int) -> List[int]:
        """Two-pointer solution. Time: O(n)

        Use two pointers from both ends to find the target sum efficiently.

        Args:
            numbers: Sorted list of integers.
            target: The target sum.

        Returns:
            1-based indices of the two numbers adding up to target.
        """
        l = 0
        r = len(numbers) - 1

        while l < r:
            tmp = numbers[l] + numbers[r]
            if tmp == target:
                return [l + 1, r + 1]  # 1-based index
            elif tmp > target:
                r -= 1  # Too big, move right pointer left
            else:
                l += 1  # Too small, move left pointer right
        return []


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSumTwoPointer([1, 2, 3, 4], 6))
