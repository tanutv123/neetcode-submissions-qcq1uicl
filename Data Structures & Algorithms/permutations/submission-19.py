class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.dfs([], nums, [False] * len(nums))
        return self.res

    def dfs(self, perm, nums, visit):
        if len(perm) == len(nums):
            self.res.append(perm.copy())
            return
        
        for i in range(len(nums)):
            if not visit[i]:
                perm.append(nums[i])
                visit[i]= True
                self.dfs(perm, nums, visit)
                perm.pop()
                visit[i] = False