class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) // 2

        def dfs(i, total):
            if total > target:
                return False
            
            if i >= len(nums):
                return False
            
            if total == target:
                return True
            
            return dfs(i + 1, total) or dfs(i + 1, total + nums[i])
        
        return dfs(0, 0)
            
