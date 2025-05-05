# https://neetcode.io/problems/climbing-stairs
# You are given an integer n representing the number of steps to reach the top of a staircase. You can climb with either 1 or 2 steps at a time.
# Return the number of distinct ways to climb to the top of the staircase.

# Input: n = 2
# Output: 2

class Solution:
    def climbStairs(self, n: int) -> int:
        first, second = 1, 1

        for i in range(n - 1):
            temp = first
            first = first + second
            second = temp
        
        return first
