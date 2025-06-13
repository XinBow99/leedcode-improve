"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]
"""

from typing import List, DefaultDict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """Groups anagrams from the input list of strings.

        Anagrams are words that have the same character counts.
        For example: "tan" and "nat" are anagrams because they both contain:
            a:1, n:1, t:1

        We use a frequency counter (hash_word) of length 26 (a-z),
        and treat it as a signature (key) to group words with the same pattern.

        Args:
            strs: A list of strings to be grouped.

        Returns:
            A list of groups, where each group contains anagrams.
        """
        # Initialize a defaultdict to store grouped anagrams.
        # The key is a tuple of character counts.
        hash_group = DefaultDict(list)

        for word in strs:
            # Create a 26-length array to count letters in the word.
            hash_word = [0] * 26
            for chr in word:
                hash_word[ord(chr) - ord("a")] += 1

            # Use the tuple version of hash_word as the key (must be hashable).
            hash_group[tuple(hash_word)].append(word)

        # Convert the dict values to a list of lists and return.
        return list(hash_group.values())