"""
Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:
Input: nums = [1,2,2,3,3,3], k = 2
Output: [2,3]

Example 2:
Input: nums = [7,7], k = 1
Output: [7]
"""

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """Finds the k most frequent elements from the input list.

        This approach uses a hash map to count frequencies, then uses a
        bucket sort idea to group numbers by how often they appear.

        Args:
            nums: A list of integers (can contain duplicates).
            k: The number of top frequent elements to return.

        Returns:
            A list of k elements that appear most frequently in nums.
        """
        # Step 1: Count the frequency of each number.
        num_times = {}  # Key: number, Value: frequency count
        for num in nums:
            num_times[num] = 1 + num_times.get(num, 0)

        # Step 2: Create a bucket list where index = frequency.
        # For example: bucket[3] will store all numbers that appear 3 times.
        # The max frequency a number can have is len(nums), so we prepare len(nums) + 1 buckets.
        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in num_times.items():
            bucket[freq].append(num)

        # Step 3: Iterate buckets in reverse order to collect the top k frequent numbers.
        result = []
        for freq in range(len(bucket) - 1, 0, -1):
            for num in bucket[freq]:
                result.append(num)
                if len(result) == k:
                    return result

        return result  # Just in case (though problem guarantees valid k)

