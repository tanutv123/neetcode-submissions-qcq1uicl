class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        subSet = []

        def dfs(i, total):
            if total == target:
                res.append(subSet.copy())
                return
            
            for j in range(i, len(nums)):
                if total > target:
                    return
                subSet.append(nums[j])
                dfs(j, total + nums[j])
                subSet.pop()
        dfs(0, 0)
        return res