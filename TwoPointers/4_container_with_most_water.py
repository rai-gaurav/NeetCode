# https://neetcode.io/problems/max-water-container
# You are given an integer array heights where heights[i] represents the height of the ithith bar.
# You may choose any two bars to form a container. Return the maximum amount of water a container can store.
# Input: height = [1,7,2,5,4,7,3,6]
# Output: 36

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        size = len(heights)
        l, r = 0, size -1
        max_water = 0
        while l < r:
            water_store = (r - l) * (min(heights[l], heights[r]))
            if max_water < water_store:
                max_water = water_store
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return max_water


        
