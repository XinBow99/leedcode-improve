from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """Finds the duplicate number in an array using Floyd's cycle detection.

        This approach treats the array as a linked list where each index points
        to the next node (i.e., nums[i] is the next node). A duplicate means there's a cycle.

        Args:
            nums: A list of integers where:
                  - The integers are in the range [1, n] inclusive.
                  - The list contains n + 1 integers (at least one duplicate).

        Returns:
            The duplicate number that appears more than once.
        """
        # Step 1: Initialize both pointers (tortoise and hare).
        turtle = nums[0]
        rabbit = nums[0]

        # Step 2: First phase - Find the intersection point inside the cycle.
        while True:
            turtle = nums[turtle]
            rabbit = nums[nums[rabbit]]
            if turtle == rabbit:
                break  # Cycle detected

        # Step 3: Second phase - Reset one pointer and move both at same speed.
        turtle = nums[0]
        while turtle != rabbit:
            turtle = nums[turtle]
            rabbit = nums[rabbit]

        # Step 4: The point where they meet is the duplicate number.
        return turtle