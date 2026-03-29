class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * (len(nums) + 1)
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)