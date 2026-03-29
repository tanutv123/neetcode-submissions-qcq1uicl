class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [defaultdict(int) for _ in range(len(nums) + 1)]
        dp[0][0] = 1 #There is 1 way to reach 0 sum with 0 element

        for i in range(len(nums)):
            for currSum, count in dp[i].items():
                dp[i+1][currSum + nums[i]] += count
                dp[i+1][currSum - nums[i]] += count
        return dp[len(nums)][target]