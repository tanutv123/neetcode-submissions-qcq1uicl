class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i, total, subSet):
            if total == target:
                res.append(subSet.copy())
                return
            
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + total > target:
                    break
                
                subSet.append(nums[j])
                dfs(j + 1, total + nums[j], subSet)
                subSet.pop()
        
        dfs(0, 0, [])
        return res