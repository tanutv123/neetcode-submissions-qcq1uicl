class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            
            if i == len(nums) or total > target:
                return
            
            curr.append(nums[i])
            dfs(i + 1, curr, total + nums[i])
            curr.pop()
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            dfs(i + 1, curr, total)
        dfs(0, [], 0)
        return res