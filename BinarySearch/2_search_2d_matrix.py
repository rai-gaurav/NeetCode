# https://neetcode.io/problems/search-2d-matrix
# You are given an m x n 2-D integer array matrix and an integer target.
#     Each row in matrix is sorted in non-decreasing order.
#     The first integer of every row is greater than the last integer of the previous row.
# Return true if target exists within matrix or false otherwise.

# Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
# Output: true

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target > row[-1]:
                continue
            elif target < row[-1]:
                left, right = 0, len(row) -1
                while left <= right:
                    mid = left + ((right - left) // 2)
                    if target > row[mid]:
                        left  = mid + 1
                    elif target < row[mid]:
                        right = mid -1
                    else:
                        return True
            else:
                return True
        return False
