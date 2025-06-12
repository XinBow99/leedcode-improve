"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""
from typing import List

class Solution:
    def twoSum(nums: List[int], target: int) -> List[int]:
        """Finds indices of the two numbers in the list that sum up to the target.

        Args:
            nums: A list of integers.
            target: The target integer we want two numbers in the list to sum to.

        Returns:
            A list containing the indices of the two numbers whose sum is equal to target.
        """
        # Hash map to store the complement value and its corresponding index.
        # Example:
        # Input: nums = [1, 2, 3, 4], target = 7
        # Iteration:
        # i = 0, num = 1, target - num = 6 -> store {6: 0}
        # i = 1, num = 2, target - num = 5 -> store {5: 1}
        # i = 2, num = 3, target - num = 4 -> store {4: 2}
        # i = 3, num = 4 -> found in dict (4 in seen), return [3, seen[4]] = [3, 2]
        seen = {}

        for i, num in enumerate(nums):
            result = target - num
            # If current number already exists in seen, we found a match.
            if num in seen:
                return [i, seen[num]]
            # Otherwise, store the result (what we’re hoping to see later) in the map.
            seen[result] = i

        # If no valid pair is found, return None (though by problem constraints, this won't happen).
        return


if __name__ == "__main__":
    test_cases = [
        {
            'input': {
                'case': [2, 7, 11, 15],
                'target': 9
            },
            'output': [0, 1]
        },
        {
            'input': {
                'case': [3, 2, 4],
                'target': 6
            },
            'output': [1, 2]
        },
        {
            'input': {
                'case': [3, 3],
                'target': 6
            },
            'output': [0, 1]
        },
        {
            'input': {
                'case': [0, 1],
                'target': 1
            },
            'output': [0, 1]
        },
        {
            'input': {
                'case': [0, 0],
                'target': 0
            },
            'output': [0, 1]
        },
    ]

    for test in test_cases:
        data_input = test['input']
        assert sorted(Solution.twoSum(data_input['case'], data_input['target'])) == sorted(test['output'])
