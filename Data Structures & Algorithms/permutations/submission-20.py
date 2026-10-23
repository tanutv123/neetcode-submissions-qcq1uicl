class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not len(nums):
            return [[]]
        res = []
        perm = self.permute(nums[1:])
        for p in perm:
            for i in range(len(p) + 1):
                copy = p.copy()
                copy.insert(i, nums[0])
                res.append(copy)
        return res
        