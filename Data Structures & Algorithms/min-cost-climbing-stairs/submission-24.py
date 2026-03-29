class Solution:
    def minCostClimbingStairs(self, costs: List[int]) -> int:
        n = len(costs)
        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            dp[i] = min(costs[i - 1] + dp[i - 1], costs[i - 2] + dp[i - 2])
        
        return dp[n]