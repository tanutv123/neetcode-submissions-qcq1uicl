class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        perms = self.permute(nums[1:])
        res = []

        for p in perms:
            for j in range(len(p) + 1):
                copy = p.copy()
                copy.insert(j, nums[0])
                res.append(copy)

        return res