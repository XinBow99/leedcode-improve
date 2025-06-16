"""
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false
Explanation: "tabacat" is not a palindrome.
"""


class Solution:
    def isPalindromeReverse(self, s: str) -> bool:
        """Checks if a string is a valid palindrome using string reversal.

        This method first filters out non-alphanumeric characters and converts
        the string to lowercase. Then it checks if the cleaned string equals its reverse.

        Time Complexity: O(n)
        Space Complexity: O(n)

        Args:
            s: Input string.

        Returns:
            True if it's a palindrome, False otherwise.
        """
        new_str = ""
        for c in s:
            if c.isalnum():
                new_str += c.lower()
        return new_str == new_str[::-1]

    def isPalindromeTwoPointer(self, s: str) -> bool:
        """Checks if a string is a valid palindrome using two pointers.

        This method avoids creating a new string.
        It uses left and right pointers to skip non-alphanumeric characters
        and compares letters in place (case-insensitive).

        Time Complexity: O(n)
        Space Complexity: O(1)

        Args:
            s: Input string.

        Returns:
            True if it's a palindrome, False otherwise.
        """
        l = 0
        r = len(s) - 1

        while l < r:
            # Move left pointer forward if not alphanumeric
            while l < r and not s[l].isalnum():
                l += 1

            # Move right pointer backward if not alphanumeric
            while r > l and not s[r].isalnum():
                r -= 1

            # Compare characters (lowercased)
            if s[l].lower() != s[r].lower():
                return False

            # Move both pointers inward
            l += 1
            r -= 1

        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindromeTwoPointer("Was it a car or a cat I saw?"))
