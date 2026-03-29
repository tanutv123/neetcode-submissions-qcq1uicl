class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        dp = [1] * (n + 1)
        dp[-1] = -1
        for i in range(n - 1, -1 ,-1):
            for j in range(i, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)
            
