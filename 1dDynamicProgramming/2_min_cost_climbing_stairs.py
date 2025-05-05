# https://neetcode.io/problems/min-cost-climbing-stairs

# You are given an array of integers cost where cost[i] is the cost of taking a step from the ith floor of a staircase. After paying the cost, you can step to either the (i + 1)th floor or the (i + 2)th floor.
# You may choose to start at the index 0 or the index 1 floor.
# Return the minimum cost to reach the top of the staircase, i.e. just past the last index in cost.

# Input: cost = [1,2,3]
# Output: 2

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for i in range(len(cost) -3 , -1 , -1):
            cost[i] += min(cost[i+1], cost[i+2])
        
        return min(cost[0], cost[1])
