class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for n in nums:
            nextPerms = []

            for p in res:
                for i in range(len(p) + 1):
                    copy = p.copy()
                    copy.insert(i, n)
                    nextPerms.append(copy)
            res = nextPerms
        return res