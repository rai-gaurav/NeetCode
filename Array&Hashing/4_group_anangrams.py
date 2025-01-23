# https://neetcode.io/problems/anagram-groups
# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

class Solution:
    # Solution 1
    def groupAnagrams_1(self, strs: List[str]) -> List[List[str]]:
        group_an = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in group_an:
                group_an[sorted_word] = []
            group_an[sorted_word].append(word)
        return list(group_an.values())

    # Solution 2
    def groupAnagrams_2(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
 
