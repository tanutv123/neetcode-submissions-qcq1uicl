class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1 #There is 1 way to reach 0 sum with 0 element

        for i in range(len(nums)):
            next_dp = defaultdict(int)
            for currSum, count in dp.items():
                next_dp[currSum + nums[i]] += count
                next_dp[currSum - nums[i]] += count
            dp = next_dp
        
        return dp[target]