# https://neetcode.io/problems/longest-substring-without-duplicates
# Given a string s, find the length of the longest substring without duplicate characters.
# A substring is a contiguous sequence of characters within a string.
# Input: s = "zxyzxyz"
# Output: 3

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        larg_substring = set()
        left = 0
        maxLength = 0
        
        for right in range(len(s)):
            if s[right] not in larg_substring:
                larg_substring.add(s[right])
                maxLength = max(maxLength, right-left + 1)
            else:
                while s[right] in larg_substring:
                    larg_substring.remove(s[left])
                    left += 1
                larg_substring.add(s[right])
        return maxLength

