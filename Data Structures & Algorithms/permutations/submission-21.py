class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visit = [False] * len(nums)
        def backtrack(perm):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            for i in range(len(nums)):
                if not visit[i]:
                    perm.append(nums[i])
                    visit[i] = True
                    backtrack(perm)
                    perm.pop()
                    visit[i] = False
        backtrack([])
        return res