# https://neetcode.io/problems/subsets

# Given an array nums of unique integers, return all possible subsets of nums.
# The solution set must not contain duplicate subsets. You may return the solution in any order.

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            # Condition for adding the item (right side of tree)
            subset.append(nums[i])
            dfs(i + 1)

            # Condition for NOT adding the item (left side of tree)
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res
