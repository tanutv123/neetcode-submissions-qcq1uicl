class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, total, subSet):
            if total == target:
                res.append(subSet.copy())
                return
            
            if i >= len(nums) or total > target:
                return
            
            subSet.append(nums[i])
            dfs(i, total + nums[i], subSet)
            subSet.pop()

            dfs(i + 1, total, subSet)
        
        dfs(0, 0, [])
        return res