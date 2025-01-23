# https://neetcode.io/problems/is-anagram
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# Input: s = "racecar", t = "carrace"
# Output: true

class Solution:
    # Solution 1
    def isAnagram_1(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_freq = {}
        t_freq = {}
        for c in s:
            if c in s_freq:
                s_freq[c] = s_freq[c] + 1
            else:
                s_freq[c] = 1
        
        for c in t:
            if c in t_freq:
                t_freq[c] = t_freq[c] + 1
            else:
                t_freq[c] = 1

        if s_freq != t_freq:        
            return False
        return True

  # Solution 2
  def isAnagram_2(self, s: str, t: str) -> bool:
        if "".join(sorted(s)) == "".join(sorted(t)):
            return True
        return False
