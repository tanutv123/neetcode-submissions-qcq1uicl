class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        
        if total % 2 != 0:
            return False

        target = total // 2
        
        def dfs(i, currTotal):
            if currTotal == target:
                return True
            if i == n or currTotal > target:
                return False
            
            return dfs(i + 1, currTotal) or dfs(i + 1, currTotal + nums[i])
        
        return dfs(0, 0)
