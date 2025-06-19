"""
Encode and Decode Strings
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.
"""

from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings into a single string.

        The format is: <len>#<string><len>#<string>...

        Args:
            strs: List of strings to encode.

        Returns:
            A single encoded string.
        """
        if not strs:
            return ""
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string into a list of strings.

        Parses using the <len>#<string> pattern.

        Args:
            s: The encoded string.

        Returns:
            The original list of strings.
        """
        res = []
        i = 0
        while i < len(s):
            j = i
            # Find the delimiter #
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length]
            res.append(word)
            i = j + 1 + length  # Move to next block
        return res


if __name__ == "__main__":
    sol = Solution()
    encoded = sol.encode(["we", "say", ":", "yes"])
    decoded = sol.decode(encoded)
    print("Encoded:", encoded)  # For debugging
    print("Decoded:", decoded)  # Should print: ['we', 'say', ':', 'yes']