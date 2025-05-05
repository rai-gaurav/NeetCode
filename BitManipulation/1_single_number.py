# https://neetcode.io/problems/single-number

# You are given a non-empty array of integers nums. Every integer appears twice except for one.
# Return the integer that appears only once.
# You must implement a solution with O(n)O(n) runtime complexity and use only O(1)O(1) extra space.

# Input: nums = [3,2,3]
# Output: 2

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique = []
        for num in nums:
            if num not in unique:
                unique.append(num)
            else:
                unique.remove(num)
        return unique[0]
