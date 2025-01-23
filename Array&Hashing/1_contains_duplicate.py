# https://neetcode.io/problems/duplicate-integer
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
# Input: nums = [1, 2, 3, 3]
# Output: true

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = set(nums)
        if len(a) == len(nums):
            return False
        return True
