class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def dfs(i, prevIndx):
            if i == len(nums):
                return 0
            
            total = dfs(i + 1, prevIndx)
            if prevIndx == -1 or nums[prevIndx] < nums[i]:
                total = max(total, 1 + dfs(i + 1, i))
            return total
        
        return dfs(0, -1)