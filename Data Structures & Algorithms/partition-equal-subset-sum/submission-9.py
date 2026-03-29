class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        maxSum = 0

        for num in nums:
            maxSum += num
        
        if maxSum % 2 != 0:
            return False
        
        def dfs(i, currTotal):
            if currTotal == (maxSum / 2):
                return True
            if i == n or currTotal > (maxSum / 2):
                return False
            
            return dfs(i + 1, currTotal) or dfs(i + 1, currTotal + nums[i])
            
        return dfs(0,0)
            

