https://neetcode.io/problems/two-integer-sum
# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
# Input: 
# nums = [3,4,5,6], target = 7
# Output: [0,1]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            diff = (target - nums[i])
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[nums[i]] = i
