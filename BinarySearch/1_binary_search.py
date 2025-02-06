# https://neetcode.io/problems/binary-search
# You are given an array of distinct integers nums, sorted in ascending order, and an integer target.
# Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.
# Your solution must run in O(logn)O(logn) time.

# Input: nums = [-1,0,2,4,6,8], target = 4
# Output: 3

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first = 0
        last = len(nums) -1

        while first <= last:
            mid =  first + ((last - first) // 2)
            if nums[mid] < target:
                first = mid + 1
            elif nums[mid] > target:
                last = last - 1 
            else:
                return mid
        return -1
