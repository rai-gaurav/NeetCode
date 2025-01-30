# https://neetcode.io/problems/three-integer-sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.
# The output should not contain any duplicate triplets. You may return the output and the triplets in any order.
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i, item in enumerate(nums):
            if item > 0:
                break
            if i > 0 and item == nums[i-1]:
                continue
            j, k = i+1, len(nums) - 1
            while j < k:
                threeSum = item + nums[j] + nums[k]
                if threeSum < 0:
                    j +=1
                elif threeSum > 0:
                    k -=1
                else:
                    result.append([item,nums[j],nums[k]])
                    j, k = j+1, k-1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
        return result
