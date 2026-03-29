class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subSet = []
        nums.sort()
        def dfs(i, curr, subSet):
            if curr == target:
                res.append(subSet.copy())
                return
            
            for j in range(i, len(nums)):
                if curr + nums[j] > target:
                    break
                subSet.append(nums[j])
                dfs(j, curr + nums[j], subSet)
                subSet.pop()
        
        dfs(0, 0, [])
        return res