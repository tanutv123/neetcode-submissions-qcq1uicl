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
            
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                if total + nums[j] > target:
                    break
                curr.append(nums[j])
                dfs(j + 1, curr, total + nums[j])
                curr.pop()
        dfs(0, [], 0)
        return res