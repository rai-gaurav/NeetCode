# https://neetcode.io/problems/top-k-elements-in-list
# Given an integer array nums and an integer k, return the k most frequent elements within the array.
# Input: nums = [1,2,2,3,3,3], k = 2

# Output: [2,3]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        
        arr = []
        for num, count in frequency.items():
            arr.append([count, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        
        return res
