class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)

        def dfs(i):
            if i >= len(nums):
                return 0
            
            if dp[i] != 0:
                return dp[i]
            
            dp[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))

            return dp[i]
        
        return dfs(0)