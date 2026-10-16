class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack([], nums, [False] * len(nums))
        return self.res

    def backtrack(self, perm, nums, visit):
        if len(perm) == len(nums):
            self.res.append(perm.copy())
            return
        
        for i in range(len(nums)):
            if visit[i]:
                continue
            
            perm.append(nums[i])
            visit[i] = True
            self.backtrack(perm, nums, visit)
            perm.pop()
            visit[i] = False