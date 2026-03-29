class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, total, subSet):
            if total == target:
                res.append(subSet.copy())
                return
            
            if i >= len(nums) or total > target:
                return
            
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    break
                subSet.append(nums[j])
                dfs(j, total + nums[j], subSet)
                subSet.pop()
        
        dfs(0, 0, [])
        return res