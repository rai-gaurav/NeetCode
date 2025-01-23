# https://neetcode.io/problems/products-of-array-discluding-self
# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
# Input: nums = [1,2,4,6]
# Output: [48,24,12,8]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output = [1] * length

        prefix = 1
        for i, num in enumerate(nums):
            output[i] = prefix
            prefix *= num
        
        postfix = 1
        for i in range(length -1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        
        return output
